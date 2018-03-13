import xlrd
import xlwt

workbook = xlrd.open_workbook(r'test.xls')
print(workbook.sheet_names())

# 根据sheet索引或者名称获取sheet内容

sheet2 = workbook.sheet_loaded('Sheet 1')  # sheet索引从0开始

sheet2.write(0,0,'序号')