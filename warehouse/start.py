# -*- coding: gbk -*-
import OpencvCamera as opc


if __name__ == '__main__':
	
	# 设置连接摄像头的ip
    ip = "10.68.19.164"
    # real_h 为水位标尺总长度
    real_h = 10.0
    # 设置图像水位与实际水位的转换比例
    ratio = 0.02
    # 设置报警阈值
    threshold = 7.0
    opc.Liquid_demo(ip,real_h,ratio,threshold)
    
