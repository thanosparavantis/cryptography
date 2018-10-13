from caesar import CaesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    sample_message = 'the quick brown fox jumps over the lazy dog'

    def test_encryption_with_key_a(self):
        Cipher = CaesarCipher(key=2)
        result = Cipher.encrypt(self.sample_message)
        expected = 'vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi'
        self.assertEqual(result, expected)

    def test_encryption_with_key_b(self):
        Cipher = CaesarCipher(key=20)
        result = Cipher.encrypt(self.sample_message)
        expected = 'nby kocwe vliqh zir dogjm ipyl nby futs xia'
        self.assertEqual(result, expected)

    def test_encryption_with_zero_key(self):
        Cipher = CaesarCipher(key=0)
        result = Cipher.encrypt(self.sample_message)
        self.assertEqual(result, self.sample_message)

    def test_encryption_with_negative_key(self):
        Cipher = CaesarCipher(key=-1)
        result = Cipher.encrypt(self.sample_message)
        self.assertEqual(result, self.sample_message)

    def test_encryption_with_large_key(self):
        Cipher = CaesarCipher(key=26)
        result = Cipher.encrypt(self.sample_message)
        self.assertEqual(result, self.sample_message)

    def test_encryption_with_uppercase_message(self):
        Cipher = CaesarCipher(key=10)
        result = Cipher.encrypt(self.sample_message.upper())
        expected = 'dro aesmu lbygx pyh tewzc yfob dro vkji nyq'
        self.assertEqual(result, expected)

    def test_decryption_with_key_a(self):
        Cipher = CaesarCipher(key=2)
        encrypted = Cipher.encrypt(self.sample_message)
        decrypted = Cipher.decrypt(encrypted)
        self.assertEqual(decrypted, self.sample_message)

    def test_decryption_with_key_b(self):
        Cipher = CaesarCipher(key=20)
        encrypted = Cipher.encrypt(self.sample_message)
        decrypted = Cipher.decrypt(encrypted)
        self.assertEqual(decrypted, self.sample_message)

    def test_decryption_with_zero_key(self):
        Cipher = CaesarCipher(key=0)
        encrypted = Cipher.encrypt(self.sample_message)
        self.assertEqual(encrypted, self.sample_message)

if __name__ == '__main__':
    unittest.main()
