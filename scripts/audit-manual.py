# Auditoría integral del manual de marca. Uso:
#   python scripts/audit-manual.py            -> audita la URL viva
#   python scripts/audit-manual.py local      -> audita el index.html local
# Requiere: playwright (sync). Sale con código 1 si hay hallazgos.
import json
import re
import sys
import urllib.request

LIVE = "https://aguslaboral.github.io/rollershow-brand-manual/"
LOCAL = "file:///C:/Users/Agus/Desktop/rollershow-brand-manual/index.html"

SWEEP = r"""() => {
  const segs = [];
  for (const el of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) continue;
    const solid = (w, st, col) => parseFloat(w) > 0 && st === 'solid' && !/rgba\(\d+, \d+, \d+, 0\)/.test(col);
    const push = side => segs.push({side, r, cls: (typeof el.className==='string'?el.className.split(' ')[0]:el.tagName)});
    if (solid(cs.borderTopWidth, cs.borderTopStyle, cs.borderTopColor)) push('top');
    if (solid(cs.borderBottomWidth, cs.borderBottomStyle, cs.borderBottomColor)) push('bottom');
    if (solid(cs.borderLeftWidth, cs.borderLeftStyle, cs.borderLeftColor)) push('left');
    if (solid(cs.borderRightWidth, cs.borderRightStyle, cs.borderRightColor)) push('right');
  }
  const out = []; const seen = new Set();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    if (!n.textContent.trim() || n.textContent.trim().length < 2) continue;
    if (n.parentElement.closest('svg')) continue;
    const range = document.createRange(); range.selectNodeContents(n);
    const t = range.getBoundingClientRect();
    if (t.width === 0 || t.height === 0) continue;
    for (const s of segs) {
      const sr = s.r;
      if (s.side === 'left' || s.side === 'right') {
        const x = s.side === 'left' ? sr.left : sr.right;
        const ov = Math.min(t.bottom, sr.bottom) - Math.max(t.top, sr.top);
        if (ov > t.height * 0.5) {
          const gL = t.left - x, gR = x - t.right;
          if ((gL >= 0 && gL < 5) || (gR >= 0 && gR < 5)) {
            const k = s.cls + '|' + n.textContent.trim().slice(0,20);
            if (!seen.has(k)) { seen.add(k); out.push(n.textContent.trim().slice(0,30) + ' @ ' + s.cls + '/' + s.side); }
          }
        }
      } else {
        const y = s.side === 'top' ? sr.top : sr.bottom;
        const ov = Math.min(t.right, sr.right) - Math.max(t.left, sr.left);
        if (ov > t.width * 0.5) {
          const gT = t.top - y, gB = y - t.bottom;
          if ((gT >= 0 && gT < 4) || (gB >= 0 && gB < 4)) {
            const k = s.cls + s.side + '|' + n.textContent.trim().slice(0,20);
            if (!seen.has(k)) { seen.add(k); out.push(n.textContent.trim().slice(0,30) + ' @ ' + s.cls + '/' + s.side); }
          }
        }
      }
    }
  }
  return out;
}"""

def static_checks(html):
    problems = []
    for tag in ['section', 'div', 'ul', 'p', 'span']:
        o = len(re.findall(r'<' + tag + r'(?:\s[^>]*)?>', html))
        c = len(re.findall(r'</' + tag + r'>', html))
        if o != c:
            problems.append(f"tags desbalanceados: {tag} {o}/{c}")
    try:
        json.loads(re.search(r'<script type="application/json"[^>]*>(.*?)</script>', html, re.S).group(1))
    except Exception as e:
        problems.append(f"JSON de tokens no parsea: {e}")
    ids = set(re.findall(r'id="([^"]+)"', html))
    problems += [f"ancla rota: #{a}" for a in re.findall(r'href="#([^"]+)"', html) if a not in ids]
    prose = re.sub(r'<code[^>]*>.*?</code>', '', html, flags=re.S)
    prose = re.sub(r'<script.*?</script>', '', prose, flags=re.S)
    prose = re.sub(r'<svg.*?</svg>', '', prose, flags=re.S)
    tells = len(re.findall(r'[—·]', prose))
    if tells:
        problems.append(f"tells (em-dash/middot) en prosa: {tells}")
    return problems

def main():
    target = LOCAL if 'local' in sys.argv else LIVE
    problems = []
    if target == LIVE:
        html = urllib.request.urlopen(LIVE, timeout=30).read().decode('utf-8')
    else:
        html = open('index.html', encoding='utf-8').read()
    problems += static_checks(html)

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w in (1280, 620, 375):
            pg = b.new_page(viewport={"width": w, "height": 900})
            errors = []
            pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.goto(target)
            pg.wait_for_timeout(1500)
            for hit in pg.evaluate(SWEEP):
                problems.append(f"[{w}px] texto pegado a linea: {hit}")
            ov = pg.evaluate("() => document.documentElement.scrollWidth - document.documentElement.clientWidth")
            if ov:
                problems.append(f"[{w}px] overflow horizontal: {ov}px")
            for src in pg.evaluate("() => [...document.images].filter(i => !i.naturalWidth).map(i => i.src)"):
                problems.append(f"[{w}px] imagen rota: {src}")
            for e in errors:
                problems.append(f"[{w}px] error de consola: {e[:120]}")
            if w == 1280:
                t1 = pg.evaluate("() => [...document.querySelectorAll('.doc-head__brand *')].map(e => getComputedStyle(e).transform).join('|')")
                pg.wait_for_timeout(900)
                t2 = pg.evaluate("() => [...document.querySelectorAll('.doc-head__brand *')].map(e => getComputedStyle(e).transform).join('|')")
                if t1 == t2:
                    problems.append("el logo del header NO esta rotando (regla 01.1)")
            pg.close()
        b.close()

    if problems:
        print(f"AUDITORIA: {len(problems)} hallazgos")
        for x in problems:
            print(" -", x)
        sys.exit(1)
    print("AUDITORIA: limpia (sintaxis, JSON, anclas, tells, barrido geometrico 1280/620/375, overflow, imagenes, consola, logo animado)")

if __name__ == '__main__':
    main()
