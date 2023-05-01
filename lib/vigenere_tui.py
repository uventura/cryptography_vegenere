from .vigenere import Vigenere
from .vigenere_attack import VigenereAttack

class VigenereTui:
    def __init__(self):
        self.vigenere = Vigenere()
        self.vigenere_attack = VigenereAttack()

    def run(self):
        while True:
            self.option_header()

            option = input("Option: ")
            while option not in "1234":
                print("!!! Wrong Answer !!!")
                option = input("Option: ")

            if option == "4":
                print("Bye :)")
                return
            if option == "1":
                self.encrypt()
            if option == "2":
                self.decrypt()
            if option == "3":
                self.attack()

    def option_header(self):
        print()
        print("-=-=-=| Select an Option |=-=-=-")
        print("(1) Encrypt")
        print("(2) Decrypt")
        print("(3) Attack")
        print("(4) Exit")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    def analyze_by_divisor(self, divisors):
        print("-=-=-=| Looking the 20 best shift coincidences |=-=-=-")
        for divisor in divisors:
            print(f"|\tKey Size = {divisor}, Coincidences = {divisors[divisor]}")
        print()

    def possible_decrypt_attacks(self, cypher_txt, min_key, max_key, language):
        possible_keys = self.vigenere_attack.attack_key(
            cypher_txt,
            min_key,
            max_key,
            language
        )

        print("-="*20)
        print("--------- Cypher Text ---------")
        print(cypher_txt)
        print("-="*20+"\n")

        for key in possible_keys:
            print(f">>>> Analysed Key = {key} <<<<")
            print(self.vigenere.decrypt(cypher_txt, key))
            print("-"*30)

    def encrypt(self):
        print("\n"+"="*5+"| Encrypt Mode |"+"="*5)
        txt = input("Text to be encrypted: ")
        key = input("Key: ")

        print("\n* Encrypted Code : "+self.vigenere.encrypt(txt, key))
        print("="*30+"\n")

    def decrypt(self):
        print("\n"+"="*5+"| Decrypt Mode |"+"="*5)
        txt = input("Text to be decrypted: ")
        key = input("Key: ")

        print("\n* Message : "+self.vigenere.decrypt(txt, key))
        print("="*30+"\n")

    def attack(self):
        print("\n"+"="*5+"| Attack Mode |"+"="*5)
        cypher_txt = self.vigenere.normalize_message(input("Cypher text: "))
        key_size_options = self.vigenere_attack.attack_key_size(cypher_txt)

        print()
        self.analyze_by_divisor(key_size_options)

        print()
        language = input("Select a language(en, pt-br): ")
        while not(language == "en" or language == "pt-br"):
            print("!!! Wrong Language !!!")
            language = input("Select a language(en, pt-br): ")

        print()
        min_key = int(self.input_digit_value("Select the minimum key size: "))
        max_key = int(self.input_digit_value("Select the maximum key size: "))

        self.possible_decrypt_attacks(cypher_txt, min_key, max_key, language)

    def input_digit_value(self, msg):
        value = input(msg)
        while not value.isdigit():
            print("!!! This is not a value !!!")
            value = input(msg)
        return value
