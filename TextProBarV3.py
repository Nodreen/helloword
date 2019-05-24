#TextProBarV3.py
from time import *
scale=100
print('执行开始'.center(scale//2,'-'))
start=perf_counter()
for i in range(scale+1):
     a='*'*i
     b='*'*(scale-i)
     c=(i/scale)*100
     dur=perf_counter()-start
     print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end=' ')
     sleep(1)
print('\n'+'执行结束'.center(scale//2,'-'))
