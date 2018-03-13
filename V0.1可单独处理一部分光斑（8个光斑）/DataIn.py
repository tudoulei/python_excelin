import numpy as np
import matplotlib.pyplot as plt
import excelin
from excelin import dataexcelin
from numpy import mean
from numpy import std
import xlrd
import xlwt
from xlwt import Workbook

"...............0.创建表格,,,,,,,,,,,,,,,,,,,,"

book = Workbook()
sheet1 = book.add_sheet('Sheet 1')  # 添加一个sheet
sheet1.write(0, 0, '序号')
sheet1.write(0, 1, '最大值加上3倍标准差')  # 通过sheet添加cell值
sheet1.write(0, 2, '最大值加上4倍标准差')
sheet1.write(0, 3, '最大值加上5倍标准差')
sheet1.write(0, 4, '平均值加上3倍标准差')
sheet1.write(0, 5, '平均值加上4倍标准差')
sheet1.write(0, 6, '平均值加上5倍标准差')

filename = open('6.txt')
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

##调换方向
for  i in range(0,272):
    a=zhendata[i]
    zhendata[i]=zhendata[543-i]
    zhendata[543-i]=a
dataexcelin(sheet1,1,listname,zhendata)

"...............2.1.第二个光斑格式不一样了,,,,,,,,,,,,,,,,,,,,"
for n in range(0,7):
    i = 53 + n * 28     #找到544帧数据并合并
    data=list[i]

    while i <= 80+n * 28:
       data=data+list[i+1]
       i=i+1
    print("第段数据")
    print(data)           #提取字符串
    zhendata = np.zeros(544)

    for i in range(0,544):
       zhendata[i]=int(data[4*i:4*i+4])
    print(zhendata)
    ##调换方向
    for i in range(0, 272):
        a = zhendata[i]
        zhendata[i] = zhendata[543 - i]
        zhendata[543 - i] = a
    dataexcelin(sheet1,n+2,listname,zhendata)
    book.save('test.xls')

book.save('test.xls')
