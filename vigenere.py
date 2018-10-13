import string


class VigenereCypher:
    char_to_int = dict(zip(string.ascii_lowercase, range(26)))
    int_to_char = dict(zip(range(26), string.ascii_lowercase))

    def __init__(self, key):
        self.key = key

    def repeat_token(self, key, message):
        extended_key = ""
        index = 0
        for char in message:
            if char.isalpha():
                if index >= len(self.key):
                    index = 0
                extended_key += self.key[index]
                index += 1
            else:
                extended_key += char

        return extended_key

    def encrypt(self, message):
        extended_key = self.repeat_token(self.key, message)
        print(extended_key)
        result = ""
        for i, char in enumerate(message):
            if char.isalpha():
                local_key = self.char_to_int[extended_key[i]]
                index = (self.char_to_int[char] + local_key) % 26
                result += self.int_to_char[index]
            else:
                result += char
        return result

    def decrypt(self, message):
        extended_key = self.repeat_token(self.key, message)
        result = ""
        for i, char in enumerate(message):
            if char.isalpha():
                local_key = self.char_to_int[extended_key[i]]
                index = (self.char_to_int[char] - local_key) % 26
                result += self.int_to_char[index]
            else:
                result += char
        return result

    def __str__(self):
        return self.key
