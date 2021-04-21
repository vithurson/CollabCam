import cv2
import sys
import time
import socket
import cv2 
import numpy
import os
from time import sleep

#TCP_IP = "localhost" 
UDP_PORT = 5003 
UDP_IP = '192.168.8.102'
rx=640
ry=480
shared_region = [0,33,50,66,100]
res_of_region = [360,240,160,96,70,5]

percentage = int(sys.argv[1])
resolution = int(sys.argv[2])
iters = int(sys.argv[3])


reg_size = res_of_region[resolution]
per      = shared_region[percentage]

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

print(per,reg_size)
start_time = time.time()
n=0
def send_chuncks(data,lent):
    global n
    n+=1
    i=-65000
    for i in range(0,lent - (lent%65000),65000):
        dt = data[i:i+65000]
        sock.sendto(dt,(UDP_IP, UDP_PORT))
        n+=1
    if((lent%65000) != 0):
        dt = data[i+65000:]
        sock.sendto(dt,(UDP_IP, UDP_PORT))
        n+=1
for j in range(iters):
    l1 = time.time()
    vid = cv2.VideoCapture(0) 
    start_time1 = time.time()
    image_set = []
    for i in range(120):
        ret, image = vid.read() 
        image = image[0:ry,0:rx]
        num_regions = ((percentage!=0) and (percentage!=4)) +1
        images=[]
        if(num_regions==2):
            im1_x_r = int(reg_size * per/100)
            im1_x_o = int(rx * per/100)
            im2_x  = rx- im1_x_o
            im1= cv2.resize(image[0:ry,0:im1_x_o],(im1_x_r,reg_size))
            im2=image[0:ry,im1_x_o:rx]
            images = [im1,im2]
            image_set.append(images)
        elif(per == 100):
            images = [cv2.resize(image,(reg_size,reg_size))]
            image_set.append(images)
        else:
            images = [image]
            image_set.append(images)
    print ("capture + process",time.time()-l1)
    vid.release()
    im_no=1
    #os.system("sudo ifconfig wlan0 up")
    l1 = time.time()
    for imaged in image_set:
        for im in imaged:
            result, imgencode = cv2.imencode('.jpg', im)
            data = numpy.array(imgencode)
            stringData = data.tostring()
            lent = len(stringData)
            size = str(lent).ljust(16).encode('utf-8')
            while(1):
                try:
                    sock.sendto(size,(UDP_IP, UDP_PORT))
                    break
                except:
                    pass
            send_chuncks(stringData,lent)
        #os.system("sudo ifconfig wlan0 down")
    print ("sending",time.time()-l1)
    delay = (start_time1-time.time())+9
    if delay <0:
        print("negative delay",delay)
        delay = 0
    time.sleep(delay)
os.system("sudo ifconfig wlan0 up")
end_time = time.time()
vid.release()
sock.close()
print("average :",(end_time-start_time)/iters)
