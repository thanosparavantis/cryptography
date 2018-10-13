from caesar import CaesarCypher
import unittest

class TestCaesarCypher(unittest.TestCase):
    sample_message = 'the quick brown fox jumps over the lazy dog'

    def test_encryption_with_key_a(self):
        cypher = CaesarCypher(key=2)
        result = cypher.encrypt(self.sample_message)
        expected = 'vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi'
        self.assertEqual(result, expected)

    def test_encryption_with_key_b(self):
        cypher = CaesarCypher(key=20)
        result = cypher.encrypt(self.sample_message)
        expected = 'nby kocwe vliqh zir dogjm ipyl nby futs xia'
        self.assertEqual(result, expected)

    def test_encryption_with_zero_key(self):
        cypher = CaesarCypher(key=0)
        result = cypher.encrypt(self.sample_message)
        self.assertEqual(result, self.sample_message)

    def test_encryption_with_negative_key(self):
        cypher = CaesarCypher(key=-1)
        result = cypher.encrypt(self.sample_message)
        self.assertEqual(result, self.sample_message)

    def test_encryption_with_large_key(self):
        cypher = CaesarCypher(key=26)
        result = cypher.encrypt(self.sample_message)
        self.assertEqual(result, self.sample_message)

    def test_encryption_with_uppercase_message(self):
        cypher = CaesarCypher(key=10)
        result = cypher.encrypt(self.sample_message.upper())
        expected = 'dro aesmu lbygx pyh tewzc yfob dro vkji nyq'
        self.assertEqual(result, expected)

    def test_decryption_with_key_a(self):
        cypher = CaesarCypher(key=2)
        encrypted = cypher.encrypt(self.sample_message)
        decrypted = cypher.decrypt(encrypted)
        self.assertEqual(decrypted, self.sample_message)

    def test_decryption_with_key_b(self):
        cypher = CaesarCypher(key=20)
        encrypted = cypher.encrypt(self.sample_message)
        decrypted = cypher.decrypt(encrypted)
        self.assertEqual(decrypted, self.sample_message)

    def test_decryption_with_zero_key(self):
        cypher = CaesarCypher(key=0)
        encrypted = cypher.encrypt(self.sample_message)
        self.assertEqual(encrypted, self.sample_message)

if __name__ == '__main__':
    unittest.main()
