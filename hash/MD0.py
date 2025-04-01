from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import socket
import json

def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def hash(data, sig):
    data = pad(data, 16)
    out = sig
    for i in range(0, len(data), 16):
        blk = data[i:i+16]
        out = bxor(AES.new(blk, AES.MODE_ECB).encrypt(out), out)
    return out

HOST = "socket.cryptohack.org"
PORT = 13388

def read_line(sock):
    buffer = b""
    while not buffer.endswith(b"\n"):
        buffer += sock.recv(1)
    return buffer.decode()

def receive_json(sock):
    line = read_line(sock)
    return json.loads(line[line.find('{'):])

def send_json(sock, payload):
    request = json.dumps(payload).encode()
    sock.sendall(request + b"\n")

with socket.create_connection((HOST, PORT)) as conn:
    print(read_line(conn))

    to_send = {"option": "sign", "message": bytes([0] * 15).hex()}
    send_json(conn, to_send)
    sig = receive_json(conn)["signature"]
    sig = hash(b'admin=True', bytes.fromhex(sig))

    to_send = {
        "option": "get_flag",
        "message": (bytes([0] * 15) + bytes([1]) + b'admin=True').hex(),
        "signature": sig.hex()
    }
    send_json(conn, to_send)
    print(receive_json(conn))