from Crypto.Util.number import bytes_to_long, long_to_bytes
import socket
import json

HOST = "socket.cryptohack.org"
PORT = 13405

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
    to_send = {"m1": m1.hex(), "m2": m2.hex()}
    send_json(conn, to_send)
    print(read_line(conn))
    print(receive_json(conn))