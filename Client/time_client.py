import socket

HOST = '172.20.77.68' 
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print("[CLIENT] Server Time:", data.decode())
