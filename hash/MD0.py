from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import socket
import json

def xor_bytes(byte_seq1, byte_seq2):
    return bytes(a ^ b for a, b in zip(byte_seq1, byte_seq2))

def custom_hash(data, signature):
    padded_data = pad(data, 16)
    result = signature
    for i in range(0, len(padded_data), 16):
        block = padded_data[i:i+16]
        result = xor_bytes(AES.new(block, AES.MODE_ECB).encrypt(result), result)
    return result

SERVER_HOST = "socket.cryptohack.org"
SERVER_PORT = 13388

def read_from_socket(sock):
    data = b""
    while not data.endswith(b"\n"):
        data += sock.recv(1)
    return data.decode()

def parse_json_response(sock):
    response = read_from_socket(sock)
    return json.loads(response[response.find('{'):])

def send_payload(sock, payload):
    serialized_data = json.dumps(payload).encode()
    sock.sendall(serialized_data + b"\n")

with socket.create_connection((SERVER_HOST, SERVER_PORT)) as connection:
    print(read_from_socket(connection))

    payload = {"option": "sign", "message": bytes([0] * 15).hex()}
    send_payload(connection, payload)
    signature = parse_json_response(connection)["signature"]
    forged_signature = custom_hash(b'admin=True', bytes.fromhex(signature))

    payload = {
        "option": "get_flag",
        "message": (bytes([0] * 15) + bytes([1]) + b'admin=True').hex(),
        "signature": forged_signature.hex()
    }
    send_payload(connection, payload)
    print(parse_json_response(connection))