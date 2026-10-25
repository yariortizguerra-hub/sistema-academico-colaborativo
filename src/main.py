"""Punto de entrada de la aplicación académica de demostración."""
from src.estudiantes import registrar_estudiante, listar_estudiantes


def main():
    estudiantes = []
    print("=== TecnoAula: registro académico de demostración ===")
    while True:
        print("\n1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre completo: ")
            programa = input("Programa de estudios: ")
            try:
                estudiante = registrar_estudiante(
                    estudiantes, codigo, nombre, programa
                )
                print(f"Registrado: {estudiante['nombre']} ({estudiante['codigo']})")
            except ValueError as error:
                print(f"Error: {error}")
        elif opcion == "2":
            registros = listar_estudiantes(estudiantes)
            if not registros:
                print("Todavía no hay estudiantes registrados.")
            else:
                print("\nCódigo | Nombre | Programa")
                print("-" * 55)
                for e in registros:
                    print(f"{e['codigo']} | {e['nombre']} | {e['programa']}")
        elif opcion == "0":
            print("Fin de la demostración.")
            break
        else:
            print("Opción no válida. Seleccione 1, 2 o 0.")


if __name__ == "__main__":
    main()
