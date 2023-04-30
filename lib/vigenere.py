class Vigenere:
    def __init__(self, language = "en"):
        self.language = language
        self.language_frequences = self._get_frequences()

    def _get_frequences(self):
        english_freq_in_order = [
            8.167, 1.492, 2.782, 4.253, 12.702, 2.228,
            2.015, 6.094, 6.966, 0.153, 0.772, 4.025,
            2.406, 6.749, 7.507, 1.929, 0.095, 5.987,
            6.327, 9.056, 2.758, 0.978, 2.360, 0.150,
            1.974, 0.074,
        ]
        portuguese_freq_in_order = [
            14.63, 1.04, 3.88, 4.99, 12.57, 1.02,
            1.30, 1.28, 6.18, 0.40, 0.02, 2.78,
            4.74, 5.05, 10.73, 2.52, 1.20, 6.53,
            7.81, 4.34, 4.63, 1.67, 0.01, 0.21,
            0.01, 0.47,
        ]

        frequences = {
            "en": {},
            "pt-br": {}
        }

        for letter_index in range(26):
            english_value = english_freq_in_order[letter_index]
            frequences["en"][chr(ord("a") + letter_index)] = english_value

            portuguese_value = portuguese_freq_in_order[letter_index]
            frequences["pt-br"][chr(ord("a")+letter_index)] = portuguese_value

        return frequences

    def _normalize_message(self, msg):
        # Looking the definition here:
        #   https://en.wikipedia.org/wiki/VigenC3A8re_cipher
        #   https://pt.wikipedia.org/wiki/Cifra_de_VigenC3A8re
        # We don't have any definition about spaces, on this case, they will not be
        # considered, same thing for accentuation.

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

        pontuations = ":;.,<>+-=)(*&%$#@!^?|\\//[]\{\} "
        for pontuation in pontuations:
            msg = msg.replace(pontuation, "")

        return msg

    def encrypt(self, msg, key):
        encrypted_text = list(self._normalize_message(msg))

        for index, letter in enumerate(encrypted_text):
            shift_amount = ord(key[index%len(key)])
            new_value = chr(ord('a') + (ord(letter)+shift_amount-2*ord('a')) % 26)
            encrypted_text[index] = new_value

        return ''.join(encrypted_text)

    def decrypt(self, msg):
        pass
