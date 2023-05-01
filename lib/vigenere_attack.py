from .vigenere import Vigenere

class VigenereAttack:
    def __init__(self):
        self.vigenere = Vigenere()
        self.language_freqs = self.get_language_frequencies()

    def attack_key_size(self, msg):
        coincidences = self.get_coincidences_shift(msg)
        coincidences = sorted(coincidences, key = self.sort_tuple, reverse = True)
        return self.get_common_divisors(coincidences[:20])

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

    def get_coincidences_shift(self, msg):
        msg = "".join(msg.split())

        distribution_shift = []
        for shift in range(1, len(msg)):
            shifted_msg = self.shift_sentence(msg, shift)
            amount = self.amount_equal_letters(msg[shift:], shifted_msg[shift:])
            distribution_shift.append((shift, amount))

        return distribution_shift

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

    def amount_equal_letters(self, msg1, msg2):
        equal = 0
        if len(msg1) != len(msg2):
            return -1

        msg1 = "".join(msg1.split())
        msg2 = "".join(msg2.split())

        for index in range(len(msg1)):
            equal += int(msg1[index] == msg2[index])

        return equal

    def shift_sentence(self, msg, shift_amount):
        shifted_msg = ['*' for i in range(len(msg))]
        for index, letter in enumerate(msg):
            shifted_msg[(index + shift_amount)%len(msg)] = letter
        return ''.join(shifted_msg)

    def dot_prod(self, v1, v2):
        if len(v1) != len(v2):
            return -1

        N = len(v1)
        prod = 0
        for i in range(N):
            prod += v1[i] * v2[i]

        return prod

    def sort_tuple(self, element):
        return element[1]

    def get_common_divisors(self, best_frequences):
        letter_positions = [element[0] for element in best_frequences]
        max_value = max(letter_positions)
        divisors = {}

        for i in range(2, max_value):
            count = 0
            for element in letter_positions:
                if element % i == 0:
                    count += 1
            if count > 2:
                divisors[i] = count
        return divisors

