import numpy as np
import matplotlib.pyplot as plt
from numpy import mean
from numpy import std
import xlrd
import xlwt
from xlwt import Workbook


filename = open('1.txt')
#求行数
#filelen = len(filename.readlines())
#print(filelen)
list = filename.read( ).split('\n')
print(list)
print(list[3])

"...............1.读取这段数据编号,,,,,,,,,,,,,,,,,,,,"
listname=list[3]
listname=listname[18:31]
print("GLAS记录索引值为：",listname)

"...............2.将544帧数据存到数组内,,,,,,,,,,,,,,,,,,,,"
i = 25     #找到544帧数据并合并
data=list[25]
while i <= 51:
    data=data+list[i+1]
    i=i+1
data=data[19:10000]
print(data)           #提取字符串
zhendata = np.zeros(544)
print(data[1:3])       #确认第一帧是否正确
for i in range(0,544):
    zhendata[i]=int(data[4*i:4*i+3])

print("544帧数据为：")
print(zhendata)        #输出544帧
plt.plot(zhendata)
plt.show()
#调换方向
for  i in range(0,272):
    a=zhendata[i]
    zhendata[i]=zhendata[543-i]
    zhendata[543-i]=a
plt.plot(zhendata)
plt.show()

"...............3.计算,,,,,,,,,,,,,,,,,,,,"
datamax = max(zhendata[0:99])
datamean = mean(zhendata[0:99])
datastd = std(zhendata[0:99])
print(datamax)
print(datamean)
print(datastd)
datamax_3times_std = datamax + 3 * datastd
datamax_4times_std = datamax + 4 * datastd
datamax_5times_std = datamax + 5 * datastd
datamean_3times_std = datamean + 3 * datastd
datamean_4times_std = datamean + 4 * datastd
datamean_5times_std = datamean + 5 * datastd

print("最大值加上3倍标准差：",datamax_3times_std)
print("最大值加上4倍标准差：",datamax_4times_std)
print("最大值加上5倍标准差：",datamax_5times_std)
print("平均值加上3倍标准差：",datamean_3times_std)
print("平均值加上4倍标准差：",datamean_4times_std)
print("平均值加上5倍标准差：",datamean_5times_std)

"...............4.放到excel中,,,,,,,,,,,,,,,,,,,,"
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')  #添加一个sheet

sheet1.write(0,0,'序号')
sheet1.write(0,1,'最大值加上3倍标准差')   #通过sheet添加cell值
sheet1.write(0,2,'最大值加上4倍标准差')
sheet1.write(0,3,'最大值加上5倍标准差')
sheet1.write(0,4,'平均值加上3倍标准差')
sheet1.write(0,5,'平均值加上4倍标准差')
sheet1.write(0,6,'平均值加上5倍标准差')

row1 = sheet1.row(1)
row1.write(0,listname)     #还可以通过row属性添加cell值
row1.write(1,datamax_3times_std)
row1.write(2,datamax_4times_std)
row1.write(3,datamax_5times_std)
row1.write(4,datamean_3times_std)
row1.write(5,datamean_4times_std)
row1.write(6,datamean_5times_std)

sheet1.col(0).width = 10000
book.save('test.xls')