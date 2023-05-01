class Vigenere:
    def normalize_message(self, msg):
        # Looking the definition here:
        #   https://en.wikipedia.org/wiki/VigenC3A8re_cipher
        #   https://pt.wikipedia.org/wiki/Cifra_de_VigenC3A8re
        # We don't have any definition about accentuation, on this case, they will not be
        # considered.

        msg = msg.lower()

        accented_letters = {
            "a": ["á", "à", "â", "ã"],
            "e": ["é", "è", "ê", "ẽ"],
            "i": ["í", "ì"],
            "o": ["ó", "ò", "ô", "õ"],
            "u": ["ú", "ù", "û", "ũ"],
            "c": ["ç"]
        }

        for letter in accented_letters:
            for accented_letter in accented_letters[letter]:
                msg = msg.replace(accented_letter, letter)

        msg = msg.replace("'", " ").replace("\n", " ")
        correct_sentence = ""
        accepted_characters = "abcdefghijklmnopqrstuvwxyz "
        for letter in msg:
            if letter in accepted_characters:
                correct_sentence += letter

        return correct_sentence

    def encrypt(self, msg, key):
        encrypted_text = list(self.normalize_message(msg))
        key = self.normalize_message(key)
        index_key = 0

        for index, letter in enumerate(encrypted_text):
            if letter == " ":
                continue
            shift_amount = ord(key[index_key%len(key)])
            new_value = chr(ord('a') + (ord(letter)+shift_amount-2*ord('a')) % 26)
            encrypted_text[index] = new_value
            index_key += 1

        return ''.join(encrypted_text)

    def decrypt(self, msg, key):
        encrypted_text = list(msg)
        decrypted_text = ""
        index_key = 0

        for index, letter in enumerate(encrypted_text):
            if letter == " ":
                decrypted_text += " "
                continue
            shift_amount = ord(key[index_key%len(key)])

            diff_l1 = ord(letter) - ord('a')
            diff_l2 = shift_amount - ord('a')

            new_value = chr(ord('a') + ((diff_l1 - diff_l2)%26))

            decrypted_text += new_value
            index_key += 1

        return decrypted_text
