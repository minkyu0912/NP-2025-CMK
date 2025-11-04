import socket

HOST = ''
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[SERVER] Echo Server listening on port {PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[SERVER] Received: {data.decode()}")
            conn.sendall(data)
