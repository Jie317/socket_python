import socket
from threading import *
from tools import *

class AppClient(Thread):
    def __init__(self, socket, address, m_sock):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.m_sock = m_sock
        
    def run(self):
        # parse spoken language (one sentence each time)
        while 1:
        # for i in range(5):
            sen = recv_one_line(self.sock)
            # tmp
            self.m_sock.sendall(sen)
            cmds = recv_one_line(self.m_sock) # transfer
            self.sock.sendall(cmds) # not reached
            confirm = recv_one_line(self.sock)
            self.m_sock.sendall(confirm)

def get_model_client():
    '''temporal implementation'''
    s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 8001
    s_sock.bind((host, port))
    s_sock.listen(1)
    m_sock, m_addr = s_sock.accept()
    print('Model client started:', m_addr) 
    return m_sock   


def main():
    m_sock = get_model_client()  # get model client (tmp deployment)

    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 8001
    ss.bind((host, port))
    ss.listen(5)
    print('Socket server started:', host, port)


    # deal with apps
    while 1:
        app_socket, app_addr = ss.accept()
        print('App connected from', app_addr)
        AppClient(app_socket, app_addr, m_sock).start()


if __name__ == '__main__':
    main()