import string


class CaesarCypher:
    char_to_int = dict(zip(string.ascii_lowercase, range(26)))
    int_to_char = dict(zip(range(26), string.ascii_lowercase))

    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        result = ""
        for char in message:
            if char.isalpha():
                index = (self.char_to_int[char] + self.key) % 26
                result += self.int_to_char[index]
            else:
                result += char
        return result

    def decrypt(self, message):
        result = ""
        for char in message:
            if char.isalpha():
                index = (self.char_to_int[char] - self.key) % 26
                result += self.int_to_char[index]
            else:
                result += char
        return result

    def bruteforce(self, message):
        for brutekey in range(26):
            attempt = ""
            for char in message:
                if char.isalpha():
                    index = (self.char_to_int[char] - brutekey) % 26
                    attempt += self.int_to_char[index]
                else:
                    attempt += char
            print("{} (key {})".format(attempt, brutekey))

    def __str__(self):
        return self.key

if __name__ == "__main__":
    key = int(input("Enter a key (0-25): "))
    message = input("Enter a message: ")
    message = message.lower()

    cypher = CaesarCypher(key)
    encrypted = cypher.encrypt(message)
    decrypted = cypher.decrypt(encrypted)

    print("Encrypted: {}".format(encrypted))
    print("Decrypted: {}".format(decrypted))

    cypher.bruteforce(encrypted)