import unittest
from Endereco_Parser import formatadora

class TestFormatadora(unittest.TestCase):

    def test_formato_nacional(self):
        self.assertEqual(formatadora("Rua das Flores, 123"), {'Rua': 'Rua das Flores', 'Número': '123'})
        self.assertEqual(formatadora("Avenida Brasil 456"), {'Rua': 'Avenida Brasil', 'Número': '456'})
        self.assertEqual(formatadora("Praça da Sé, 789"), {'Rua': 'Praça da Sé', 'Número': '789'})
        self.assertEqual(formatadora("Rua São Paulo 101"), {'Rua': 'Rua São Paulo', 'Número': '101'})
        self.assertEqual(formatadora("Avenida das Nações, 2020"), {'Rua': 'Avenida das Nações', 'Número': '2020'})
    
    def test_formato_nacional_letra(self):
        self.assertEqual(formatadora("Rua das Flores 123A"), {'Rua': 'Rua das Flores', 'Número': '123A'})
        self.assertEqual(formatadora("Avenida Brasil 456B"), {'Rua': 'Avenida Brasil', 'Número': '456B'})
        self.assertEqual(formatadora("Praça da Sé, 789C"), {'Rua': 'Praça da Sé', 'Número': '789C'})
        self.assertEqual(formatadora("Rua São Paulo 101D"), {'Rua': 'Rua São Paulo', 'Número': '101D'})
        self.assertEqual(formatadora("Avenida das Nações 2020E"), {'Rua': 'Avenida das Nações', 'Número': '2020E'})
    
    def test_formato_internacional1(self):
        self.assertEqual(formatadora("123, Avenida de Roma d'Alba"), {'Rua': "Avenida de Roma d'Alba", 'Número': '123'})
        self.assertEqual(formatadora("456, Rua Paris"), {'Rua': 'Rua Paris', 'Número': '456'})
        self.assertEqual(formatadora("789, Boulevard de São Paulo"), {'Rua': 'Boulevard de São Paulo', 'Número': '789'})
        self.assertEqual(formatadora("101, Calle de Madrid"), {'Rua': 'Calle de Madrid', 'Número': '101'})
        self.assertEqual(formatadora("2020, Via de Lisboa"), {'Rua': 'Via de Lisboa', 'Número': '2020'})
    
    def test_formato_internacional2(self):
        self.assertEqual(formatadora("Avenida das Nações 2020, No 1"), {'Rua': 'Avenida das Nações 2020', 'Número': 'No 1'})
        self.assertEqual(formatadora("Rua das Flores 123, N° 2"), {'Rua': 'Rua das Flores 123', 'Número': 'N° 2'})
        self.assertEqual(formatadora("Avenida Brasil 456, Núm. 3"), {'Rua': 'Avenida Brasil 456', 'Número': 'Núm. 3'})
        self.assertEqual(formatadora("Praça da Sé 789, nr 4"), {'Rua': 'Praça da Sé 789', 'Número': 'nr 4'})
        self.assertEqual(formatadora("Rua São Paulo 101, N° 5"), {'Rua': 'Rua São Paulo 101', 'Número': 'N° 5'})

if __name__ == "__main__":
    unittest.main()
