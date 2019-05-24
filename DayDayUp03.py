#DayDayUp03.py
a=0.01
dayup=1.0
for i in range(365):
     if i%7 in [0,6]:
          dayup*=(1-a)
     else:
          dayup*=(1+a)
print('工作日的力量是:{:.4f}'.format(dayup))

          
