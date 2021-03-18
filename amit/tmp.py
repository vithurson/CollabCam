
#iters k int(sys.argv[1)
#xs = int(sys.argv[2])
#ys = int(sys.argv[3])
#
#cur_res = res[1]
## Load .png image
#crop_images=[]
#secs =  xs*ys
#xsize = int(cur_res/xs)
#ysize = int(cur_res/ys)
#image = image[0:2100,0:2100] 
#image = cv2.resize(image, (cur_res,cur_res))
#for y in range(ys):
#    for x in range(xs):
#        ylow= ysize*y 
#        yup= ysize*y + ysize
#        xlow = xsize*x 
#        xup = xsize*x + xsize
#        scale = int(sys.argv[4+(y*xs+x)])
#        crop_images.append(cv2.resize(image[ylow:yup, xlow:xup],(int(xsize/scale),int(ysize/scale))))
## Save .jpg image
#im_no = 1
#data_size = []
#for crop_image in crop_images:
#    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),100]
#    result, imgencode = cv2.imencode('.jpg', crop_image, encode_param)
#    data = numpy.array(imgencode)
#    stringData = data.tostring()
#    lent = len(stringData)
#    size = str(lent).ljust(16).encode('utf-8')
#    data_size.append([size, stringData])
#    im_no+=1
#start_time = time.time()
#for i in range(iters):
#    for datas in data_size:
#        sock.send(datas[0])
#        sock.send(datas[1])
#end_time = time.time()
