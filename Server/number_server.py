import socket
import time

HOST = ''
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[SERVER] Number Server listening on port {PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Connected by {addr}")
        n = 1
        while True:
            conn.sendall(str(n).encode())
            print(f"[SERVER] Sent: {n}")
            n += 1
            time.sleep(1)
