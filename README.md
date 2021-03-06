# Cryptography

This is an experimental project that illustrates popular cryptography techniques. It contains implementations of algorithms, unit tests and several use case scenarios. The prototype source code is written in Python 3.6 and may have some issues or vulnerabilities.

## Caesar Cipher

Demonstration of a substitution cipher.

The Caesar Cipher is located in the `caesar.py` python file. In order to use it, you must choose a numerical number ranging from 0 to 25. With the `CaesarCipher` class you can encrypt, decrypt or bruteforce a message.

### References
- https://en.wikipedia.org/wiki/Caesar_cipher
- https://en.wikipedia.org/wiki/Substitution_cipher

## Vigenere Cipher

Demonstration of a polyalphabetic cipher.

The Vigenere Cipher is located in the `vigenere.py` python file. Before using it, you must choose a preferably large string as your key. You can utilize the `VigenereCipher` class to encrypt and decrypt messages.

### References
- https://en.wikipedia.org/wiki/Vigenère_cipher
- https://en.wikipedia.org/wiki/Polyalphabetic_cipher
