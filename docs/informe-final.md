# Informe final de ejecución

## 1. Datos generales
- Institución: ______________________
- Programa de estudios: ______________________
- Unidad didáctica: ______________________
- Docente: ______________________
- Integrantes: 1) ______________  2) ______________  3) ______________
- Fecha: ____ / ____ / 2026

## 2. Objetivo
Practicar un flujo de trabajo colaborativo con Git y GitHub sobre un prototipo académico de registro de estudiantes (TecnoAula Perú S.A.C.). Se buscó aprender a organizar el trabajo con repositorio, ramas, commits, Issues, Pull Requests con revisión, resolución de conflictos, pruebas automatizadas y documentación, de modo que tres personas puedan modificar el mismo proyecto sin pisarse el trabajo.

## 3. Actividades realizadas
1. **Entorno:** se verificó la instalación de Git y Python y se configuró el nombre y correo de usuario en Git.
2. **Repositorio:** se creó el repositorio `sistema-academico-colaborativo` en GitHub y se publicó la rama `main` con la estructura inicial (`src`, `tests`, `docs`, `.github`, `.gitignore`, `README.md`).
3. **Ramas:** se creó la rama de integración `dev` y las ramas de trabajo `feature/registro-estudiantes`, `feature/listado-estudiantes` y `docs/guia-proyecto`.
4. **Issues:** se registraron cinco Issues (estructura inicial, registro, listado, pruebas y documentación), cada uno con título, descripción, responsable y etiquetas.
5. **Commits:** se usó la convención `feat:`, `fix:`, `docs:`, `test:` y `refactor:` para mantener un historial claro.
6. **Pull Requests:** cada rama se envió a `dev` mediante un Pull Request, revisado por otro integrante antes de fusionarse.
7. **Conflicto:** se provocó un conflicto de forma controlada modificando la misma línea de `mensaje.txt` en dos ramas (`practica/conflicto-a` y `practica/conflicto-b`), y se resolvió eligiendo una versión y eliminando los marcadores.
8. **Pruebas:** se ejecutaron las pruebas con `python -m unittest discover -s tests -v` (casos P01 a P06 del plan de pruebas).
9. **Integración final:** con `dev` estable, se fusionó a `main`.

> Edita este apartado si hicieron algo distinto. Describan solo lo que realmente hicieron.

## 4. Resultados verificados
(Completa con los datos reales de TU ejecución.)
- URL del repositorio: ______________________
- Número de ramas: ____
- Número de commits relevantes: ____
- Issues completados: ____ de 5
- Pull Requests fusionados: ____
- Resultado de las pruebas: ____ pruebas ejecutadas, estado: ______ (esperado: OK)
- Conflicto resuelto: Sí / No

## 5. Dificultades y soluciones
(Escribe errores REALES que tuvieron. Ejemplos de cosas que suelen pasar: `git` o `python` no se reconocía en la terminal, `remote origin already exists`, un `push` rechazado, o el primer conflicto que dio miedo. Anota qué pasó y cómo lo resolvieron.)

| Dificultad | Cómo se solucionó |
|---|---|
| | |
| | |

## 6. Aprendizajes
- **Integrante 1:** ______________________
- **Integrante 2:** ______________________
- **Integrante 3:** ______________________

## 7. Mejoras futuras
- Guardar los estudiantes en una base de datos para que no se pierdan al cerrar el programa.
- Crear una interfaz gráfica o web en lugar de la consola.
- Agregar inicio de sesión y roles de usuario.
- Añadir más validaciones (formato del código, nombres duplicados) y más pruebas automatizadas.
- Automatizar las pruebas en cada Pull Request con GitHub Actions.

## 8. Conclusiones
(Redáctalas con base en lo que viviste. Una guía: el trabajo con ramas y Pull Requests permite que varias personas avancen a la vez y que otra persona revise antes de integrar; los conflictos son normales y se resuelven revisando con calma; las pruebas automatizadas confirman que el programa sigue funcionando después de cada cambio.)
