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
fram['zhenshu'].plot()


fram['1'] = fram['zhenshu'].rolling(window=4).mean()
#print(aaa)


fram.plot()
plt.show()
