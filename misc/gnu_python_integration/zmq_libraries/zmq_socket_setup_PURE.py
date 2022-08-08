import zmq


def makeZMQPushSocket(push_address):
    push_context = zmq.Context()
    push_sock = push_context.socket(zmq.PUSH)

    # The High Water Mark (hwm) and the underlying OS buffer (SNDBUF)
    # are...
    #  - the max number of messages in zmq's queue
    #  - the max size of the underlying OS buffer
    # respectively.
    # I set them to avoid maxing out the RAM.
    # The values came from trial and error; feel free to modify.
    push_sock.set(zmq.SNDHWM, 1000)
    push_sock.set(zmq.SNDBUF, 300000)

    rc = push_sock.bind(push_address)
    
    # This line is from the example code,
    # I think it's just there to make sure the bind worked.
    assert rc == None  

    return push_sock