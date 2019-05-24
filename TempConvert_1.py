#TempConvert.py
TemStr=input('请输入温度：')
if TemStr[0] in ['C','c']:
     F=1.8*eval(TemStr[1:20])+32
     print('转换后的温度是：{:.2f}F'.format(F))
elif TemStr[0] in ['F','f']:
     C=(eval(TemStr[1:20])-32)/1.8
     print('转换后的温度是：{:.2f}C'.format(C))
else:
     print('输入的格式有误')
     
