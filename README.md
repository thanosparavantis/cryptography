# Cryptography

An experimental Python project that illustrates basic cryptography techniques. It features implementations of the Caesar and Vigenere cipher with their respective unit tests. The Caesar cipher is initialized with a key integer value ranging from 0 to 25. The Vigenere cipher is initialized with a key string value that is preferred to be a large sequence. Both ciphers have encrypt and decrypt methods that accept plain strings of text.

**Browse through related projects on thanosparavantis.com:**  
https://www.thanosparavantis.com/projects/cryptography

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
