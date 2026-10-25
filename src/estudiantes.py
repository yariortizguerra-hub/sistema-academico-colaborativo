"""Funciones básicas para registrar y listar estudiantes."""

def registrar_estudiante(estudiantes, codigo, nombre, programa):
    """Valida y agrega un estudiante a la lista recibida.

    Devuelve el diccionario registrado. Lanza ValueError si los datos no son válidos.
    """
    codigo = str(codigo).strip()
    nombre = str(nombre).strip()
    programa = str(programa).strip()

    if not codigo:
        raise ValueError("El código del estudiante es obligatorio.")
    if not nombre:
        raise ValueError("El nombre del estudiante es obligatorio.")
    if not programa:
        raise ValueError("El programa de estudios es obligatorio.")
    if any(e["codigo"] == codigo for e in estudiantes):
        raise ValueError(f"Ya existe un estudiante con código {codigo}.")

    estudiante = {
        "codigo": codigo,
        "nombre": nombre,
        "programa": programa,
    }
    estudiantes.append(estudiante)
    return estudiante


def listar_estudiantes(estudiantes):
    """Devuelve una copia ordenada de los estudiantes por código."""
    return sorted((dict(e) for e in estudiantes), key=lambda e: e["codigo"])
