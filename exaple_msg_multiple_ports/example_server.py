

from socket import *

s = socket()
s.bind(('',12345))
s.listen(10)
print ('server is on')

new_socket_tuple = s.accept()
print ('client is connected')

new_socket = new_socket_tuple[0]
print (new_socket.recv(1024).decode())

new_socket.send('hi from server'.encode())