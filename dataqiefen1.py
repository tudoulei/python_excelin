"提取光斑进行简单噪声分析算法"
from xlwt import Workbook

# from dataqiefen2 import fenxi_data

"UTCTime 相对于2000年1月1日中午时间，第一字段记录的是秒，第二字段记录的是微秒部分"
"检测整个文件"

"*******************************1.打开文件*************************************************"
names = 'GLA01_03100701_r2003_L2A.P0417_01_00.txt'  # 文件名修改
filename = open(names)
filelen = len(filename.readlines())
print("主数据行数为：", filelen)
n = filelen / 1619
n = int(n)  # main个数
print(n)

"*********************************2.创建表格************************************************************"

book = Workbook()
sheet1 = book.add_sheet('Sheet 1', cell_overwrite_ok=True)  # 添加一个sheet

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

"****************3.提取光斑******************"


def fenxi_data(data_no1, data_no2, list, sheet1):
    import numpy as np
    data_no2 = data_no2
    data_no1 = data_no1
    "...............1.读取这段数据编号,,,,,,,,,,,,,,,,,,,,"
    listname = list[3]
    listname = listname[18:80]
    print("GLAS记录索引值为：", listname)

    "...............2.将544帧数据存到数组内,,,,,,,,,,,,,,,,,,,,"
    i = 25  # 找到544帧数据并合并
    data = list[25]
    while i <= 51:
        data = data + list[i + 1]
        i = i + 1
    data = data[19:10000]
    # print(data)  # 提取字符串
    zhendata = np.zeros(544)
    # print(data[1:3])  # 确认第一帧是否正确
    for i in range(0, 544):
        zhendata[i] = int(data[4 * i:4 * i + 3])

    ##调换方向
    for i in range(0, 272):
        a = zhendata[i]
        zhendata[i] = zhendata[543 - i]
        zhendata[543 - i] = a
    dataexcelin(0, data_no1, data_no2, listname, zhendata, list, sheet1)

    "...............2.1.第二个光斑格式不一样了,,,,,,,,,,,,,,,,,,,,"
    for n in range(0, 7):
        i = 53 + n * 28  # 找到544帧数据并合并
        data = list[i]

        while i <= 80 + n * 28:
            data = data + list[i + 1]
            i = i + 1
        print("第段数据")
        # print(data)  # 提取字符串
        zhendata = np.zeros(544)

        for i in range(0, 544):
            zhendata[i] = int(data[4 * i:4 * i + 4])
        # print(zhendata)
        ##调换方向
        for i in range(0, 272):
            a = zhendata[i]
            zhendata[i] = zhendata[543 - i]
            zhendata[543 - i] = a
        dataexcelin(n + 1, data_no1, data_no2, listname, zhendata, list, sheet1)


"****************4.计算所需要的值；标准差之类******************"


def dataexcelin(n, data_no1, data_no2, listname, zhendata, list, sheet1):
    import numpy as np
    from numpy import mean
    from numpy import std

    print("MAIN 序列：", data_no1, "LONG 序列：", data_no2)

    "*******************数据处理**********************"
    i_rec_ndx = list[3]
    i_rec_ndx = i_rec_ndx[18:31]
    # print("GLAS记录索引值为：", listname)
    i_UTCTime = list[4]
    i_UTCTime = i_UTCTime[18:46]  # 未测试列数，整行读入
    datamax = max(zhendata[0:99])
    datamean = mean(zhendata[0:99])
    datastd = std(zhendata[0:99])
    hou_datamax = max(zhendata[0:99])
    datamax_3times_std = datamax + 3 * datastd
    datamax_4times_std = datamax + 4 * datastd
    datamax_5times_std = datamax + 5 * datastd
    datamean_3times_std = datamean + 3 * datastd
    datamean_4times_std = datamean + 4 * datastd
    datamean_5times_std = datamean + 5 * datastd

    "********************将帧数数据变为字符串*********************"
    zongdata = [0 for i in range(544)]
    zongdata = np.vstack((zongdata, zhendata))

    "*********************存到excel中******************************"

    huanhang = n + data_no1 * 45 + data_no2 * 9 + 1  # 数据应该放到哪一行
    row1 = sheet1.row(huanhang)
    print("数据写入第几行", huanhang)

    row1.write(0, i_rec_ndx)
    row1.write(1, i_UTCTime)
    row1.write(3, datamax_3times_std)
    row1.write(4, datamax_4times_std)
    row1.write(5, datamax_5times_std)
    row1.write(6, datamean_3times_std)
    row1.write(7, datamean_4times_std)
    row1.write(8, datamean_5times_std)
    row1.write(9, hou_datamax)
    print(zhendata)
    print("元素个数：")
    print(len(zhendata))
    row1.write(11, len(zhendata))

    "*********************导入帧数数据********************"
    # 失败：不能将一帧帧数据存到excel中，因为excel最多有256列
    # for zhenshu in range(280):
    #    row1.write(20+zhenshu, zhendata[zhenshu])
    #    #if zhendata[zhenshu] < 0:
    #     #   break
    # str = ','.join(zhendata)
    # print(str)
    "将帧数合并到一个字符串内保存"
    a = " ".join('%s' % id for id in zhendata)
    row1.write(11, a)


"*********************************5.切分数据，调用两个函数，fenxi_data和dataexcelin****************************************"
for data_no1 in range(0, n):  # n为main的总数
    filename = open(names)
    list = filename.read().split('\n')
    data_index = []
    data_index = list[data_no1 * 1619:(data_no1 + 1) * 1619 - 1]

    "处理1619行数据内的断头文件+切分五个数据操作"
    data_wuhang = data_index[329:1618]

    data_wuduan = []
    for data_no2 in range(0, 5):
        data_wuduan = data_wuhang[258 * data_no2:258 * (data_no2 + 1) - 1]
        fenxi_data(data_no1, data_no2, data_wuduan, sheet1)

book.save('test5.xls')
