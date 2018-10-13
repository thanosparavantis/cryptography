from caesar import CaesarCipher

if __name__ == "__main__":
    key = int(input("Enter a key (0-25): "))
    message = input("Enter a message: ")
    message = message.lower()

    Cipher = CaesarCipher(key)
    encrypted = Cipher.encrypt(message)
    decrypted = Cipher.decrypt(encrypted)

    print("Encrypted: {}".format(encrypted))
    print("Decrypted: {}".format(decrypted))

    Cipher.bruteforce(encrypted)
