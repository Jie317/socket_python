import socket
import time
from tools import recv_one_line, s_addr

start = time.time()
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect(s_addr)
	print('Connected to', s.getpeername())

	for i in range(3):
		print('Sending spoken language')
		s.sendall('离散哈希算5.25.*^&%hm），为以用于.\n'.encode()+time.strftime('%m%S').encode())

		# recv = recv_one_line(s)
		received = s.recv(1024)
		print("\nReceived: {}".format(received.decode()))
		# confirm parsed cmds
		s.sendall(b'y\n')
finally:
	s.close()


print('Time elapse:', time.time()-start)