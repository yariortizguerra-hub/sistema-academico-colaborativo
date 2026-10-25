import unittest
from src.estudiantes import registrar_estudiante, listar_estudiantes


class TestEstudiantes(unittest.TestCase):
    def setUp(self):
        self.estudiantes = []

    def test_registro_correcto(self):
        resultado = registrar_estudiante(
            self.estudiantes, "A001", "Ana Torres", "Computación e Informática"
        )
        self.assertEqual(resultado["codigo"], "A001")
        self.assertEqual(len(self.estudiantes), 1)

    def test_rechaza_codigo_vacio(self):
        with self.assertRaisesRegex(ValueError, "código"):
            registrar_estudiante(self.estudiantes, "", "Ana Torres", "Computación")

    def test_rechaza_nombre_vacio(self):
        with self.assertRaisesRegex(ValueError, "nombre"):
            registrar_estudiante(self.estudiantes, "A001", " ", "Computación")

    def test_rechaza_programa_vacio(self):
        with self.assertRaisesRegex(ValueError, "programa"):
            registrar_estudiante(self.estudiantes, "A001", "Ana Torres", "")

    def test_rechaza_codigo_duplicado(self):
        registrar_estudiante(self.estudiantes, "A001", "Ana Torres", "Computación")
        with self.assertRaisesRegex(ValueError, "Ya existe"):
            registrar_estudiante(self.estudiantes, "A001", "Luis Rojas", "Administración")

    def test_lista_ordenada_por_codigo(self):
        registrar_estudiante(self.estudiantes, "A002", "Luis Rojas", "Administración")
        registrar_estudiante(self.estudiantes, "A001", "Ana Torres", "Computación")
        resultado = listar_estudiantes(self.estudiantes)
        self.assertEqual([e["codigo"] for e in resultado], ["A001", "A002"])


if __name__ == "__main__":
    unittest.main()
