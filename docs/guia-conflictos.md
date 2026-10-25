# Práctica controlada: resolución de conflictos Git

## Objetivo
Observar un conflicto cuando dos ramas cambian las mismas líneas de un archivo y resolverlo de forma consciente.

## Preparación
Haz esta práctica en un repositorio de prueba o asegúrate de tener el trabajo confirmado y respaldado. No la realices sobre cambios importantes sin commit.

```bash
git switch dev
git switch -c practica/conflicto-a
```

Crea `mensaje.txt` con este contenido y confirma el cambio:

```text
Mensaje del sistema académico:
Bienvenido al portal de estudiantes.
```

```bash
git add mensaje.txt
git commit -m "docs: agrega mensaje inicial"
git switch dev
git switch -c practica/conflicto-b
```

En `mensaje.txt`, cambia la segunda línea a:

```text
Bienvenido al sistema académico.
```

Confirma:
```bash
git add mensaje.txt
git commit -m "docs: actualiza mensaje del sistema"
```

Ahora vuelve a la rama A y cambia la misma segunda línea por:

```text
Bienvenido al portal de TecnoAula.
```

Confirma ese cambio también. Para que el ejercicio de conflicto sea válido, las dos ramas deben partir del mismo commit base y modificar la misma línea por separado.

## Provocar el conflicto
Fusiona primero una rama en `dev` y luego intenta integrar la otra. Si la historia está preparada como se indica, Git puede detener la fusión y mostrar un conflicto.

```bash
git status
```

Abre el archivo. Los marcadores se parecerán a:

```text
<<<<<<< HEAD
Bienvenido al portal de TecnoAula.
=======
Bienvenido al sistema académico.
>>>>>>> otra-rama
```

Los nombres y el orden exactos dependen de la rama actual y de la operación.

## Resolver
Edita el archivo para dejar una sola versión elegida, por ejemplo:

```text
Mensaje del sistema académico:
Bienvenido al portal de TecnoAula.
```

Elimina todos los marcadores de conflicto. Luego:

```bash
git diff
git add mensaje.txt
git status
git commit -m "fix: resuelve conflicto en mensaje"
```

Según el tipo de fusión, Git puede requerir completar el commit de fusión en vez de crear un commit ordinario. Sigue las indicaciones que muestre `git status`.

## Cancelar una fusión
Si la fusión está en curso y deseas volver al estado anterior:

```bash
git merge --abort
```

Este comando se usa para abortar una fusión en curso. Si hay cambios locales previos, el resultado puede requerir atención; por eso se recomienda comenzar con un árbol de trabajo limpio.

## Evidencia
Captura el conflicto visible, el archivo después de resolverlo, `git status` y el historial con `git log --oneline --graph --all`.
