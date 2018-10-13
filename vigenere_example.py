from vigenere import VigenereCypher

if __name__ == "__main__":
    key = input("Enter a key: ")
    message = input("Enter a message: ")

    cypher = VigenereCypher(key)
    encrypted = cypher.encrypt(message)
    decrypted = cypher.decrypt(encrypted)

    print("Encrypted: {}".format(encrypted))
    print("Decrypted: {}".format(decrypted))
