import socket
from threading import *
from tools import *
import select

class ModelClient(Thread):
    """docstring for ModelClient"""
    def __init__(self, arg):
        super(ModelClient, self).__init__()
        self.arg = arg
        

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
            if not sen:
                break
            self.m_sock.sendall(append_n(sen))
            cmds = recv_one_line(self.m_sock) # transfer
            if not cmds:
                break
            self.sock.sendall(append_n(cmds)) # not reached
            confirm = recv_one_line(self.sock)
            if not confirm:
                break
            self.m_sock.sendall(append_n(confirm))
        self.sock.close()
        print('App exited\n')

def get_model_sock():
    '''temporal implementation'''
    s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 8000
    s_sock.bind((host, port))
    s_sock.listen(5)
    
    print('Waiting for model client to connect...')
    m_sock, m_addr = s_sock.accept()
    print('Model client connected from', m_addr)
    return m_sock, s_sock

def check(m_sock):
    try:
        m_sock.sendall(b'')
        print('Model client already connected')
        return True
    except Exception as e:
        print('Model client not connected')
        return False   

def main():
    app_socket = None
    while 1:
        m_sock, s_sock = get_model_sock()  # get model client (tmp deployment)
        ss_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = socket.gethostname()
        port = 8001
        ss_sock.bind((host, port))
        ss_sock.listen(5)

        # deal with apps
        while 1:
            if not check(m_sock):
                break
            if not app_socket:
                print('Waiting for App to connect...')
                app_socket, app_addr = ss_sock.accept()
                print('App connected from', app_addr)
            if not check(m_sock):
                print('Model closed, app disconnected from', app_addr)
                break
            AppClient(app_socket, app_addr, m_sock).start()
            app_socket = None


if __name__ == '__main__':
    main()