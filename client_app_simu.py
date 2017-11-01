import socket
import time
from tools import recv_one_line

s = socket.socket()
s.connect(('18.221.53.75', 8001))
print('Connected to', s.getpeername())


for i in range(3):

	s.sendall(b'spoken sentence from app\n')

	recv = recv_one_line(s).decode()
	print('Received:', recv)

	# confirm parsed cmds
	s.sendall(b'y\n')

	time.sleep(1)

# recv = recv_one_line(s).decode()
# print('Additional recv:', recv)
s.close()