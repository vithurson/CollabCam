import cv2
import sys
import time
import socket
import cv2
import numpy
res = [2100,1800,1500,1200,900,600,300]

TCP_IP = '100.109.70.146'
TCP_PORT = 5003
cur_res = res[int(sys.argv[1])]
iters = int(sys.argv[2])
# Load .png image
image = cv2.imread('test.png')
crop_image = image[0:cur_res-1,0:cur_res-1]
# Save .jpg image
cv2.imwrite('image.jpg', crop_image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))
frame= cv2.imread("image.jpg")

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),100]
result, imgencode = cv2.imencode('.jpg', frame, encode_param)
data = numpy.array(imgencode)
stringData = data.tostring()
lent = len(stringData)
start_time = time.time()
for i in range(iters):
    sock.send( str(lent).ljust(16));
    sock.send(stringData);
end_time = time.time()
sock.close()
print "average :", (end_time-start_time)/iters
