# Candidatos al sistema de marca

Este registro conserva recursos nuevos descubiertos en implementaciones reales antes de que entren al manual. Estar acá significa “en evaluación”, no “aprobado” ni “prohibido”.

## Estados

- **Prueba**: existe una implementación visible y reversible.
- **Pendiente de aprobación**: la comparación con el manual está documentada y espera decisión de Agus.
- **Aprobado para incorporar**: Agus aprobó el resultado final; falta actualizar el manual, los tokens o los activos.
- **Incorporado**: ya forma parte de una versión publicada del manual.
- **Descartado**: se probó y no se adopta; se conserva el motivo para no repetir la evaluación.

## Registro

| Fecha | Recurso | Implementación verificable | Qué cambia | Valor aportado | Estado | Decisión |
|---|---|---|---|---|---|---|
| 2026-07-16 | Escena inmersiva de luz y tela | [`rollershow-cortina-viva@8b10c8b`](https://github.com/AgusLaboral/rollershow-cortina-viva/commit/8b10c8b), [`4add6f3`](https://github.com/AgusLaboral/rollershow-cortina-viva/commit/4add6f3), [`9a84684`](https://github.com/AgusLaboral/rollershow-cortina-viva/commit/9a84684) | Suma luz causal, translucidez textil graduada, física de terminaciones, perfiles full/lite, movimiento sutil del dispositivo y QA por silueta real. | Permite comparar telas por su efecto sobre un mismo ambiente sin perder materialidad ni funcionamiento en equipos limitados. | Incorporado en v2.3 | Agus aprobó el resultado y pidió guardarlo como aprendizaje reutilizable. |
| 2026-07-16 | Navegación editorial de escena | [`rollershow-cortina-viva@7c237f3`](https://github.com/AgusLaboral/rollershow-cortina-viva/commit/7c237f3) | Define Anterior/Siguiente como controles transparentes con palabra, flecha, penumbra localizada y hairline direccional. | Mantiene orientación y accesibilidad sobre una escena compleja sin competir con el CTA primario. | Incorporado en v2.4 | Agus detectó que el desarrollo aprobado no estaba representado dentro del manual y pidió incorporarlo. |

No se agregan candidatos sin evidencia. Cada fila debe enlazar una página, captura versionada o commit accesible y nombrar quién tomó la decisión.
