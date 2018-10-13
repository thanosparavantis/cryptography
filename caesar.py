import string


class CaesarCipher:
    char_to_int = dict(zip(string.ascii_lowercase, range(26)))
    int_to_char = dict(zip(range(26), string.ascii_lowercase))

    def __init__(self, key):
        self.key = self.normalize_key(key)

    def encrypt(self, message):
        message = self.normalize_message(message)
        result = ""
        for char in message:
            if char.isalpha():
                index = (self.char_to_int[char] + self.key) % 26
                result += self.int_to_char[index]
            else:
                result += char
        return result

    def decrypt(self, message):
        message = self.normalize_message(message)
        result = ""
        for char in message:
            if char.isalpha():
                index = (self.char_to_int[char] - self.key) % 26
                result += self.int_to_char[index]
            else:
                result += char
        return result

    def bruteforce(self, message):
        message = self.normalize_message(message)
        for brutekey in range(26):
            attempt = ""
            for char in message:
                if char.isalpha():
                    index = (self.char_to_int[char] - brutekey) % 26
                    attempt += self.int_to_char[index]
                else:
                    attempt += char
            print("{} (key {})".format(attempt, brutekey))

    def normalize_key(self, key):
        return 0 if key < 0 or key > 25 else key

    def normalize_message(self, message):
        return message.lower().strip()

    def __str__(self):
        return self.key
