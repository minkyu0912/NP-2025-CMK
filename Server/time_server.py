import socket
import datetime

HOST = ''  
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[SERVER] Time Server listening on port {PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Connected by {addr}")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn.sendall(now.encode())
        print("[SERVER] Time sent to client.")
