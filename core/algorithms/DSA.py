import random


class DSACipher(object):
    def __init__(self):
        self.n = 823 * 953

    # Function to find gcd
    # of two numbers
    def euclid(self, m, n):
        if n == 0:
            return m
        else:
            r = m % n
            return self.euclid(n, r)

    # Program to find
    # Multiplicative inverse
    def exteuclid(self, a, b):
        r1 = a
        r2 = b
        s1 = int(1)
        s2 = int(0)
        t1 = int(0)
        t2 = int(1)

        while r2 > 0:
            q = r1 // r2
            r = r1 - q * r2
            r1 = r2
            r2 = r
            s = s1 - q * s2
            s1 = s2
            s2 = s
            t = t1 - q * t2
            t1 = t2
            t2 = t

        if t1 < 0:
            t1 = t1 % a

        return (r1, t1)

    def get_encrypt_key(self):
        # Enter two large prime
        # numbers p and q
        p = 823
        q = 953
        Pn = (p - 1) * (q - 1)

        # Generate encryption key
        # in range 1<e<Pn
        key = []

        for i in range(2, Pn):

            gcd = self.euclid(Pn, i)

            if gcd == 1:
                key.append(i)

        # Select an encryption key
        # from the above list
        return random.choice(key)

    # Obtain inverse of
    # encryption key in Z_Pn
    def get_decrypt_key(self, e):
        p = 823
        q = 953
        Pn = (p - 1) * (q - 1)
        r, d = self.exteuclid(Pn, e)
        if r == 1:
            d = int(d)
            return d
        else:
            print("Multiplicative inverse for\
                the given encryption key does not \
                exist. Choose a different encryption key ")

    def encrypt(self, M, key):
        # Signature is created by Alice
        return (M ** key) % self.n

    def decrypt(self, M, key):
        return (M ** key) % self.n
