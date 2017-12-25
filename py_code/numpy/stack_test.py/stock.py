# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt
import numpy as np
import sys

input_file = "D:\py_code\\numpy_code\Code\ch3code\data.csv"
c = np.loadtxt(input_file, delimiter=',', usecols=(6,), unpack=True)
returns = np.diff(c) / c[:-1]
print "standard deviation =", np.std(returns)
logreturns = np.diff(np.log(c))
posrestindices = np.where( returns > 0)
print "indices with positive returns", posrestindices
annual_volatility = np.std(logreturns)/np.mean(logreturns)
annual_volatility = annual_volatility/np.sqrt(1./252.)
print "Annual volatility", annual_volatility
print "Monthly volatility", annual_volatility*np.sqrt(1./12.)
