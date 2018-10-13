from vigenere import VigenereCipher

if __name__ == "__main__":
    key = input("Enter a key: ")
    message = input("Enter a message: ")

    Cipher = VigenereCipher(key)
    encrypted = Cipher.encrypt(message)
    decrypted = Cipher.decrypt(encrypted)

    print("Encrypted: {}".format(encrypted))
    print("Decrypted: {}".format(decrypted))
