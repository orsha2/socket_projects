from socket import *


host = 'www.google.com'
port = 80
s = socket()
s.connect((host,port))

byte_send = s.send("GET / HTTP/1.1\r\nHost: "+host+"\r\n\r\n")

print ('-----------------')
msg_resv1 = s.recv(1024)
print msg_resv1

print ('-----------------')
msg_resv2 = s.recv(1024)
print (msg_resv2)

print ('-----------------')
msg_resv3 = s.recv(1024)
print (msg_resv3)
