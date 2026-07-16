# RollerShow — Manual de Marca

Manual de marca oficial de RollerShow, imprimible a PDF (Ctrl/Cmd + P), más un paquete versionado de activos listos para gráfica, web, redes y video.

- **Ver en vivo**: https://aguslaboral.github.io/rollershow-brand-manual/
- **Repositorio canónico**: https://github.com/AgusLaboral/rollershow-brand-manual
- **Integrarlo en otro proyecto**: leer [`INTEGRATION.md`](INTEGRATION.md). Contiene la instrucción lista para citar en Codex, Claude u otro agente.
- **Editar el manual**: `index.html`. Deploy automático a GitHub Pages al pushear a `main`.
- **Activos**: `brand-assets/` contiene logos, iconos, fotos de referencia, plantillas y hojas de producción. La descarga consolidada está en `downloads/`.
- **Regenerar el paquete**: ejecutar `powershell -ExecutionPolicy Bypass -File scripts/build-brand-assets.ps1` después de cambiar iconos, logos o plantillas. El script actualiza el manifiesto de integridad y el ZIP.
- **Para agentes (Claude/GPT/Codex)**: leer `AGENTS.md` antes de tocar nada.

## Un estándar vivo

El manual es una guía de partida, no un techo creativo. Una herramienta, animación o tecnología nueva no se rechaza por estar ausente. Se conserva la propuesta, se explican sus diferencias con el sistema actual y se pide aprobación. Cuando una implementación final aprobada aporta una solución reutilizable, el aprendizaje vuelve a este repositorio y se incorpora al manual, los datos estructurados, los activos y el historial correspondientes.

Las propuestas todavía no aprobadas se registran en [`CANDIDATES.md`](CANDIDATES.md). Solo lo aprobado entra al manual como estándar vigente.

Lo efímero (capturas, scripts de prueba) va en `_scratch/` (ignorado por git).
