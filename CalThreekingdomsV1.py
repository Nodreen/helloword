#CalThreekindomsV1.py
from jieba import *
txt=open('2018政府工作报告.txt','r',encoding='utf-8').read()
#excludes={'将军','却说','荆州','二人','不可','不能','如此'}
words=lcut(txt)
counts={}
for word in words:
     if len(word)==1:
          continue
     else:
          counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
     word,count=items[i]
     print('{0:10}{1:>5}'.format(word,count))
     
