#AutoTraceDraw.py
from turtle import *
title('自动轨迹绘制')
setup(800,600,0,0)
pencolor('red')
pensize(5)
#数据读取
datals=[]
f=open('data.txt')
for line in f:
     line=line.replace("\n",' ')
     datals.append(list(map(eval,line.split(','))))
     print(datals)
f.close()
#图形绘制
for i in range(len(datals)):
     pencolor(datals[i][3],datals[i][4],datals[i][5])
     fd(datals[i][0])
     if datals[i][1]:
          right(datals[i][2])
     else:
          left(datals[i][2])
          
