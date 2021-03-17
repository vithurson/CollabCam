#!/usr/bin/python
import socket
import cv2
import numpy

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = ''
TCP_PORT = 5003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
conn, addr = s.accept()
cur= 1
datas=[]
while(1):
    try:
        length = recvall(conn,16)
        stringData = recvall(conn, int(length))
        data = numpy.fromstring(stringData, dtype='uint8')
        datas.append(data)
    except:
        print("Breaking..",len(datas))
        break
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),100]
for i in range(len(datas)):
    data= datas[i]
    decimg=cv2.imdecode(data,1)
    cv2.imwrite('image'+str(i+1)+'.jpg', decimg, encode_param)
print("done")
s.close()
#data= datas[0]
#decimg=cv2.imdecode(,1)
#cv2.imshow('SERVER',decimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows() 
