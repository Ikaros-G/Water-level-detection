# Water-level-detection
一个通过Opencv调用ip摄像头检测水位高度的简单实现。<br>
利用ip摄像头软件代替独立摄像头，通过opencv实现摄像头调用和图像处理检测水位

### 参数调整 (Parameter adjustments)
ip摄像头下载地址：https://www.downkuai.com/android/142512.html <br>
参数修改见 warehouse/start.py <br>
参数详情请见 warehouse/OpencvCamera.py 中 Liquid_demo() 注释

### 运行 (run)
1. 打开ip摄像头软件，点击打开IP摄像头服务器。将start.py文件中第 8 行的 ip 变量设置为摄像头app界面局域网IP。
2. 其余参数可根据需求更改
3. 运行 start.py
