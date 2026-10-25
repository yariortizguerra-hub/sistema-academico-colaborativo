# Guía de ejecución paso a paso

## Fase 1. Preparar el entorno
En PowerShell o en la terminal de VS Code:

```powershell
git --version
python --version
git config --global user.name "Nombre del Estudiante"
git config --global user.email "correo-que-usas-en-git@example.com"
git config --global --list
```

Usa tu nombre y correo reales apropiados para los commits. No compartas tokens ni contraseñas.

## Fase 2. Crear el repositorio remoto
1. En GitHub, crea un repositorio llamado `sistema-academico-colaborativo`.
2. Para esta práctica, puedes crearlo vacío, sin README ni `.gitignore`, porque esos archivos vienen en el proyecto.
3. Copia la URL HTTPS del repositorio.

Si partes de esta carpeta ya descargada, abre una terminal aquí y ejecuta:

```bash
git init
git branch -M main
git add .
git commit -m "chore: crea estructura inicial del proyecto"
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

Reemplaza `URL_DEL_REPOSITORIO` por la URL copiada de tu repositorio. No escribas literalmente ese texto.

## Fase 3. Crear la rama de integración
```bash
git switch -c dev
git push -u origin dev
```

## Fase 4. Trabajar en una funcionalidad
Antes de empezar una tarea, actualiza `dev`:

```bash
git switch dev
git pull origin dev
git switch -c feature/registro-estudiantes
```

Edita los archivos necesarios y ejecuta las pruebas:

```bash
python -m unittest discover -s tests -v
git status
git diff
git add src/estudiantes.py tests/test_estudiantes.py
git commit -m "feat: implementa registro de estudiantes"
git push -u origin feature/registro-estudiantes
```

## Fase 5. Abrir Pull Request
1. En GitHub, abre un Pull Request desde `feature/registro-estudiantes` hacia `dev`.
2. Explica qué cambió, cómo probarlo y qué Issue resuelve.
3. Solicita revisión a otro integrante.
4. Atiende comentarios y vuelve a publicar los cambios si corresponde.
5. Fusiona el PR cuando cumpla los criterios de aceptación.

Repite el flujo con `feature/listado-estudiantes` y `docs/guia-proyecto`. Evita que dos integrantes editen simultáneamente las mismas líneas sin coordinar.

## Fase 6. Verificar historial y ramas
```bash
git branch
git branch -r
git log --oneline --graph --decorate --all
git status
```

## Fase 7. Ejecutar el programa y las pruebas
Desde la raíz:

```bash
python -m src.main
python -m unittest discover -s tests -v
```

## Comandos de ayuda
- `git status`: muestra el estado de archivos.
- `git diff`: muestra cambios no preparados.
- `git diff --staged`: muestra cambios preparados.
- `git log --oneline --graph --all`: historial compacto.
- `git show`: detalles del commit actual.
- `git switch nombre-rama`: cambia de rama.
- `git switch -c nombre-rama`: crea y cambia a una rama.

## Errores frecuentes
- **`git` no se reconoce:** instala Git y vuelve a abrir la terminal.
- **`python` no se reconoce:** verifica la instalación de Python; en Windows prueba `py --version`.
- **`remote origin already exists`:** revisa con `git remote -v`; si la URL es incorrecta, usa `git remote set-url origin URL_CORRECTA`.
- **`rejected` al publicar:** primero actualiza la rama con `git pull --rebase origin NOMBRE_RAMA` solo si entiendes el estado local y remoto; si hay dudas, detente y solicita revisión.
- **Conflicto al fusionar:** sigue `guia-conflictos.md`; no borres cambios sin revisar.
