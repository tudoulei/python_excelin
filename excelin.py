"****************3.计算所需要的值；标准差之类******************"

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
