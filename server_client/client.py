
import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('172.16.96.160', 1234)) #enter server address & port number
print("client is connected")

soc.send(b"message from client")
print(soc.recv(1024))