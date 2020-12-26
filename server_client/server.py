
import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind(('172.16.96.160', 1234)) #enter server address & port number
soc.listen(10)
print("server is wating....")
(client, address) = soc.accept()
print(client.recv(1024))
client.send(b"message from server")