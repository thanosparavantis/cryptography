import string


class VigenereCypher:
    char_to_int = dict(zip(string.ascii_lowercase, range(26)))
    int_to_char = dict(zip(range(26), string.ascii_lowercase))

    def __init__(self, key):
        self.key = key

    def repeat_token(self, key, length):
        return (key * length)[0:length]

    def encrypt(self, message):
        extended_key = self.repeat_token(self.key, len(message))
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
        extended_key = self.repeat_token(self.key, len(message))
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

if __name__ == "__main__":
    key = input("Enter a key: ")
    message = input("Enter a message: ")

    cypher = VigenereCypher(key)
    encrypted = cypher.encrypt(message)
    decrypted = cypher.decrypt(encrypted)

    print("Encrypted: {}".format(encrypted))
    print("Decrypted: {}".format(decrypted))
