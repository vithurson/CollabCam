import cv2
import numpy as np
import sys
import time
jpeg="y" in input("do you want jpeg compression (yes/no):")
if jpeg:
    print("jpeg enabled")
try:
    file_name = sys.argv[1]
    num_regions_x= int(sys.argv[2])
    num_regions_y= int(sys.argv[3])
    # Load .png image
    image = cv2.imread(file_name)
    height, width,ch = image.shape 
    xx= int(width/num_regions_x)
    yy=int(height/num_regions_y)
    imges=[]
    for y in range(num_regions_y):
        for x in range(num_regions_x):
            im = image[y*yy: y*yy+yy, x*xx: x*xx+xx]
            scale = int(sys.argv[4+y*num_regions_x+x])
            print("Applying scale of",scale,"on region",x,y)
            im = cv2.resize(im, (int(xx/scale),int(yy/scale)))
            if jpeg:
                quality = int(sys.argv[2+num_regions_x*num_regions_x+ y*num_regions_x+x])
                print("Applying jpeg quality of",quality,"on region",x,y)
                encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),quality]
                result, imgencode = cv2.imencode('.jpg', im, encode_param)
                im=cv2.imdecode(imgencode,1)
            cv2.imwrite('image'+str(x)+str(y)+'.ppm', im)
            im = cv2.resize(im, (xx,yy),interpolation=cv2.INTER_LINEAR)
            imges.append(im)
    for y in range(0,num_regions_y):
        x_image= imges[y*num_regions_x]
        for x in range(1,num_regions_x):
            x_image= np.concatenate((x_image, imges[y*num_regions_x+x]), axis=1)
        if(y==0):
            y_image=x_image
        else:
            y_image= np.concatenate((y_image, x_image), axis=0)
    
    cv2.imwrite('patched.ppm', y_image)
except:
    print("error")
    print("usage, python resolution.py <input_image> <x_regions> <y_regions> <scale_of_region1> <scale_of_region2> .. <scale_of_region x*y>, <jpeg quality of region 1>, <jpeg quality of region 2> ...")
