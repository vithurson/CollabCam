import socket

UDP_IP = ""
UDP_PORT = 5003

sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(32) # buffer size is 1024 bytes
    print data
    lent = int(data)
    while(lent>65000):
        data, addr = sock.recvfrom(65000) # buffer size is 1024 bytes
        #print len(data)
        lent-=65000
    while(lent):
        data, addr = sock.recvfrom(lent) # buffer size is 1024 bytes
        #print len(data)
        lent = 0
    data, addr = sock.recvfrom(lent) # buffer size is 1024 bytes
    print("received message: %d" % lent)

