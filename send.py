import cv2
import sys
import time
res = [2100,1800,1500,1200,900,600,300]

cur_res = res[int(sys.argv[1])]
iters = int(sys.argv[2])
# Load .png image
image = cv2.imread('test.png')
crop_image = image[0:cur_res-1,0:cur_res-1]
# Save .jpg image
start_time = time.time()
for i in range(iters):
    cv2.imwrite('image.jpg', crop_image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
end_time = time.time()

print "average :", (end_time-start_time)/iters
