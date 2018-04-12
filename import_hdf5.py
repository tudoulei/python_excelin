"读取h5文件算法"

import h5py  #导入工具包
import numpy as np
#HDF5的写入：
filename = 'GLAH01_033_2131_002_0076_3_02_0001.H5'
imgData = np.zeros((30, 3, 128, 256))
f = h5py.File(filename, 'w')   #创建一个h5文件，文件指针是f
f['data'] = imgData                 #将数据写入文件的主键data下面
f['labels'] = range(100)            #将数据写入文件的主键labels下面
f.close()                           #关闭文件

#HDF5的读取：
f = h5py.File(filename, 'r')   #打开h5文件
f.keys()                            #可以查看所有的主键
a = f['data'][:]                    #取出主键为data的所有的键值
print(a)
f.close()