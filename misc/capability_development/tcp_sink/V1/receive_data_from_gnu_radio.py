# Echo client program
import socket

# This should work too: 127.0.0.1
HOST = 'localhost'    # The remote host
PORT = 50009          # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall('Hello, world'.encode("utf-8"))
    # x = 5
    # s.sendall(f"Stuff: {x}".encode("utf-8"))
    # s.sendall('Hello, world'.encode("utf-8"))
    while True:
        # Grab a chunk of data
        data = s.recv(1024)
        dataAsInt = [int(piece) for piece in data]
        for x in dataAsInt:
            if x >= 1:
                print("Saw something")

    # print('Received:')
    # print(data)


