# Plan de pruebas

## Pruebas funcionales
| ID | Caso | Resultado esperado |
|---|---|---|
| P01 | Registrar estudiante con datos válidos | Se agrega un registro |
| P02 | Código vacío | Se genera `ValueError` |
| P03 | Nombre vacío | Se genera `ValueError` |
| P04 | Programa vacío | Se genera `ValueError` |
| P05 | Código duplicado | Se rechaza el segundo registro |
| P06 | Listar varios registros | Se devuelve lista ordenada por código |

## Ejecución
```bash
python -m unittest discover -s tests -v
```

## Criterio de aprobación
Todas las pruebas automatizadas deben finalizar con estado `OK`. Registra el resultado real; no sustituyas la ejecución por una captura ilustrativa.

## Pruebas de colaboración
- La rama de funcionalidad se publicó en GitHub.
- El Pull Request apunta a `dev`.
- Al menos otro integrante revisó el cambio.
- El cambio se integró después de atender observaciones.
- El historial muestra commits comprensibles.
