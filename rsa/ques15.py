#FAST PRIMES 

#!/usr/bin/env python3

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, inverse
from Crypto.Util import number

c = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28

key = RSA.importKey(open("Downloads/key.pem", "rb").read())

n = key.n
e = key.e

f = FactorDB(n)
f.connect()
p = int(f.get_factor_from_api()[0][0])
q = int(f.get_factor_from_api()[1][0])

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
r = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28
c = number.long_to_bytes(r)
m = cipher.decrypt(c)
print(m)