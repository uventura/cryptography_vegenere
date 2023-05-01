import pathlib
import sys

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

import unittest
from lib.vigenere_attack import VigenereAttack
from lib.vigenere import Vigenere

class TestVigenereAttack(unittest.TestCase):
    def setUp(self):
        self.vigenere = Vigenere()
        self.vigenere_attack = VigenereAttack()

    def test_dot_prod_correct_vectors(self):
        vec_a = [4, 2, 5, 9, 76, 82]
        vec_b = [7, 15, 12, 67, 89, 55]

        prod = self.vigenere_attack.dot_prod(vec_a, vec_b)
        self.assertEqual(prod, 11995)

    def test_incorrect_dot_prod(self):
        vec_a = [1, 2]
        vec_b = [1]

        prod = self.vigenere_attack.dot_prod(vec_a, vec_b)
        self.assertEqual(prod, -1)

    def test_shift_vector_positive_value(self):
        vec = [1, 2, 3, 4, 5]
        shifted_vector = self.vigenere_attack.shift_vector(vec, 2)

        self.assertEqual(shifted_vector, [4, 5, 1, 2, 3])

    def test_shift_vector_negative_value(self):
        vec = [1, 2, 3, 4, 5]
        shifted_vector = self.vigenere_attack.shift_vector(vec, -2)

        self.assertEqual(shifted_vector, [3, 4, 5, 1, 2])

    def test_groups_generation(self):
        # Groups = {encrypted(mod k)}

        encrypted = "abcdaaa"
        groups = self.vigenere_attack.generate_groups(encrypted, 3)

        self.assertEqual(
            groups,
            [
                {'a': 2, 'd': 1},
                {'b': 1, 'a': 1},
                {'c': 1, 'a': 1}
            ]
        )

    def test_frequency_group(self):
        '''
            frequency(letter) = incidences(letter)/size(crypted_text)
        '''

        encrypted = "abcdaaa"
        groups = self.vigenere_attack.generate_groups(encrypted, 3)
        frequency_group = self.vigenere_attack.get_group_frequency(encrypted, groups[0])

        self.assertEqual(
            frequency_group,
            [
                0.2857142857142857, 0, 0,
                0.14285714285714285, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            ]
        )

if __name__ == "__main__":
    unittest.main()
