from __future__ import print_function

import scipy.io
import sys

matdata = scipy.io.loadmat(sys.argv[1])
print(matdata)

import matplotlib.pyplot as plt

x  = matdata["data_2"][0,:]
y1 = matdata["data_2"][1,:]
y2 = matdata["data_2"][2,:]

plt.clf()
plt.plot(x, y1, linewidth=2, label="y1")
plt.plot(x, y2, linewidth=2, label="y2")
plt.legend()
plt.savefig("plot.png", dpi=300)


