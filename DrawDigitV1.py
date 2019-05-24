import time
from turtle import *
def DrawLine(draw):
     drawgap()
     pendown() if draw else penup()
     fd(40)
     drawgap()
     right(90)

def drawDigit(digit):
     DrawLine(True) if digit in[2,3,4,5,6,8,9] else DrawLine(False)
     DrawLine(True) if digit in[0,1,3,4,5,6,7,8,9] else DrawLine(False)
     DrawLine(True) if digit in [0,2,3,5,6,8,9] else DrawLine(False)
     DrawLine(True) if digit in [0,2,6,8] else DrawLine(False)
     left(90)
     DrawLine(True) if digit in [0,4,5,6,8,9] else DrawLine(False)
     DrawLine(True) if digit in [0,2,3,5,6,7,8,9] else DrawLine(False)
     DrawLine(True) if digit in [0,1,2,3,4,7,8,9] else DrawLine(False)
     left(180)
     penup()
     fd(20)
     pendown()
     
def drawDate(date):
     for i in date:
          if i=='-':
               write('年',font=('Arial',18,'normal'))
               pencolor('green')
               penup()
               fd(40)
               pendown()
          elif i=='=':
               write('月',font=('Arial',18,'normal'))
               pencolor('red')
               penup()
               fd(40)
               pendown()
          elif i=='+':
               write('日',font=('Arial',18,'normal'))
          else:
               drawDigit(eval(i))
def drawgap():
     penup()
     fd(5)
def main():
     setup(800,400,200,200)
     penup()
     fd(-300)
     pensize(5)
     drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
     hideturtle()
     done()
main()

     


