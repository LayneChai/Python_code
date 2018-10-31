import socket

#client

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET 代表的是ipv4 SOCK_STREAM 代表的是TCP协议
s.connect(('www.sina.com',80)) #建立连接

s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
print(data)
s.close()
header,html = data.split(b'\r\n\r\n',1)
with open('a.txt','wb') as f:
    f.write(html
    
    
    
#server
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
#紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
