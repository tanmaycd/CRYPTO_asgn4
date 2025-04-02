import socket
import json

HOST = "socket.cryptohack.org"
PORT = 13393

def read_line(sock):
    buffer = b""
    while not buffer.endswith(b"\n"):
        buffer += sock.recv(1)
    return buffer.decode()

def send_json(sock, payload):
    serialized_data = json.dumps(payload).encode()
    sock.sendall(serialized_data + b"\n")

def receive_json(sock):
    response = read_line(sock)
    return json.loads(response)

with socket.create_connection((HOST, PORT)) as conn:
    print(read_line(conn))
    payload = {
        "data": "76777776666666666666667767767676",
        "option": "hash"
    }
    send_json(conn, payload)
    response = receive_json(conn)
    print(response)