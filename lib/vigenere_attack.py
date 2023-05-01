from .vigenere import Vigenere

class VigenereAttack:
    def __init__(self, attacks_output = "attack_output.txt"):
        self.attacks_output = attacks_output
        self.vigenere = Vigenere()
        self.language_freqs = self.get_language_frequencies()

    def attack_key(self, cypher_txt, min_key_size = 2, max_key_size = 100, language = "en"):
        encrypt = self.vigenere.normalize_message(cypher_txt)

        guessed_keys = []
        for key_size in range(min_key_size, max_key_size + 1):
            groups = self.generate_groups(encrypt, key_size)
            founded_key = ""

            for group in groups:
                founded_key += self.get_best_probabilistic_letter(encrypt, group, language)

            guessed_keys.append(founded_key)

        return guessed_keys

    def get_best_probabilistic_letter(self, crypted_txt, group, language):
        freq = self.get_group_frequency(crypted_txt, group)

        max_prob = 0
        max_shift = 0

        for shift in range(26):
            shifted_frequency = self.shift_vector(freq, -shift)
            prob = self.dot_prod(shifted_frequency, self.language_freqs[language])
            if prob > max_prob:
                max_prob = prob
                max_shift = shift
        return chr(ord('a') + max_shift)

    def get_language_frequencies(self):
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

        english_freq_in_order = [
            english_freq_in_order[i] / 100.0
            for i in range(len(english_freq_in_order))
        ]

        portuguese_freq_in_order = [
            portuguese_freq_in_order[i] / 100.0
            for i in range(len(portuguese_freq_in_order))
        ]

        language_freq = {
            "en": english_freq_in_order,
            "pt-br": portuguese_freq_in_order
        }

        return language_freq

    def shift_vector(self, vec, shift_amount):
        N = len(vec)
        shifted_vec = [0 for i in range(N)]

        for i in range(N):
            shifted_vec[(i + shift_amount) % N] = vec[i]
        return shifted_vec

    def generate_groups(self, msg, guessed_key_size):
        groups = [{} for i in range(guessed_key_size)]
        msg = "".join(msg.split())

        for i in range(len(msg)):
            key_index = i % guessed_key_size

            if msg[i] not in groups[key_index]:
                groups[key_index][msg[i]] = 1
            else:
                groups[key_index][msg[i]] += 1

        return groups

    def get_group_frequency(self, msg, group):
        frequency = [0 for i in range(26)]

        for letter in group:
            frequency[ord(letter)-ord('a')] = group[letter] / len(msg)
        return frequency

    def dot_prod(self, v1, v2):
        if len(v1) != len(v2):
            return -1

        N = len(v1)
        prod = 0
        for i in range(N):
            prod += v1[i] * v2[i]

        return prod

