import socketserver
import socket
import threading

class TCPHandler(socketserver.StreamRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.server.add_client(self.request)
        while 1:
            if len(self.server.clients) < 2:
                continue
            self.data = self.request.recv(1024).strip()
            if not self.data:
                break
            print( "{} wrote:".format(self.client_address[0]))
            print( self.data)
            # just send back the same data, but upper-cased
            self.server.send(self.request, self.data)

        self.server.remove_client(self.request)

    # def handle(self):
    #     # self.rfile is a file-like object created by the handler;
    #     # we can now use e.g. readline() instead of raw recv() calls
    #     self.data = self.rfile.readline().strip()
    #     print("{} wrote:".format(self.client_address[0]))
    #     print(self.data)
    #     # Likewise, self.wfile is a file-like object used to write back
    #     # to the client
    #     self.wfile.write(self.data.upper())

class Server(socketserver.ThreadingTCPServer):

    def __init__(self,*args,**kwargs):
        super(Server, self).__init__(*args,**kwargs)
        self.clients = []
        self.lock = threading.Lock()

    def add_client(self,c):
        with self.lock:
            print('Added client: ', c)
            self.clients.append(c)

    def remove_client(self,c):
        with self.lock:
            self.clients.remove(c)

    def send(self,sender,data):
        with self.lock:
            for c in self.clients:
                if c is not sender:
                    c.sendall(data)

s = Server((socket.gethostname(), 8001), TCPHandler)
s.serve_forever()