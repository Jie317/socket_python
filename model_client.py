import socket
from tools import recv_one_line, s_addr

s = socket.socket()
s.connect(s_addr)
print('Connected')

while 1:
	# recv = recv_one_line(s).decode()
	recv = s.recv(1024)
	if not recv:
		break
	print('\nModel received:',recv.decode())
	# TODO: parse sentence
	s.sendall(b'parsed commands\n')

	confirm = s.recv(1024)
	if not confirm:
		break
	print("Received confirm: {}".format(confirm.decode()))
	s.sendall(b'got confirm, finished\n')

	if b'y' in confirm:
		pass # perform actions

s.close()