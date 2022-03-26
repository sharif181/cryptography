from base64 import b64encode, b64decode
import hashlib
from Crypto.Cipher import DES


class DESCipher(object):
    def __init__(self, secret):
        self.secret = secret
        self.key = self.secret + '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
        self.m = hashlib.md5(self.key.encode("utf-8"))
        self.key = self.m.digest()

    def encrypt(self, plain_text):
        (dk, iv) = (self.key[:8], self.key[8:])
        crypter = DES.new(dk, DES.MODE_CBC, iv)
        plain_text += '\x00' * (8 - len(plain_text) % 8)
        ciphertext = crypter.encrypt(plain_text.encode("utf-8"))
        encode_string = b64encode(ciphertext)
        return encode_string.decode("utf-8")

    def decrypt(self, encrypted_string):
        (dk, iv) = (self.key[:8], self.key[8:])
        crypter = DES.new(dk, DES.MODE_CBC, iv)
        encrypted_string = b64decode(encrypted_string)
        decrypted_string = crypter.decrypt(encrypted_string)
        return decrypted_string.decode('utf-8')