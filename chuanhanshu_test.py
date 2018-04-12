"窗函数算法"

import xlrd
import numpy as np
import random
import matplotlib.pyplot as plt
from pandas import DataFrame


import pandas as pd
import scipy.signal
from gauss_juanji import gauss_lvbo

a = np.random.random_sample(100)

b = {'zhenshu': a}
fram = DataFrame(b)
print(b)
#fram['zhenshu'].plot()


fram['1'] = fram['zhenshu'].rolling(window=4, win_type=boxcar).mean()

fram.plot(subplots=True, figsize=(9, 5), grid=True)  # subplots 改为false就会合并到一张图
plt.xlim(0, 90)
plt.legend
plt.annotate('local max', xy=(40, 0.4), xytext=(50, 0.7),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )   # 箭头注释案例
plt.show()

"*********************************"
windowsize = [5,10,20]
for i in windowsize:
    fram['roll_mean_'+str(i)] = fram['zhenshu'].rolling(i).mean()
fram[['zhenshu', 'roll_mean_5', 'roll_mean_10', 'roll_mean_20']].plot(figsize=(9, 5), grid=True)
plt.show()