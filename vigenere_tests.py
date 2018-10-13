from vigenere import VigenereCipher
import unittest

class TestVigenereCipher(unittest.TestCase):
    sample_message = 'the quick brown fox jumps over the lazy dog'
    sample_key = 'lemonade'

    def test_encryption_with_key(self):
        cipher = VigenereCipher(key=self.sample_key)
        result = cipher.encrypt(self.sample_message)
        expected = 'elq ehifo mvaka frb uyydf oyic xts yacc oss'
        self.assertEqual(result, expected)
    
    def test_decryption_with_key(self):
        cipher = VigenereCipher(key=self.sample_key)
        encrypted = cipher.encrypt(self.sample_message)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(self.sample_message, decrypted)

if __name__ == '__main__':
    unittest.main()
