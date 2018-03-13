
from xlwt import Workbook
from dataqiefen2 import fenxi_data
"UTCTime 相对于2000年1月1日中午时间，第一字段记录的是秒，第二字段记录的是微秒部分"
"检测整个文件"

"*******************************打开文件*************************************************"

filename = open('GLA01_03100701_r2003_L2A.P0417_01_00.txt')
filelen = len(filename.readlines())
print("主数据行数为：", filelen)
n = filelen/1619
n = int(n)  #main个数
print(n)


"*********************************创建表格************************************************************"

book = Workbook()
sheet1 = book.add_sheet('Sheet 1',cell_overwrite_ok=True) # 添加一个sheet

sheet1.write(0, 0, 'GPS记录索引值；i_rec_ndx')
sheet1.write(0, 1, '第一个足印点的发射时间：i_UTCTime')
sheet1.write(0, 2, '  ')
sheet1.write(0, 3, '最大值加上3倍标准差')  # 通过sheet添加cell值
sheet1.write(0, 4, '最大值加上4倍标准差')
sheet1.write(0, 5, '最大值加上5倍标准差')
sheet1.write(0, 6, '平均值加上3倍标准差')
sheet1.write(0, 7, '平均值加上4倍标准差')
sheet1.write(0, 8, '平均值加上5倍标准差')
sheet1.write(0, 11, '544帧数据')



"*********************************切分数据************************************************************"
for data_no1 in range(0, n):#n
    filename = open('GLA01_03100701_r2003_L2A.P0417_01_00.txt')
    list = filename.read().split('\n')
    data_index = []
    data_index = list[data_no1 * 1619:(data_no1 + 1) * 1619 - 1]

    "处理1619行数据内的断头文件+切分五个数据操作"
    data_wuhang = data_index[329:1618]

    data_wuduan=[]
    for data_no2 in range(0, 5):
        data_wuduan = data_wuhang[258 * data_no2:258 * (data_no2+ 1) - 1]
        fenxi_data(data_no1,data_no2,data_wuduan,sheet1)

book.save('test5.xls')



