import socket

HOST = "127.0.0.1"
PORT = 5514

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"{HOST}:{PORT}")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        count = 0
        while count < 5:
            data = conn.recv(1024)
            if not data:
                break
            # conn.sendall(data)
            print( data )
            conn.sendall(data)
            count += 1

print("Server killed the connection!")
