#DayDayUp02.py
a=0.005
dayup=pow(1+a,365)
daydown=pow(1-a,365)
print('向上{:.3f}'.format(dayup),'向下{:.3f}'.format(daydown))
