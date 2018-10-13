from caesar import CaesarCypher

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
