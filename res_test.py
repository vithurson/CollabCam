import cv2, sys, os
im_name = sys.argv[1]
im = cv2.imread(im_name)
output_format=input("1. raw image\n, 2. jpeg\n:")
if output_format=="2":
    quality= int(input("pls input jpeg quality:"))
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),quality]
    ext = ".jpg"
else:
    ext= ".ppm"
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),100]
print("input image dimensions are :",im.shape)
x_out = int(input("output image res_x:"))
y_out = int(input("output image res_y:"))
im2 = cv2.resize(im,(x_out,y_out))
cv2.imwrite("out"+ext,im2,encode_param)
print("output im size",os.path.getsize("out"+ext)/1000,"kB")
