# -*- coding: gbk -*-
import OpencvCamera as opc


if __name__ == '__main__':
    
    # ������ Liquid_demo()
    ip = "10.68.19.164"#"�˴���������ͷip"  
    real_h = 10.0
    ratio = 0.02
    threshold = 7.0
    opc.Liquid_demo(ip,real_h,ratio,threshold)
    
