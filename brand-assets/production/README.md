# Producción de color

HEX y RGB son la fuente de verdad digital. No existe una conversión CMYK universal: cambia según perfil, tinta, máquina y soporte.

Antes de una primera tirada con un proveedor o material nuevo:

1. El proveedor informa perfil ICC, máquina y soporte.
2. Convierte los colores desde los valores digitales del manual.
3. Imprime `print-proof-sheet.svg` al 100%, sin “mejoras automáticas”.
4. Se compara la prueba con la pantalla calibrada y con una pieza aprobada.
5. Se anotan perfil, soporte, fecha, valores resultantes y responsable.
6. Esa combinación queda aprobada para repetirla. Un cambio de soporte o máquina exige otra prueba.

No publicar una tabla CMYK genérica como si fuera exacta. La prueba física aprobada manda.
