import numpy as np
import matplotlib.pyplot as plt
import excelin
from excelin import dataexcelin
from numpy import mean
from numpy import std
import xlrd
import xlwt
from xlwt import Workbook

filename = open('GLA01_03100701_r2003_L2A.P0417_01_00.txt')
filelen = len(filename.readlines())
print(filelen)


list = filename.read( ).split('\n')

datagai=[]
datagai=list[329:586]
datagai1=list[587:844]
print(datagai)
print(datagai1)

