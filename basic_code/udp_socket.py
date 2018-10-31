import socket

#client
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('127.0.0.1',9999)
while True:
    s.sendto(b'client',('127.0.0.1',9999))
    print(s.recvfrom(1024))
    
    
#socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))

while True:
    data,addr = s.recvfrom(1024)
    print(type(data),data)
    s.sendto(b'server',addr)

