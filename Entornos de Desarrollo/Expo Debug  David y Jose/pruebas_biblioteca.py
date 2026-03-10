import unittest
from libro import Libro
from biblioteca import Biblioteca

class TestLibro(unittest.TestCase):

    def setUp(self):
        # Creamos un libro de prueba con 3 copias y lo guardamos en 'self' para usarlo en los tests.
        self.libro = Libro("123-4", "Python 101", "Ana Pérez", 3)

    def test_prestar_disminuye_copias(self):
        self.libro.prestar()
        self.assertEqual(self.libro.copias, 2, "Al prestar, las copias deben disminuir en 1.")

    def test_devolver_aumenta_copias(self):
        self.libro.devolver()
        self.assertEqual(self.libro.copias, 4, "Al devolver, las copias deben aumentar en 1.")

    def test_disponible_con_copias(self):
        self.assertTrue(self.libro.disponible(), "El libro debe estar disponible si tiene copias > 0.")

    def test_no_disponible_sin_copias(self):
        self.libro.copias = 0
        self.assertFalse(self.libro.disponible(), "El libro no debe estar disponible si tiene 0 copias.")


class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.bib = Biblioteca()
        self.libro = Libro("123-4", "Python 101", "Ana Pérez", 1)
        self.bib.registrar_libro(self.libro)

    def test_registrar_libro(self):
        self.assertIn("123-4", self.bib.catalogo, "El libro debe estar en el catálogo tras registrarse.")

    def test_prestar_libro_exito(self):
        self.bib.prestar_libro("123-4")
        self.assertEqual(self.libro.copias, 0, "Las copias deben ser 0 tras prestar la única copia.")

    def test_prestar_libro_no_encontrado(self):
        with self.assertRaises(KeyError):
            self.bib.prestar_libro("isbn-falso")

    def test_prestar_libro_sin_copias(self):
        self.bib.prestar_libro("123-4")
        with self.assertRaises(RuntimeError):
            self.bib.prestar_libro("123-4")

    def test_devolver_libro_exito(self):
        self.bib.prestar_libro("123-4")
        self.bib.devolver_libro("123-4")
        self.assertEqual(self.libro.copias, 1, "Las copias deben restaurarse tras la devolución.")

    def test_devolver_libro_no_encontrado(self):
        with self.assertRaises(KeyError):
            self.bib.devolver_libro("isbn-falso")

if __name__ == "__main__":
    unittest.main()