import socket
from tools import recv_one_line

s = socket.socket()
s.connect(('18.221.53.75', 8001))

while 1:
	recv = recv_one_line(s).decode()
	print('Received:', recv)
	# TODO parse sentence

	s.sendall(b'parsed commands\n')

	get_confirm = recv_one_line(s)

	if b'y' in get_confirm:
		pass # perform actions
	print('Finished\n')
