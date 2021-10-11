import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('I am connecting the server!')
for xx in ['aBch'，'f服务d','h7Tq','.']:
s.sendto(xx,('192.168.3.13',8088))
str1,addr=s.recvfrom(1024)
str2=str(str1,encoding='utf-8')
print(s.recv(1024).decode('utf-8'))
s.close()
