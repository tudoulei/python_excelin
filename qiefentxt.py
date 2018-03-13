import numpy as np
import dataqiefen2
from dataqiefen2 import fenxi_data
from xlwt import Workbook

"检测整个文件"
filename = open('wuduan.txt')
filelen = len(filename.readlines())
print("主数据行数为：", filelen)
n = filelen/1619
n = int(n)
print(n)
"*********************************创建表格************************************************************"
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')  # 添加一个sheet
global sheet1
data_no1 = 0
"*********************************************************************************************"
for data_no2 in range(0, 5):
    filename = open('wuduan.txt')
    list = filename.read().split('\n')
    #print(list)
    #print(list[3])
    data_index = []
    data_index = list[(258 * data_no2):(258 * (data_no2+ 1) - 1)]
    print(data_index)
    fenxi_data(data_no1, data_no2, data_index)

book.save('test.xls')