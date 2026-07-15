# RollerShow Brand Manual — guía para agentes

Este repo contiene el manual de marca de RollerShow (`index.html`, single-file HTML, imprimible a PDF) y su paquete versionado de activos (`brand-assets/` + `downloads/`). Es el gold standard que marca el ritmo del resto de los documentos de la marca. Leé este archivo entero antes de tocar nada: el manual pasó por muchas rondas de corrección con Agus y varias reglas no son obvias mirando solo el código.

## Datos del proyecto

- **Manual**: `index.html`. Cero dependencias de ejecución salvo Google Fonts (Bricolage Grotesque + Manrope) y recursos propios.
- **Activos**: `brand-assets/` contiene maestros y plantillas editables; `brand-assets/manifest.json` registra versión, peso y SHA-256; `downloads/rollershow-brand-assets-v1.0.2.zip` es la entrega consolidada.
- **Generador**: `scripts/build-brand-assets.ps1` toma el logo oficial, extrae los 16 iconos del manual, copia las fotos reales de referencia, recalcula el manifiesto y recompone el ZIP. Ejecutarlo después de cualquier cambio en esos recursos.
- **Repo GitHub**: `AgusLaboral/rollershow-brand-manual` (público, por GitHub Pages).
- **URL viva**: https://aguslaboral.github.io/rollershow-brand-manual/
- **Deploy**: `git push origin main` y esperar ~1 minuto. Este repo es SOLO del manual: nadie más pushea acá, no hay trampas de worktree. Después de cada push, verificar la URL viva con curl (HTTP 200 + un string del cambio) antes de reportar como hecho.
- Lo efímero (capturas, scripts de prueba) va en `_scratch/` (ignorado por git).

## Estructura del documento

Portada manifiesto · 00 Cómo leer y gobernar el manual · 01 Marca, archivos y convivencia con terceros · 02 Color y producción impresa · 03 Tipografía y licencias · 04 Espaciado, grilla y movimiento · 05 Voz, nomenclatura y claims · 06 Componentes web y accesibilidad · 07 Papelería · 08 Redes y video · 09 Fotografía y derechos · 10 Materia, iconografía, diagramas técnicos y control final · 11 Tokens (`<script type="application/json" id="rollershow-brand-tokens">` con TODO el sistema para lectura de máquina; mantenerlo sincronizado con cualquier cambio del cuerpo).

## Definiciones de marca dictadas por Agus (canon, no reinterpretar)

- **Tesis confirmada (versión completa, corregida por Agus)**: la experiencia empieza antes del presupuesto, en un anuncio, una recomendación o la primera conversación; sigue en el asesoramiento, el presupuesto, la fabricación y la instalación; continúa en el uso, el cuidado y la posventa real; y vuelve a empezar en la recomendación. Atención, tecnología y estética son un proceso conectado, y quien compra el producto más accesible recibe la misma experiencia que quien compra el más premium. El manual usa este recorrido como criterio para guiar gráfica, web, impresos y movimiento; su función principal sigue siendo gráfica y operativa.
- **Retórica prohibida en títulos y prosa** (Agus los marcó como tells de IA): tricolones con remate ("Un logotipo, dos versiones, cero excepciones"), negativo-para-afirmar ("Dos familias, ningún atajo", "se habla como X, no como Y"), paralelismos aforísticos ("La luz siempre cálida, la cortina siempre protagonista"). Los títulos dicen qué contiene el capítulo, directo.
- **Concepto ancla "real"**: productos reales, atención real, equipo real y posventa real. Viene de Nicolás y Agus pidió aplicarlo a lo largo del documento donde amerite. En portada se resume como "Productos reales. Atención real. Posventa real.".
- **Espectro de catálogo**: va del producto intermedio a muy buen precio hasta el de altísima calidad. Se comunica como rango ("del mejor precio a la más alta calidad"), nunca con precios ni modelos específicos.
- **Trayectoria (claim corregido por Agus)**: el claim correcto es "la empresa con más trayectoria vendiendo cortinas a medida ONLINE en la Argentina". Nunca omitir el "online": sin esa palabra el claim es falso.
- **Tríada real**: "Productos reales. Atención real. Posventa real." es el statement de portada. La garantía queda como una prueba concreta dentro de la posventa, no como sustituto de toda la experiencia posterior a la compra.
- **Bajada "Cortinas como imaginás"**: adoptada como bajada de trabajo (visible en portada y especificada en 01.6). Puede afinarse antes de un lanzamiento formal; los ajustes se registran en 01.6.
- **Color de excepción "Bosque" #1F3D2B** (02.8): solo campañas premium y ediciones limitadas; nunca UI diaria; nunca en la misma pieza que el Rojo Teja; sin variantes ni degradés.
- **Registro de redacción**: las partes blandas se escriben como los grandes manuales de marca, hablando de la marca en sí, con lenguaje agnóstico del lector (nada de conceptos internos del negocio que un lector externo no conoce). Lo técnico se mantiene técnico y claro. Prohibidos además de los tells de siempre: comparaciones autorreferenciales y frases que nadie diría en voz alta.

## Reglas duras (costaron rondas de corrección; no las rompas)

1. **Agnóstico de aplicaciones.** El manual no menciona bots, archivos, proyectos ni landings específicas. Si una pieza real contradice al manual, se corrige la pieza, no el manual (regla 00.2.3). Bugs encontrados en otros proyectos NO se documentan acá.
2. **Cero tells de diseño IA**: sin eyebrows (el numeral va fundido en el mismo renglón del título, `<span class="spec__title-num">`), sin cajas-dentro-de-cajas (separar solo con hairlines de 1px), sin pills de acción, dots de color, checks/estrellas decorativas, cifras que cuentan, revelados genéricos de scroll, blobs/auroras, resaltados marcador ni cards de selección con radio circular. Prohibida también cualquier barra vertical de color que marque selección, éxito, error o estado: cambiar radio por barra conserva el mismo patrón genérico. El estado se resuelve mediante contenido, jerarquía y función.
3. **Cero tells de REDACCIÓN IA**: sin middots `·` ni em-dashes `—` en prosa propia (las únicas excepciones son los `<code>` de la regla 05.3.1 que los nombra); sin paralelismos contrastivos en serie tipo "X, no Y / A, no B" (Agus lo marcó explícitamente como tell de modelo); sin frases que nadie diría en voz alta — test: leer el texto como si se lo dijeras a un colega, si suena a documento se reescribe. Voseo rioplatense siempre.
4. **Un solo color de acción**: Rojo Teja `#C63A21` (glow `#D2451E`, profundo `#97290F`). Terracota `#B8662C` es acento de apoyo, nunca acción. Error de formulario = Rojo Profundo, nunca Teja. No existe verde de éxito (confirmación textual en Tinta); el único verde es del botón del canal de mensajes y está documentado como fuera de norma de contraste.
5. **`.clauses li` usa sangría colgante (número en `position:absolute`), NUNCA `display:grid`/`flex`.** Un grid de columnas fijas con contenido que mezcla `<b>`/`<code>`/`<a>` y texto suelto trata cada fragmento como celda y parte el texto en una palabra por línea — ya rompió el documento entero una vez. Para cualquier componente nuevo de número+prosa, copiar el patrón de `.clauses`.
6. **Logos del CDN nunca con altura fija**: el SVG es 11.5:1 de proporción, a `height:36px` mide ~415px de ancho y desborda un viewport de 375. Siempre `width:min(100%, Npx); height:auto`.
7. **Contenido con reglas numéricas (porcentajes, zonas, medidas) lleva SU diagrama al lado** — convención de plano técnico: zona rayada (hatch 45° teja al 14-16% de opacidad) + cota con tics y label. Ver 08.2 y 09.1 como referencia.
8. **Todo valor visible tiene que existir también en el JSON de tokens** (cap 11) y viceversa. El JSON debe parsear siempre (`JSON.parse` sin error).
9. **Movimiento de marca nacido del producto, no efectos sueltos.** Biblioteca aprobada: roller sunscreen que baja/cubre/sube, comparador de luz táctil, tela física que responde al puntero, trama reactiva y Cota activa. Toda transición declara disparador, propiedad, duración, curva, interrupción y versión reducida. Canon: salida 140ms, feedback 180ms, estado 280ms, escena 480ms, material 620ms y roller completa 1200ms; las recetas exactas viven en 04.4 y los tokens. En producción no hay loops decorativos en botones, textos, fondos o métricas.
10. **No existe marca compacta aprobada.** El maestro vigente es el wordmark completo de proporción 11.54:1. No recortar una R, una O ni otro fragmento para fabricar favicon, avatar o isotipo. Si la necesidad aparece, se abre un proceso de diseño y aprobación específico.
11. **El paquete y el manual son una unidad.** Toda referencia descargable debe existir, abrir y estar incluida en el manifiesto y el ZIP. Después de tocar logos, iconos, fotos o plantillas, regenerar el paquete y verificar enlaces y hashes.

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

Para reconstruir y validar la entrega de activos:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build-brand-assets.ps1
```

Comprobar además que el ZIP, el manifiesto y cada enlace de descarga respondan en la URL viva.

## Pendientes que necesitan a Agus

- **07.3 "Especimen completo" del presupuesto**: dice "Pendiente" a propósito. Agus va a pasar un presupuesto viejo real como referencia de formato. Cuando llegue: reconstruir el especimen con el componente `.paper` (la clase ya existe en el CSS) usando el formato real, y sacar la nota. **No inventar un presupuesto de ejemplo** — ya se hizo y se pidió sacarlo.
- Datos duros de papelería (CUIT, direcciones exactas de los locales) si el membrete pasa a producción. Los locales son Villa Carlos Paz y Capital Federal — **nunca** "Córdoba Capital", no existe local ahí.

## Historial de decisiones grandes (por qué el manual es como es)

- v0.x: mockup de un capítulo → Agus validó la piel editorial (hairlines, radio 0 en la estructura, numeración fundida) tras rechazar dos versiones con tells de IA.
- v1.0: 12 capítulos → se detectó y arregló el bug de `.clauses` con grid.
- v1.1: se volvió agnóstico (fuera Ulises/archivos/proyectos, fuera "confirmado/propuesto", fuera capítulo de plantillas conversacionales de WhatsApp — eso es material operativo, no de manual gráfico) y se pobló con recursos: fondos con nombre (Amanecer de lino / Brasa / Penumbra), elementos recurrentes (Banda de color, Hairline, Trama de tejido, Folio), biblioteca de CTAs, contraste medido, aplicaciones por fondo, iconografía propia, diagramas con cotas, tarjeta, membrete, plantillas de post y story, checklist final.
- v1.2: portada manifiesto + personalidad + sección "para qué existe". Luego reescrita en voz natural al detectar tells de redacción.
- v1.3: la tesis pasó a cubrir el recorrido completo desde anuncio o recomendación hasta uso, posventa y nueva recomendación, sin desplazar la función gráfica del manual. Color se convirtió en inventario completo y se corrigió la falsa prohibición de logo Tinta sobre Arena. Movimiento sumó niveles, tokens, accesibilidad y recursos propios de medida, ambientes y control de luz.
- v1.4: se eliminaron Cifra viva, auroras, marcador y movimientos genéricos. Se incorporaron recursos reales de RollerShow (roller de transición, comparador táctil, tela física y trama reactiva), selección editorial sin radio-card, estados completos de formularios, avisos, membrete detallado, fondos revisados e iconografía para todo el recorrido.
- v1.5: la selección dejó de representarse mediante una barra lateral o cualquier marcador decorativo. El producto activo pasa a ser el contenido principal y las alternativas son acciones de comparación. La prohibición se extendió a avisos y a todo estado de interfaz.
- v1.6: movimiento pasó de tokens sueltos a recetas operativas. Se definieron duración, curva, propiedades, disparador, interrupción y movimiento reducido para feedback, estados, cambios de escena, respuesta material, comparadores, Cota activa y la secuencia roller completa de 1200ms.
- v1.7: el manual pasó a ser un sistema entregable. Se corrigió el maestro del logo y su proporción, se explicitó que no existe marca compacta aprobada, y se agregó un paquete verificable con logos, 16 iconos, fotos reales de referencia, plantillas editables y hojas de producción. El cuerpo sumó gobierno, co-branding, impresión, licencias, nomenclatura y claims, accesibilidad, video, derechos de imagen y diagramas técnicos.
- v1.8: se eliminó el lenguaje interno de IA del documento público, las etiquetas visuales tipo eyebrow y las referencias que normalizaban cards. Se corrigió la contradicción de “logo compacto” y el stepper pasó a ser operable con teclado sin imponer un rango que pertenezca a una colección específica.
- v1.9: se corrigió la referencia de índice que anunciaba una cotización de ejemplo inexistente. La sección 07 ahora nombra lo que entrega hoy y explicita que el futuro espécimen se construye desde un presupuesto aprobado, nunca ficticio.
