import socket
from tools import recv_one_line, s_addr

s = socket.socket()
s.connect(s_addr)
print('Connected')

while 1:
	recv = recv_one_line(s).decode()
	print(recv)
	# TODO: parse sentence

	s.sendall(b'parsed commands\n')

	confirm = s.recv(1024)
	print("\nConfirm: {}".format(confirm.decode()))

	if b'y' in confirm:
		pass # perform actions