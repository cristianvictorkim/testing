# TPO2 - Automatizacion de pruebas y pipeline CI/CD

Proyecto simple en Python para demostrar automatizacion de pruebas con `pytest` e integracion continua con GitHub Actions.

## Funcionalidad

La aplicacion calcula el total final de una compra aplicando descuentos segun el tipo de cliente:

- `regular`: 0%
- `premium`: 10%
- `vip`: 20%

## Estructura

```text
app/                 Codigo de la funcionalidad
tests/               Tests automatizados con pytest
docs/                Escenario y casos de prueba
.github/workflows/   Pipeline CI/CD
main.py              Ejecucion manual de ejemplo
requirements.txt     Dependencias
```

## Ejecutar localmente

```bash
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html
```

El reporte HTML queda disponible en `reports/report.html`.

## Pipeline

El workflow de GitHub Actions se ejecuta automaticamente en cada `push` y `pull_request`. Instala dependencias, ejecuta los tests y publica el reporte HTML como artefacto.
