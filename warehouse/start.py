# -*- coding: gbk -*-
import OpencvCamera as opc


if __name__ == '__main__':
	
	# ������������ͷ��ip
    ip = "10.68.19.164"
    # real_h Ϊˮλ����ܳ���
    real_h = 10.0
    # ����ͼ��ˮλ��ʵ��ˮλ��ת������
    ratio = 0.02
    # ���ñ�����ֵ
    threshold = 7.0
    opc.Liquid_demo(ip,real_h,ratio,threshold)
    
