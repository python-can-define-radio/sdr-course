Create two files, `send_client.py` and `recv_server.py`. Copy the following into the respective files:


```python
## Copy this file into send_client.py

import socket

HOST = 'localhost'    # The remote host
PORT = 50008          # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Client is connected to server.")
s.sendall('Hello, world'.encode("UTF"))
print("Data sent.")
s.close()
```

```python
## Copy this file into recv_server.py

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## On the server, setting the host to "" means to 
## listen to connections from anyone. If you wanted to
## only listen to connections from this computer, you
## would put "localhost".
HOST = ""
PORT = 50008    # Arbitrary non-privileged port

s.bind((HOST, PORT))
s.listen(1)
print("Server ready for connections.")

conn, addr = s.accept()
print("Connected by", addr, "and they said...")
data = conn.recv(1024).decode("UTF")
print(data)

## Wait a bit so that the client can close first.
## (0.8 seconds is arbitrary.)
## This avoids the TCP requirement of waiting a 
## little while for the other party to finish talking.
## (If the client still isn't done, then we can close anyway.)
time.sleep(0.8)
conn.close()
s.close()
```

We're going to use these to simulate how SDRs handle data.

But first, make sure it runs:

1. In one terminal, run the server.
2. In another, run the client.

Then move on to the next page.