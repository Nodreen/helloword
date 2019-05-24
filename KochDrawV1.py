#KochDrawV1.py
from turtle import *
def koch(size,n):
     if n==0:
          fd(size)
     else:
          for angle in [0,60,-120,60]:
               left(angle)
               koch(size/3,n-1)
def main():
     setup(600,600)
     pu()
     goto(-200,100)
     pd()
     pensize(2)
     level=5
     for i in range(3):
          koch(400,level)
          right(120)
     hideturtle()
main()

     
          
