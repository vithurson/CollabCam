import cv2
import sys
import time
import socket
import cv2
import numpy
reduce_pix = 0
res_x = [1920,1600,1366,1280,1024]
res_y = [1080,900, 768,  720, 576]
#TCP_IP = 'localhost'
TCP_IP = '192.168.86.86'
TCP_PORT = 5002
iters = int(sys.argv[1])
xs = int(sys.argv[2])
ys = int(sys.argv[3])

cur_res_x = res_x[3]
cur_res_y = res_y[3]
# Load .png image
image = cv2.imread('test.jpg')
image = image[0:1080,0:1920]
crop_images=[]
secs =  xs*ys
xsize = int(cur_res_x/xs)
ysize = int(cur_res_y/ys)
image = cv2.resize(image, (cur_res_x,cur_res_y))
if(reduce_pix==0):
    qualities = [90,50,30,10]
    scales = []

for y in range(ys):
    for x in range(xs):
        ylow= ysize*y 
        yup= ysize*y + ysize
        xlow = xsize*x 
        xup = xsize*x + xsize
        scale = int(sys.argv[4+(y*xs+x)])
        if(reduce_pix):
            crop_images.append(cv2.resize(image[ylow:yup, xlow:xup],(int(xsize/scale),int(ysize/scale))))
        else:
            if(scale==0):
                crop_images.append(cv2.resize(image[ylow:yup, xlow:xup],(int(xsize),int(ysize))))
            else:
                crop_images.append(cv2.resize(image[ylow:yup, xlow:xup],(int(xsize/(scale+2)),int(ysize/(scale+2)))))
            scales.append(scale)
# Save .jpg image
im_no = 1
data_size = []
sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))
for crop_image in crop_images:
    quality = qualities[scales[im_no-1]]
    print("qual",quality,scales[im_no-1]+2)
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),quality]
    result, imgencode = cv2.imencode('.jpg', crop_image, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()
    lent = len(stringData)
    size = str(lent).ljust(16).encode('utf-8')
    data_size.append([size, stringData])
    im_no+=1
start_time = time.time()
for i in range(iters):
    for datas in data_size:
        sock.send(datas[0])
        sock.send(datas[1])
end_time = time.time()
sock.close()
print("average :", (end_time-start_time)/iters)
