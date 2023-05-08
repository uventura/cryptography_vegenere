import pathlib
import sys

_parentdir = pathlib.Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(_parentdir))

from lib.vigenere_attack import VigenereAttack
from lib.vigenere import Vigenere

class ExampleModel:
    def __init__(self, cypher_txt, min_key = 2, max_key = 20, language = "en"):
        self.min_key = min_key
        self.max_key = max_key

        test_path = str(pathlib.Path(__file__).parent.resolve())

        self.vigenere = Vigenere()
        self.vigenere_attack = VigenereAttack()
        self.cypher_txt = self.vigenere.normalize_message(
            open(test_path + "/" + cypher_txt, "r", encoding="utf8").read()
        )
        self.language = language

    def run(self):
        possible_keys = self.vigenere_attack.attack_key(
            self.cypher_txt,
            self.min_key,
            self.max_key,
            self.language
        )

        print("-="*20)
        print("--------- Cypher Text ---------")
        print(self.cypher_txt)
        print("-="*20+"\n")

        for key in possible_keys:
            print(f">>>> Analysed Key = {key} <<<<")
            print(self.vigenere.decrypt(self.cypher_txt, key))
            print("-"*30)
