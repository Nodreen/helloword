import random

def genpwd(length):
    if length==0:
        return 0
    else:
        return genpwd(str(random.randint(0,9))+genpwd(length))
        len

length = eval(input('请输入'))
random.seed(17)
for i in range(3):
    print(genpwd(length))
