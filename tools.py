s_addr = ('18.221.53.75', 8001)
# s_addr = ('localhost', 8001)

def recv_one_line(sock, recv_buffer=4096, delim=b'\n'):
    buf = b''
    data = True
    while data:
        data = sock.recv(recv_buffer)
        buf += data
        if delim in buf:
            line = buf.split(delim)[0]
            return line

def recv_line(sock, recv_buffer=4096, delim=b'\n'):
    buf = b''
    data = True
    while data:
        data = sock.recv(recv_buffer)
        buf += data

        while delim in buf:
            line, buf = buf.split(delim, 1)
            yield line

def append_n(b):
    return b+b'\n'