def gauss_lvbo(x):
    import numpy as np
    import math
    import scipy.signal
    import matplotlib.pyplot as plt

    sita = np.std(x)
    print(sita)
    pi = 3.14
    h = np.zeros(544)
    for t in range(0, 544):
        h[t] = (-t / (math.sqrt(2 * pi * sita ** 3))) * math.exp(-(t**2) / (2 * sita ** 2))
    print(h)
    plt.plot(h)
    arr = scipy.signal.convolve(x,h, mode='same' ) #卷积运算
    return arr


