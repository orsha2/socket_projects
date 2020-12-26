


from socket import *
from time import sleep

s = socket()
s.connect(('localhost',12345))  # '' == localhost

s.send('asdasd'.encode())

print s.recv(1024).decode()