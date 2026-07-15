# RollerShow — Manual de Marca

Manual de marca oficial de RollerShow, imprimible a PDF (Ctrl/Cmd + P), más un paquete versionado de activos listos para gráfica, web, redes y video.

- **Ver en vivo**: https://aguslaboral.github.io/rollershow-brand-manual/
- **Editar el manual**: `index.html`. Deploy automático a GitHub Pages al pushear a `main`.
- **Activos**: `brand-assets/` contiene logos, iconos, fotos de referencia, plantillas y hojas de producción. La descarga consolidada está en `downloads/`.
- **Regenerar el paquete**: ejecutar `powershell -ExecutionPolicy Bypass -File scripts/build-brand-assets.ps1` después de cambiar iconos, logos o plantillas. El script actualiza el manifiesto de integridad y el ZIP.
- **Para agentes (Claude/GPT/Codex)**: leer `AGENTS.md` antes de tocar nada.

Lo efímero (capturas, scripts de prueba) va en `_scratch/` (ignorado por git).
