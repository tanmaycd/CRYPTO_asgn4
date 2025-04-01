from Crypto.Util.number import bytes_to_long, long_to_bytes
import socket
import json

HOST = "socket.cryptohack.org"
PORT = 13389

def read_socket(sock):
    buffer = b""
    while not buffer.endswith(b"\n"):
        buffer += sock.recv(1)
    return buffer.decode()

def parse_json(sock):
    data = read_socket(sock)
    return json.loads(data[data.find('{'):])

def send_data(sock, payload):
    sock.sendall(json.dumps(payload).encode() + b"\n")

with socket.create_connection((HOST, PORT)) as conn:
    print(read_socket(conn))
    doc1 = {
        "document": "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
    }
    send_data(conn, doc1)
    print(read_socket(conn))
    doc2 = {
        "document": "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"
    }
    send_data(conn, doc2)
    print(read_socket(conn))