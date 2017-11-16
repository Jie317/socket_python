import socket
from tools import recv_one_line, s_addr

def parseText(txt):
	print('\tParsing cmds...')
	return 'move(5,3)\n'
def performCmds(cmds):
	print('\tPerforming cmds:', cmds)
	return 'Finished\n'

s = socket.socket()
s.connect(s_addr)
print('Connected')

status = ''

while 1:
	# recv = recv_one_line(s).decode()
	recv = s.recv(1024).decode()
	if not recv:
		break

	if recv.startswith('Text'):
		recv_text = recv[4:]
		print('\nText received:', recv_text)
		cmds = parseText(recv_text)
		status = 'Confirm'
		s.sendall(cmds.encode())

	if recv.startswith('Confirm'):
		if status == 'Confirm':
			status = ''
			recv_confirm = recv[7:]
			print('Confirm received:', recv_confirm)
			if recv_confirm == 'Ok':
				result = performCmds(cmds)
				s.sendall(result.encode())
			else:
				s.sendall(b'Cancelled\n')
		else:
			s.sendall(b'\n')

s.close()