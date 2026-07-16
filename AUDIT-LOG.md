# Registro de inconsistencias del manual

Este archivo reúne contradicciones, vacíos y reglas que produjeron resultados ambiguos en implementaciones reales. No reemplaza `CANDIDATES.md`: un candidato es un recurso nuevo en evaluación; una inconsistencia es una regla vigente que falta, se contradice o induce una aplicación incorrecta.

## Estados

- **Abierta**: la inconsistencia está comprobada y todavía no fue corregida en el manual.
- **En corrección**: ya existe una solución verificada y falta incorporarla al cuerpo, tokens o activos.
- **Resuelta**: la versión indicada del manual ya contiene la corrección.
- **No corresponde**: era un bug particular de una pieza y no un problema del sistema general.

## Abiertas

| ID | Fecha | Hallazgo y evidencia | Riesgo | Corrección pendiente | Estado |
|---|---|---|---|---|---|
| DIM-001 | 2026-07-16 | El manual sólo documenta la cota técnica horizontal con línea y tics. Cortina Viva aplicó esa firma a los campos Ancho y Alto, por lo que Alto quedó representado como una medida horizontal. La corrección verificable está en [`rollershow-cortina-viva@50ee23d`](https://github.com/AgusLaboral/rollershow-cortina-viva/commit/50ee23d): reutiliza los iconos de dimensión que ya existen en la landing del cotizador y el simulador. | Confundir un diagrama técnico con un selector UI produce semántica falsa aunque el valor sea correcto. | Separar en el capítulo 06/10 dos usos: cota técnica sobre escena o diagrama = línea, tics y valor; selector de medidas = flecha bidireccional horizontal para Ancho y vertical para Alto. Incluir ambos SVG como activos o snippets canónicos y reflejar la distinción en los tokens legibles por máquina. | En corrección |
| DOC-002 | 2026-07-15 | La sección 07.3 todavía necesita un presupuesto real aprobado para construir el espécimen completo. | Inventar datos o estructura comercial convertiría el manual en una fuente falsa. | Incorporar el espécimen únicamente cuando Agus entregue un presupuesto real de referencia. | Abierta |
| PRINT-001 | 2026-07-15 | Faltan CUIT y direcciones confirmadas si el membrete pasa a producción. | Una pieza imprimible podría publicar datos incompletos o incorrectos. | Completar sólo con información oficial; los locales conocidos son Villa Carlos Paz y Capital Federal. | Abierta |

## Resueltas

| ID | Versión | Inconsistencia corregida | Resolución |
|---|---|---|---|
| ID-001 | v1.8 | El documento mencionaba una marca compacta inexistente. | Se eliminó la contradicción y quedó explícito que sólo existe el wordmark completo aprobado. |
| DOC-001 | v1.9 | El índice anunciaba un ejemplo de cotización que el manual no incluía. | Se corrigió el índice y el futuro espécimen quedó condicionado a un presupuesto real. |
| COPY-001 | v2.0 | La portada comenzaba desde “cotizar” sin explicar qué hace RollerShow; varios CTA no nombraban el objeto. | La apertura presenta empresa, producto y función; las acciones nombran las cortinas a medida. |
| UI-001 | v2.1 | El stepper podía separar o superponer cifra y unidad y no aseguraba un área táctil consistente. | Cifra y unidad pasaron a ser un grupo inseparable con controles mínimos de 44 px. |
| GOV-001 | v2.2 | El manual podía interpretarse como techo creativo y no tenía circuito para aprendizajes externos. | Se creó `INTEGRATION.md` y `CANDIDATES.md`; una implementación aprobada puede volver al sistema como estándar. |

## Regla de uso

Cada entrada nueva debe incluir una implementación, captura o commit verificable. Cuando se resuelve, se mueve a “Resueltas” indicando la versión del manual. Los bugs particulares permanecen en el repositorio donde aparecieron; entran acá únicamente cuando exponen un vacío o una contradicción reutilizable del sistema.
