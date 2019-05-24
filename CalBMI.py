#CalBMI.v1
height,weight=eval(input())
bmi=weight/pow(height,2)
print('BMI数值是:{:.2f}'.format(bmi))
if bmi>=30:
     print('肥胖，肥胖')
elif 28<=bmi<30:
     print('偏胖，肥胖')
elif 25<=bmi<28:
     print('偏胖，偏胖')
elif 24<=bmi<25:
     print('正常，偏胖')
elif 18.5<=bmi<24:
     print('正常，正常')
else:
     print('偏瘦，偏瘦')
