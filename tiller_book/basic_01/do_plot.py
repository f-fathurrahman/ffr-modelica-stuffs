import sys
from numpy import genfromtxt

import matplotlib.pyplot as plt
plt.style.use("dark_background")

# Check assumption
assert sys.argv[1].replace("_res.csv", "")

# Parse header
line = open(sys.argv[1], "r").readline().strip()
headers = line.replace("\"", "").split(",")
Ncols = len(headers)

# Read data, skip header (first line)
data = genfromtxt(sys.argv[1], delimiter=',')

plt.clf()
for icol in range(1,Ncols):
    plt.plot(data[:,0], data[:,icol], linewidth=2, label=headers[icol])
plt.xlabel(headers[0])
plt.legend()

prefix_name = sys.argv[1].replace("_res.csv", "")
plt.savefig(f"IMG_{prefix_name}.png", dpi=150)
