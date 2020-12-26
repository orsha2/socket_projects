#client code:
import socket
import threading

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.16.96.160", 1234)) #enter server address & port number

def job():
      while True:
            s.send(input().encode())

t = threading.Thread(target=job)
t.start()

while True:
      try:
            print(s.recv(1024).decode())
      except:
            pass