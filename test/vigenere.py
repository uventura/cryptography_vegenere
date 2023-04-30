import pathlib
import sys

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

import unittest
from lib.vigenere import Vigenere

class TestVigenere(unittest.TestCase):
    def setUp(self):
        self.vigenere = Vigenere()

    def test_letter_encryption_a_e(self):
        encrypted_letter = self.vigenere.encrypt("a", "e")
        self.assertEqual(encrypted_letter, "e")

    def test_letter_encryption_l_r(self):
        encrypted_letter = self.vigenere.encrypt("l", "r")
        self.assertEqual(encrypted_letter, "c")

    def test_word_encryption(self):
        encrypted_word = self.vigenere.encrypt("hello, world!", "mykey")
        self.assertEqual(encrypted_word, "tcvpm imbpb")

    def test_letter_decryption_e_a(self):
        decrypted_letter = self.vigenere.decrypt("e", "a")
        self.assertEqual(decrypted_letter, "e")

    def test_letter_decryption_r_l(self):
        decrypted_letter = self.vigenere.decrypt("c", "r")
        self.assertEqual(decrypted_letter, "l")

    def test_word_decryption(self):
        decrypted_word = self.vigenere.decrypt("tcvpm imbpb", "mykey")
        self.assertEqual(decrypted_word, "hello world")

if __name__ == "__main__":
    unittest.main()

