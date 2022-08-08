import socket
import numpy as np

HOST = '127.0.0.1'    
PORT = 9000           
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = np.frombuffer(s.recv(1024), dtype=np.complex64)
nonzero = data[data != 0]  # filter to just non-zero data

# If there's nothing left after filtering...
if len(nonzero) == 0:
    print("there was nothing left.")
else:
    print('Received', repr(nonzero))

s.close()








