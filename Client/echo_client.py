import socket

HOST = '172.20.77.68'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("Enter message (or 'quit'): ")
        if msg == 'quit':
            break
        s.sendall(msg.encode())
        data = s.recv(1024)
        print(f"[CLIENT] Echo: {data.decode()}")
