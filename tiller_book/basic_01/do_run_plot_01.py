import sys
model_name = sys.argv[1].replace(".mo", "")

STR_TEMPLATE = f"""
loadFile("{model_name}.mo");
checkModel({model_name});
simulate({model_name}, startTime=0.0, stopTime=10.0, outputFormat="csv");
print(getErrorString());
"""

file = open("TEMP_scr.mos", "w")
file.write(STR_TEMPLATE)
file.close()

import subprocess
result = subprocess.run(["omc", "TEMP_scr.mos"]) 

# The returncode attribute indicates the command's exit status (0 usually means success)
print("Exit code:", result.returncode)


from numpy import genfromtxt

import matplotlib.pyplot as plt
plt.style.use("dark_background")

result_file = model_name + "_res.csv"

# Parse header
line = open(result_file, "r").readline().strip()
headers = line.replace("\"", "").split(",")
Ncols = len(headers)

# Read data, skip header (first line)
data = genfromtxt(result_file, delimiter=',')

plt.clf()
for icol in range(1,Ncols):
    plt.plot(data[:,0], data[:,icol], linewidth=2, label=headers[icol])
plt.xlabel(headers[0])
plt.legend()
plt.savefig(f"IMG_{model_name}.png", dpi=150)
