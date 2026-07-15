# RollerShow Brand Assets 1.1.0

Este paquete acompaña al Manual de Marca v2.0. Los archivos se usan sin redibujar, deformar ni recolorear fuera de las versiones provistas.

## Contenido

- `logo/`: wordmark oficial animado y fotogramas estáticos Tinta y Blanco.
- `icons/`: biblioteca de 16 íconos SVG en retícula de 24px.
- `photography/`: dos referencias reales para calibrar encuadre, luz y tratamiento.
- `templates/`: originales SVG editables para post, story, reel y hoja membretada.
- `production/`: hoja de control para una prueba física de color.
- `fonts/`: fuentes, pesos y licencias.
- `manifest.json`: versión, tamaño y SHA-256 de cada archivo.

## Marca compacta

No existe un isotipo ni un favicon compacto aprobado. Las dos “O” animadas pertenecen al wordmark completo y no se recortan. Tampoco se crea una “R” dentro de un círculo. Hasta que exista un dibujo maestro aprobado, en espacios menores al mínimo del logo se omite la marca gráfica y se conserva el nombre en el contenido o metadata de la plataforma.

## Fuentes de verdad

- Logo: archivo de producción `rollershow/img/logo.svg`, idéntico al SVG público del CDN.
- Familias, colecciones y garantías: API pública `https://www.rollershow.com.ar/api/v2`.
- Fotografía: originales usados en la web de RollerShow, conservados como referencia y no como banco libre.

El ZIP público se genera con `scripts/build-brand-assets.ps1`. No editar el ZIP a mano.
