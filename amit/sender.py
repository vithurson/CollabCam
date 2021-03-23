import cv2
import sys
import time
import socket
import cv2 
import numpy
from time import sleep

#TCP_IP = "localhost" 
TCP_PORT = 5003
TCP_IP = '192.168.86.80'

shared_region = [0,33,50,66,100]
res_of_region = [360,160,96,70,5]

percentage = int(sys.argv[1])
resolution = int(sys.argv[2])
iters = int(sys.argv[3])


reg_size = res_of_region[resolution]
per      = shared_region[percentage]
vid = cv2.VideoCapture(0) 
vid.set(cv2.CAP_PROP_FRAME_WIDTH,512)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,512)
while(1):
    ret, image = vid.read() 
    sleep(1000)
    pass
sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))
print(per,reg_size)
start_time = time.time()
for j in range(iters):
    start_time1 = time.time()
    ret, image = vid.read() 
    num_regions = ((percentage!=0) and (percentage!=4)) +1
    
    images=[]
    if(num_regions==2):
        im1_x_r = int(reg_size * per/100)
        im1_x_o = int(512 * per/100)
        im2_x  = 512- im1_x_o
        im1= cv2.resize(image[0:512,0:im1_x_o],(im1_x_r,reg_size))
        im2=image[0:512,im1_x_o:512]
        images = [im1,im2]
    elif(per == 100):
        images = [cv2.resize(image,(reg_size,reg_size))]
    else:
        images = [image]
    im_no=1
    for im in images:
        result, imgencode = cv2.imencode('.ppm', im)
        data = numpy.array(imgencode)
        stringData = data.tostring()
        lent = len(stringData)
        size = str(lent).ljust(16).encode('utf-8')
        sock.send(size)
        sock.send(stringData)
    while((time.time()-start_time1)<0.1):
        pass
end_time = time.time()
vid.release()
sock.close()
print("average :", (end_time-start_time)/iters)
