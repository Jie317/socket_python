import socket
from tools import recv_one_line, s_addr

s = socket.socket()
s.connect(s_addr)
print('Connected')

while 1:
	# recv = recv_one_line(s).decode()
	recv = s.recv(1024)
	print('\nModel received:',recv)
	# TODO: parse sentence
	s.sendall(b'parsed commands')

	confirm = s.recv(1024)
	print("rReceived confirm: {}".format(confirm.decode()))
	s.sendall(b'got confirm, finished')

	if b'y' in confirm:
		pass # perform actions