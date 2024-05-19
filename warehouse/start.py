# -*- coding: gbk -*-
import OpencvCamera as opc


if __name__ == '__main__':
    
    # 参数见 Liquid_demo()
    ip = "10.68.19.164"#"此处输入摄像头ip"  
    real_h = 10.0
    ratio = 0.02
    threshold = 7.0
    opc.Liquid_demo(ip,real_h,ratio,threshold)
    
