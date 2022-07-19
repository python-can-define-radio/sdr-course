import zmq
import numpy as np
import time
from matplotlib import pyplot as plt

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:50252")

# while True:
msg = socket.recv()
for idx, x in enumerate(msg):
    if x:
        print(idx, x)
import pdb; pdb.set_trace()
data = np.frombuffer(msg, dtype=np.complex64, count=-1) # make sure to use correct data type (complex64 or float32); '-1' means read all data in the buffer
print(data)
plt.plot(data.real)
plt.show()
