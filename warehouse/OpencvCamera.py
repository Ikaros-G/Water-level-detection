# -*- coding: gbk -*-
import cv2 as cv
import numpy as np
########################################


# 窗口名
windox = "camera"

# 水位图像采集
def Liquid_demo(ip,real_h,ratio,threshold):
    '''
    This function is used to detect the height of the water level
    
    Parameters:
        ip(string): camera ip
        real_h(float): Length of water level ruler (line)
        ratio(float): Scale factor of image size to actual size
        threshold(float): Water level warning thresholds
    
    '''
    # 创建显示窗口
    cv.namedWindow(windox,1)
    # 此处根据IP摄像头生成的局域网地址
    video = "http://admin:admin@" + ip +":8081/"
    # 调用摄像头
    capture = cv.VideoCapture(video)
    print('摄像头已启动!')
    
    # 引入视频地址，video其实也可以换成电脑中的视频地址可以制作成一个播放器。
    while True:
        # 读取每一帧图像
        success, img = capture.read()  
        # img = cv.flip(img, 1)   # 图像水平反转
        # img = cv.rotate(img,cv.ROTATE_90_CLOCKWISE) # 图像顺时针90度反转  
        
        # 实现图像放大
        # 改变图像尺寸
        resize_img = cv.resize(img,dsize=(1200,1400))  
        # 截取部分图像
        resize_img = resize_img[400:1000,400:1000]
        # 转化为灰度图像
        gray_img = cv.cvtColor(resize_img,cv.COLOR_BGR2GRAY)    

        
        # 高斯滤波
        aussian = cv.GaussianBlur(gray_img,(5,5),1)
   
        # 边缘检测Sobal算子 x 方向
        sobel_x = cv.Sobel(aussian,cv.CV_64F,1,0,ksize=3)
        sobel_x = cv.convertScaleAbs(sobel_x)

        # 阈值 二值化
        thresh =  160   #阈值
        maxval = 255    #最大值（最亮）
        ret,dst = cv.threshold(sobel_x,thresh,maxval,cv.THRESH_BINARY) #cv.THRESH_BINARY 二值化
     
        # 形态学 膨胀
        # 构造结构元素
        kernel = np.ones((3,3),np.uint8)
        # 进行膨胀
        dilatation = cv.dilate(dst,kernel,iterations = 1)
        dilatation = cv.dilate(dilatation,kernel,iterations = 1)
        # 轮廓检测
        contours, hierarchy = cv.findContours(dilatation,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
         
        # 外接矩形
        if len(contours) > 0 :
            y = []
            for i in range(0,len(contours)):
                epsilon = 0.1*cv.arcLength(contours[i],True)
                y.append(epsilon)
            marks = y.index(max(y))   
            cnt = contours[marks]
            # 获取矩形在图像的 (x,y) 和 宽高     
            x,y,w,h = cv.boundingRect(cnt)
            # 在图中绘制外接矩形
            resize_img = cv.rectangle(resize_img,(x,y),(x+w,y+h),(0,255,0),2)
            
            # 转换为实际高度
            test_h = h*ratio 
            if test_h <= real_h:
                test_h = round(real_h - test_h,2)
            else:
                # 如果为负值则至高度为 0
                test_h = 0
            if test_h > threshold:
                # 高于阈值显示 Warnings
                resize_img	= cv.putText(resize_img, str('Warnings'),(40, 120), cv.FONT_HERSHEY_SIMPLEX, 2.0,(0, 0, 255), 3)   
            # 输出检测水位 test_h 
            resize_img	= cv.putText(resize_img, str(test_h),(40, 60), cv.FONT_HERSHEY_SIMPLEX, 2.0,(0, 255, 0), 3)    
            
        # 显示图像
        cv.imshow(windox,resize_img)   
        key = cv.waitKey(10)
        if key == ord('q'):  # ord将字符转为其对应的ascii码
            # 按下 q 退出
            break

        if key == 32:  
            # 空格 拍照
            filename = ".\\image\\Water.jpg"      
            cv.imwrite(filename, resize_img)  # 保存一张图像     
            print("保存了一张图像")
    
    #释放摄像头          
    capture.release()
    # 回收窗口
    cv.destroyWindow(windox)        
           


