
#!/usr/bin/env python
# encoding=utf-8
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from test import gauss_lvbo
import math
from PIL import Image
from PIL import ImageFilter

"***********显示原始图像************"
excelFile = ('test5.xls')
data = xlrd.open_workbook(excelFile)
table = data.sheets()[0]
#nrows = table.nrows #行数
#ncols = table.ncols #列数
nrows = input("输入数据行数，不要输入空行: ")
nrows = int(nrows)
data = table.cell(nrows, 11).value
index = table.cell(nrows, 1).value
print(index)
zhendata = data.split(' ') #字符串转为数值
arr = np.array(zhendata)
arr = arr.astype(np.float) #转化为float
print(arr)
fig=plt.figure()
fig.add_subplot(2,2,1)
plt.plot(arr, color='g')
plt.axis('tight')
plt.xlabel('xiangduishijian/ns')
plt.ylabel('zhenfu')
plt.title('UTC_time: %s ' % index)


"***********************电压值转换*************************"
a1 = 0.006675
a2 = 0.006198
b1 = -0.19528
b2 = -0.13442

zhendata_dianya = np.zeros(544)
for i in range(544):
    if arr[i] < 127:
        zhendata_dianya[i] = a1 * arr[i] + b1
    else:
        #zhendata(i)>127:#or zhendata(i)<255:
        zhendata_dianya[i] = a2 * arr[i] + b2
fig.add_subplot(2,2,2)
plt.plot(zhendata_dianya)
plt.xlabel('xiangduishijian/ns')
plt.ylabel('dianyazhi')
plt.title('UTC_time: %s ' % index)





"***********************波形正则化*************************"

vt = zhendata_dianya.sum()
zhendata_zhengze = zhendata_dianya/vt



fig.add_subplot(2,2,3)
plt.plot(zhendata_zhengze)
plt.xlabel('xiangduishijian/ns')
plt.ylabel('dianyazhi')
plt.title('UTC_time: %s ' % index)



"***********************数据解压缩*************************"




"***********************高斯滤波*************************"
lvbo = gauss_lvbo(zhendata_dianya)
fig.add_subplot(2,2,4)
plt.plot(lvbo)
plt.xlabel('xiangduishijian/ns')
plt.ylabel('dianyazhi')
plt.title('UTC_time: %s ' % index)
plt.show()