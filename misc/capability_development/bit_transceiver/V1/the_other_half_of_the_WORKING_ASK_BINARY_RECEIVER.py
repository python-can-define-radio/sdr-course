import socket
import numpy as np
import pydash
import sys



connectToMe = ("127.0.0.1", 51234)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(connectToMe)

myData = []

# Do a bunch of times:
for whatever in range(1000):
    # Grab a piece of data.
    pieceAsBytes = s.recv(1)

    # Technically the type is "bytes".
    #  We can treat it as a collection of integers,
    #  (actually, just one integer).
    #  Extract that one item (which is at index 0).
    piece = pieceAsBytes[0]

    # If it's past an arbitrary threshold:
    if piece > 22:
        interpretation = 1
    else:
        interpretation = 0
    
    print(f"Data was {piece}. I interpreted as a {interpretation}")
    myData.append(interpretation)

s.close()


###### Now to interpret.
# To be a valid packet, I'm going to 
# require that it starts with 10101010.
# (This is similar to what real-life
#  Ethernet packets do).
#
# I'm going to also assume that before that point,
# it was only zeros (because the transmitter
# hadn't started).
# So I'm going to strip off any leading zeros,
# and then require that my special pattern comes next.

# Where is the first 1?
whereDataStarts = pydash.find_index(myData, lambda x: x == 1)

# Grab all the data from that point to the end
actualData = myData[whereDataStarts:]

print(actualData)

# If the first 8 are not 10101010, then discard.
if actualData[:8] != [1, 0, 1, 0, 1, 0, 1, 0]:
    print("Invalid data. Packet header not detected.")
    sys.exit()

# make it a single string
asOneStr = "".join(map(str, actualData))

f = open("receivedData.txt", "w")
f.write(asOneStr)
f.close()
