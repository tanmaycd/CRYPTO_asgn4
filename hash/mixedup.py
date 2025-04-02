from Crypto.Util.number import long_to_bytes
from hashlib import sha256

from pwn import *
import json

# Just so we know the length of the flag.
FLAG = b"crypto{???????????????????????????????}"

r = remote("socket.cryptohack.org", 13402, level="error")
r.recvline()

# precompute sha256 table
sha256_table = {}
for i in range(0, 256):
    b = long_to_bytes(i, 1) * len(FLAG)
    sha256_table[sha256(b).hexdigest()] = True

bits = []
flag = ""
logger = log.progress("🏴")
for idx in range(0, len(FLAG)*8):
    r.sendline(json.dumps(
        {"option": "mix", "data": long_to_bytes(1 << idx, len(FLAG)).hex()}))
    resp = (json.loads(r.recvline().decode()))["mixed"]
    bit = 0 if resp in sha256_table else 1
    bits.append(bit)
    if len(bits) == 8:
        flag = long_to_bytes(
            int("".join(map(str, bits))[::-1], 2)).decode() + flag
        logger.status(flag)
        bits = []