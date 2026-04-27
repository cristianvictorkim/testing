# Escenario de prueba

## Contexto

Se desarrolla un sistema simple de descuentos para una tienda. La funcion recibe el subtotal de una compra y el tipo de cliente. Segun el tipo de cliente, aplica el descuento correspondiente y devuelve el total final.

Tipos de cliente:

- `regular`: 0% de descuento
- `premium`: 10% de descuento
- `vip`: 20% de descuento

## Casos de prueba

| Caso | Tipo | Datos de entrada | Resultado esperado |
| --- | --- | --- | --- |
| Compra cliente premium | Caso exitoso | subtotal `1000`, cliente `premium` | descuento `100`, total final `900` |
| Subtotal negativo | Caso de error | subtotal `-1`, cliente `regular` | se lanza `ValueError` porque el subtotal no puede ser negativo |
| Compra con subtotal cero | Caso borde | subtotal `0`, cliente `vip` | descuento `0`, total final `0` |
| Cliente con espacios y mayusculas | Caso adicional | subtotal `500`, cliente ` VIP ` | se normaliza a `vip`, descuento `100`, total final `400` |
