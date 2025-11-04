import socket

HOST = '172.20.77.68'
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(f"[CLIENT] Received number: {data.decode()}")

