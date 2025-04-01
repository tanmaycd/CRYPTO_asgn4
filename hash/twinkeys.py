from Crypto.Util.number import bytes_to_long, long_to_bytes
import socket
import json

SERVER_HOST = "socket.cryptohack.org"
SERVER_PORT = 13397

def read_from_socket(sock):
    data = b""
    while not data.endswith(b"\n"):
        data += sock.recv(1)
    return data.decode()

def parse_json_response(sock):
    response = read_from_socket(sock)
    return json.loads(response[response.find('{'):])

def send_payload(sock, data):
    serialized_data = json.dumps(data).encode()
    sock.sendall(serialized_data + b"\n")

key1 = "43727970746f4861636b205365637572652053616665300a08de6e639eb76baa3f782925580a654ad735580c928d0e6936fecd35ebd5ac2d6bc4608b6e55239ddee23a8ae2c6bdcdf57745c78aef60b46903e9b3eb4e128ad05ab9f459839ccd8374ca53aa802edd2cba35bf081d2b7ae96e70787c391cf11bcc226565219236"
key2 = "43727970746f4861636c205365637572652053616665300a08de6e639eb76baa3f782925580a654ad735580c928d0e6936fecd35ebd5ac2d6bc4608b6e55239ddee23a8ae2c6bdcdf57645c78aef60b46903e9b3eb4e128ad05ab9f459839ccd8374ca53aa802edd2cba35bf081d2b7ae96e70787c391cf11bcc226565219236"

with socket.create_connection((SERVER_HOST, SERVER_PORT)) as connection:
    print(read_from_socket(connection))
    payload = {"option": "insert_key", "key": key1}
    send_payload(connection, payload)
    print(parse_json_response(connection))
    payload = {"option": "insert_key", "key": key2}
    send_payload(connection, payload)
    print(parse_json_response(connection))
    payload = {"option": "unlock"}
    send_payload(connection, payload)
    print(parse_json_response(connection))