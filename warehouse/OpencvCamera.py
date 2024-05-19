# -*- coding: gbk -*-
import cv2 as cv
import numpy as np
########################################


# ������
windox = "camera"

# ˮλͼ��ɼ�
def Liquid_demo(ip,real_h,ratio,threshold):
    '''
    This function is used to detect the height of the water level
    
    Parameters:
        ip(string): camera ip
        real_h(float): Length of water level ruler (line)
        ratio(float): Scale factor of image size to actual size
        threshold(float): Water level warning thresholds
    
    '''
    # ������ʾ����
    cv.namedWindow(windox,1)
    # �˴�����IP����ͷ���ɵľ�������ַ
    video = "http://admin:admin@" + ip +":8081/"
    # ��������ͷ
    capture = cv.VideoCapture(video)
    print('����ͷ������!')
    
    # ������Ƶ��ַ��video��ʵҲ���Ի��ɵ����е���Ƶ��ַ����������һ����������
    while True:
        # ��ȡÿһ֡ͼ��
        success, img = capture.read()  
        # img = cv.flip(img, 1)   # ͼ��ˮƽ��ת
        # img = cv.rotate(img,cv.ROTATE_90_CLOCKWISE) # ͼ��˳ʱ��90�ȷ�ת  
        
        # ʵ��ͼ��Ŵ�
        # �ı�ͼ��ߴ�
        resize_img = cv.resize(img,dsize=(1200,1400))  
        # ��ȡ����ͼ��
        resize_img = resize_img[400:1000,400:1000]
        # ת��Ϊ�Ҷ�ͼ��
        gray_img = cv.cvtColor(resize_img,cv.COLOR_BGR2GRAY)    

        
        # ��˹�˲�
        aussian = cv.GaussianBlur(gray_img,(5,5),1)
   
        # ��Ե���Sobal���� x ����
        sobel_x = cv.Sobel(aussian,cv.CV_64F,1,0,ksize=3)
        sobel_x = cv.convertScaleAbs(sobel_x)

        # ��ֵ ��ֵ��
        thresh =  160   #��ֵ
        maxval = 255    #���ֵ��������
        ret,dst = cv.threshold(sobel_x,thresh,maxval,cv.THRESH_BINARY) #cv.THRESH_BINARY ��ֵ��
     
        # ��̬ѧ ����
        # ����ṹԪ��
        kernel = np.ones((3,3),np.uint8)
        # ��������
        dilatation = cv.dilate(dst,kernel,iterations = 1)
        dilatation = cv.dilate(dilatation,kernel,iterations = 1)
        # �������
        contours, hierarchy = cv.findContours(dilatation,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
         
        # ��Ӿ���
        if len(contours) > 0 :
            y = []
            for i in range(0,len(contours)):
                epsilon = 0.1*cv.arcLength(contours[i],True)
                y.append(epsilon)
            marks = y.index(max(y))   
            cnt = contours[marks]
            # ��ȡ������ͼ��� (x,y) �� ���     
            x,y,w,h = cv.boundingRect(cnt)
            # ��ͼ�л�����Ӿ���
            resize_img = cv.rectangle(resize_img,(x,y),(x+w,y+h),(0,255,0),2)
            
            # ת��Ϊʵ�ʸ߶�
            test_h = h*ratio 
            if test_h <= real_h:
                test_h = round(real_h - test_h,2)
            else:
                # ���Ϊ��ֵ�����߶�Ϊ 0
                test_h = 0
            if test_h > threshold:
                # ������ֵ��ʾ Warnings
                resize_img	= cv.putText(resize_img, str('Warnings'),(40, 120), cv.FONT_HERSHEY_SIMPLEX, 2.0,(0, 0, 255), 3)   
            # ������ˮλ test_h 
            resize_img	= cv.putText(resize_img, str(test_h),(40, 60), cv.FONT_HERSHEY_SIMPLEX, 2.0,(0, 255, 0), 3)    
            
        # ��ʾͼ��
        cv.imshow(windox,resize_img)   
        key = cv.waitKey(10)
        if key == ord('q'):  # ord���ַ�תΪ���Ӧ��ascii��
            # ���� q �˳�
            break

        if key == 32:  
            # �ո� ����
            filename = ".\\image\\Water.jpg"      
            cv.imwrite(filename, resize_img)  # ����һ��ͼ��     
            print("������һ��ͼ��")
    
    #�ͷ�����ͷ          
    capture.release()
    # ���մ���
    cv.destroyWindow(windox)        
           


