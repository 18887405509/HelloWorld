import socket
s= socket.socket(socket.AFINET socket.SOCK_DGRAM)
s.bind(('192.168.3.13'，8088)
print('Bind UDP on 8088...')
while True:
str1,addr=recvfrom(1024)
str2=str(str1,encoding='utf- 8')
print('I received a string is:',str2)
str3=str2.upper()
s.sendto(str3.encode('utf-8'),addr)

