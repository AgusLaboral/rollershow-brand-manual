# RollerShow Brand Manual — guía para agentes

Este repo contiene UNA sola pieza: el manual de marca de RollerShow (`index.html`, single-file HTML, imprimible a PDF). Es el gold standard que marca el ritmo del resto de los documentos de la marca. Leé este archivo entero antes de tocar nada: el manual pasó por muchas rondas de corrección con Agus y varias reglas no son obvias mirando solo el código.

## Datos del proyecto

- **Archivo único**: `index.html` (~1650 líneas). Cero dependencias salvo Google Fonts (Bricolage Grotesque + Manrope) y el logo SVG desde `https://assets.rollershow.com.ar/2021/img/rs_logo_animado_b.svg` (CDN real de producción, no inventar otro origen).
- **Repo GitHub**: `AgusLaboral/rollershow-brand-manual` (público, por GitHub Pages).
- **URL viva**: https://aguslaboral.github.io/rollershow-brand-manual/
- **Deploy**: `git push origin main` y esperar ~1 minuto. Este repo es SOLO del manual: nadie más pushea acá, no hay trampas de worktree. Después de cada push, verificar la URL viva con curl (HTTP 200 + un string del cambio) antes de reportar como hecho.
- Lo efímero (capturas, scripts de prueba) va en `_scratch/` (ignorado por git).

## Estructura del documento

Portada manifiesto (tesis: "RollerShow vende calidad y la calidad se nota antes de tocar el producto"; personalidad: "habla como un buen vendedor de local: cálido, directo y preciso, sin gritar") · 00 Cómo leer el manual (00.1 para qué existe: es árbitro y es el brief; 00.2 convenciones; 00.4 las 7 máximas) · 01 Marca · 02 Color (+ matriz de contraste WCAG medida) · 03 Tipografía · 04 Espaciado, grilla, sangrado, escala de espaciado · 05 Voz, copy, biblioteca de CTAs, ortotipografía · 06 Componentes web (+ anatomía y 5 estados del botón, campos y feedback) · 07 Papelería (presupuesto, firma, tarjeta, membrete) · 08 Redes (zonas seguras graficadas, plantillas de post y story) · 09 Fotografía · 10 Materia y efectos (fondos con nombre, elementos recurrentes, iconografía, catálogo sí/no, control final 10.9) · 11 Tokens (`<script type="application/json" id="rollershow-brand-tokens">` con TODO el sistema para lectura de máquina — mantenerlo sincronizado con cualquier cambio del cuerpo).

## Reglas duras (costaron rondas de corrección; no las rompas)

1. **Agnóstico de aplicaciones.** El manual no menciona bots, archivos, proyectos ni landings específicas. Si una pieza real contradice al manual, se corrige la pieza, no el manual (regla 00.2.3). Bugs encontrados en otros proyectos NO se documentan acá.
2. **Cero tells de diseño IA**: sin eyebrows (el numeral va fundido en el mismo renglón del título, `<span class="spec__title-num">`), sin cajas-dentro-de-cajas (separar solo con hairlines de 1px), sin pills de acción, sin dots de color pulsantes, sin checks/estrellas decorativas, sin contadores de urgencia.
3. **Cero tells de REDACCIÓN IA**: sin middots `·` ni em-dashes `—` en prosa propia (las únicas excepciones son los `<code>` de la regla 05.3.1 que los nombra); sin paralelismos contrastivos en serie tipo "X, no Y / A, no B" (Agus lo marcó explícitamente como tell de modelo); sin frases que nadie diría en voz alta — test: leer el texto como si se lo dijeras a un colega, si suena a documento se reescribe. Voseo rioplatense siempre.
4. **Un solo color de acción**: Rojo Teja `#C63A21` (glow `#D2451E`, profundo `#97290F`). Terracota `#B8662C` es acento de apoyo, nunca acción. Error de formulario = Rojo Profundo, nunca Teja. No existe verde de éxito (confirmación textual en Tinta); el único verde es del botón del canal de mensajes y está documentado como fuera de norma de contraste.
5. **`.clauses li` usa sangría colgante (número en `position:absolute`), NUNCA `display:grid`/`flex`.** Un grid de columnas fijas con contenido que mezcla `<b>`/`<code>`/`<a>` y texto suelto trata cada fragmento como celda y parte el texto en una palabra por línea — ya rompió el documento entero una vez. Para cualquier componente nuevo de número+prosa, copiar el patrón de `.clauses`.
6. **Logos del CDN nunca con altura fija**: el SVG es 11.5:1 de proporción, a `height:36px` mide ~415px de ancho y desborda un viewport de 375. Siempre `width:min(100%, Npx); height:auto`.
7. **Contenido con reglas numéricas (porcentajes, zonas, medidas) lleva SU diagrama al lado** — convención de plano técnico: zona rayada (hatch 45° teja al 14-16% de opacidad) + cota con tics y label. Ver 08.2 y 09.1 como referencia.
8. **Todo valor visible tiene que existir también en el JSON de tokens** (cap 11) y viceversa. El JSON debe parsear siempre (`JSON.parse` sin error).

## Cómo verificar (no hay screenshot fiable garantizado)

Nunca reportar "verificado" con solo conteos de DOM. Patrón mínimo tras cada cambio visual, corrido contra la URL viva:

```js
// overflow real (¡medir clientWidth real, no confiar en el preset mobile del browser!)
const vw = document.documentElement.clientWidth;
({vw, scrollW: document.documentElement.scrollWidth,
  over: [...document.querySelectorAll('*')].filter(el => el.getBoundingClientRect().right > vw + 2).length})
```

Y para layout de listas/patrones repetidos: medir `getBoundingClientRect().height` de todas las instancias y buscar outliers (un `<li>` de 400px delata texto fragmentado). Validación de sintaxis pre-commit:

```bash
python3 -c "
import re, json
s = open('index.html', encoding='utf-8').read()
for tag in ['section','div','ul','p','span']:
    o = len(re.findall(r'<'+tag+r'(?:\s[^>]*)?>', s)); c = len(re.findall(r'</'+tag+r'>', s))
    assert o==c, (tag,o,c)
json.loads(re.search(r'<script type=\"application/json\"[^>]*>(.*?)</script>', s, re.S).group(1))
print('OK')"
```

Antes de cerrar cualquier ronda, correr la propia checklist del manual (sección 10.9) sobre el documento mismo.

## Pendientes que necesitan a Agus

- **07.3 "Especimen completo" del presupuesto**: dice "Pendiente" a propósito. Agus va a pasar un presupuesto viejo real como referencia de formato. Cuando llegue: reconstruir el especimen con el componente `.paper` (la clase ya existe en el CSS) usando el formato real, y sacar la nota. **No inventar un presupuesto de ejemplo** — ya se hizo y se pidió sacarlo.
- Datos duros de papelería (CUIT, direcciones exactas de los locales) si el membrete pasa a producción. Los locales son Villa Carlos Paz y Capital Federal — **nunca** "Córdoba Capital", no existe local ahí.

## Historial de decisiones grandes (por qué el manual es como es)

- v0.x: mockup de un capítulo → Agus validó la piel editorial (hairlines, radio 0 en la estructura, numeración fundida) tras rechazar dos versiones con tells de IA.
- v1.0: 12 capítulos → se detectó y arregló el bug de `.clauses` con grid.
- v1.1: se volvió agnóstico (fuera Ulises/archivos/proyectos, fuera "confirmado/propuesto", fuera capítulo de plantillas conversacionales de WhatsApp — eso es material operativo, no de manual gráfico) y se pobló con recursos: fondos con nombre (Amanecer de lino / Brasa / Penumbra), elementos recurrentes (Banda de color, Hairline, Trama de tejido, Folio), biblioteca de CTAs, contraste medido, aplicaciones por fondo, iconografía propia, diagramas con cotas, tarjeta, membrete, plantillas de post y story, checklist final.
- v1.2: portada manifiesto + personalidad + sección "para qué existe". Luego reescrita en voz natural al detectar tells de redacción.
