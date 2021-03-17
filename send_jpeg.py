import cv2
import sys
import time
import socket
import cv2
import numpy
res = [2100,1800,1500,1200,900,600,300]
quality=[100,80,60,40,20,10]
TCP_IP = '192.168.98.146'
TCP_PORT = 5003
cur_res = res[0]
iters = int(sys.argv[2])
# Load .png image
image = cv2.imread('test.jpg')
crop_image = image[0:cur_res-1,0:cur_res-1]
# Save .jpg image
cv2.imwrite('image.jpg', crop_image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))
frame= cv2.imread("image.jpg")

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),quality[int(sys.argv[1])]]
result, imgencode = cv2.imencode('.jpg', frame, encode_param)
data = numpy.array(imgencode)
stringData = data.tostring()
lent = len(stringData)
start_time = time.time()
for i in range(iters):
    start_time1 = time.time()
    sock.send( str(lent).ljust(16).encode('utf-8'))
    sock.send(stringData)
    while((time.time()-start_time1)<0.5):
        pass
end_time = time.time()
sock.close()
print("average :", (end_time-start_time)/iters)
