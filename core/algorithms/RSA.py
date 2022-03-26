import random
import string


class RSACipher(object):

    def get_N(self, p, q):
        return p * q

    def get_phi_of_n(self, p, q):
        return (p - 1) * (q - 1)

    def get_gcd(self, x, y):
        while (y):
            x, y = y, x % y
        return x

    def get_encryption_key(self, n, phi_of_n):
        lst = [i for i in range(1, n + 1)]
        e_list = []
        for i in lst:
            if (1 < i) and (i < phi_of_n):
                gcd = self.get_gcd(i, n)
                gcd_phi = self.get_gcd(i, phi_of_n)
                if (gcd == 1) and (gcd_phi == 1):
                    e_list.append(i)
        if len(e_list) == 1:
            return e_list[0]
        else:
            return e_list[random.randint(1, len(e_list) - 1)]

    def get_decryption_key(self, e, phi_of_n):
        try:
            d_list = []
            for i in range(e * 25):
                if (e * i) % phi_of_n == 1:
                    d_list.append(i)
            return d_list[random.randint(1, len(d_list) - 1)]
        except:
            self.get_encryption_key(e, phi_of_n)

    def text_to_digits(self, PT):
        pool = string.ascii_letters + string.punctuation + " "
        M = []
        for i in PT:
            M.append(pool.index(i))
        return M

    def digits_to_text(self, DT):
        pool = string.ascii_letters + string.punctuation + " "
        msg = ''
        for i in DT:
            msg += pool[i]
        return msg

    def encrypt(self, M, public_key):
        return [(i ** public_key[0]) % public_key[1] for i in M]

    def decrypt(self, CT, private_key):
        return [((i ** private_key[0]) % private_key[1]) for i in CT]


