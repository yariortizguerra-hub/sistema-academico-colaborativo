# Caso práctico 01: Control de versiones y colaboración para un sistema académico

**Empresa ficticia:** TecnoAula Perú S.A.C.  
**Área:** Desarrollo de Software  
**Equipo:** 3 estudiantes  
**Duración estimada:** 6–8 horas  
**Herramientas:** Git, GitHub, Visual Studio Code y Python 3.10+

## Objetivo
Implementar un flujo colaborativo con Git y GitHub: repositorio, ramas, commits, Issues, Pull Requests, revisión, resolución de conflictos, pruebas y documentación.

## Funcionalidades del prototipo
- Registrar estudiantes en memoria.
- Validar código, nombre y programa de estudios.
- Listar los estudiantes registrados.
- Ejecutar pruebas automatizadas con `unittest`.

> Este prototipo es didáctico: no utiliza base de datos y los datos se pierden al cerrar el programa.

## Requisitos
- Git instalado.
- Python 3.10 o posterior.
- Cuenta de GitHub.
- Editor recomendado: Visual Studio Code.

## Ejecución local
Desde la carpeta raíz del proyecto:

```powershell
python -m src.main
```

Ejecutar las pruebas:

```powershell
python -m unittest discover -s tests -v
```

## Estructura
```text
sistema-academico-colaborativo/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── tarea.md
│   │   └── error.md
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── alcance.md
│   ├── guia-ejecucion.md
│   ├── guia-conflictos.md
│   ├── plan-pruebas.md
│   ├── rubrica.md
│   ├── evidencias.md
│   └── informe-final.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── estudiantes.py
├── tests/
│   └── test_estudiantes.py
├── .gitignore
└── README.md
```

## Flujo de ramas sugerido
- `main`: versión estable.
- `dev`: integración de funcionalidades.
- `feature/registro-estudiantes`: registro.
- `feature/listado-estudiantes`: listado.
- `docs/guia-proyecto`: documentación.

## Convención de commits
- `feat:` funcionalidad nueva.
- `fix:` corrección.
- `docs:` documentación.
- `test:` pruebas.
- `refactor:` mejora interna.

Ejemplos:
```bash
git commit -m "feat: agrega registro de estudiantes"
git commit -m "test: agrega pruebas de validacion"
git commit -m "docs: explica ejecucion del proyecto"
```

## Flujo colaborativo recomendado
1. Crear un Issue para cada tarea.
2. Actualizar la rama `dev`.
3. Crear una rama de trabajo.
4. Implementar un cambio pequeño y probarlo.
5. Hacer commit y publicar la rama.
6. Abrir Pull Request hacia `dev`.
7. Solicitar revisión a otro integrante.
8. Corregir observaciones y fusionar.
9. Probar `dev`; integrar a `main` cuando esté estable.

## Seguridad
Nunca publiques contraseñas, tokens, claves privadas ni archivos `.env` con secretos. `.gitignore` evita algunos archivos, pero no elimina secretos que ya fueron confirmados en un commit.

## Limitaciones
El proyecto no persiste datos, no autentica usuarios y no debe usarse como sistema académico de producción.
