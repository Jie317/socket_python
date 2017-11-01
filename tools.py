def recv_one_line(sock, recv_buffer=4096, delim=b'\n'):
    buf = b''
    data = True
    while data:
        data = sock.recv(recv_buffer)
        buf += data

        print('Buf:', buf)
        if buf.find(delim):
            line = buf.split(b'\n')[0]
            return line

def recv_line(sock, recv_buffer=4096, delim=b'\n'):
    buf = b''
    data = True
    while data:
        data = sock.recv(recv_buffer)
        buf += data

        while buf.find(delim):
            line, buf = buf.split(b'\n', 1)
            yield line