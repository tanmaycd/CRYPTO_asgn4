#ron was wrong


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util import number
import gmpy
from itertools import combinations
from gmpy2 import mpz

grps = {'n':[],'c':[],'e':[]}
for i in range(1, 51):
    key = RSA.importKey(open(f"Ron_was_Wrong/keys_and_messages/{i}.pem", 'r').read())
    cipher = open(f"Ron_was_Wrong/keys_and_messages/{i}.ciphertext", 'r').read()
    cipher = number.bytes_to_long(bytes.fromhex(cipher))
    grps['n'].append(key.n)
    grps['c'].append(cipher)
    grps['e'].append(key.e)

N = 0
for i in range(len(grps['n'])):
    for j in range(len(grps['n'])):
        gcd = gmpy.gcd(grps['n'][i], grps['n'][j])
        if int(gcd) != mpz('1') and i!=j:
            N = int(gcd)
            ind = j
            
e = grps['e'][ind]
p = N
q = grps['n'][ind]//N
phi = (p-1)*(q-1)
d = number.inverse(e, phi)

key = RSA.construct((grps['n'][ind], e, d))
cipher = PKCS1_OAEP.new(key)
flag = number.long_to_bytes(grps['c'][ind])
flag = cipher.decrypt(flag)
print(flag)