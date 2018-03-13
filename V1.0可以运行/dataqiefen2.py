def fenxi_data(data_no1,data_no2,list,sheet1):
    import excelin
    from excelin import dataexcelin
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
    #print(data)  # 提取字符串
    zhendata = np.zeros(544)
    #print(data[1:3])  # 确认第一帧是否正确
    for i in range(0, 544):
        zhendata[i] = int(data[4 * i:4 * i + 3])

    #print("544帧数据为：")
    #print(zhendata)  # 输出544帧

    ##调换方向
    for i in range(0, 272):
        a = zhendata[i]
        zhendata[i] = zhendata[543 - i]
        zhendata[543 - i] = a
    dataexcelin(0,data_no1,data_no2, listname, zhendata,list,sheet1)

    "...............2.1.第二个光斑格式不一样了,,,,,,,,,,,,,,,,,,,,"
    for n in range(0, 7):
        i = 53 + n * 28  # 找到544帧数据并合并
        data = list[i]

        while i <= 80 + n * 28:
            data = data + list[i + 1]
            i = i + 1
        print("第段数据")
        #print(data)  # 提取字符串
        zhendata = np.zeros(544)

        for i in range(0, 544):
            zhendata[i] = int(data[4 * i:4 * i + 4])
        #print(zhendata)
        ##调换方向
        for i in range(0, 272):
            a = zhendata[i]
            zhendata[i] = zhendata[543 - i]
            zhendata[543 - i] = a
        dataexcelin(n + 1,data_no1,data_no2, listname, zhendata,list,sheet1)
