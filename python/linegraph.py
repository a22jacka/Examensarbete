import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

PATH_TO_SRC = "../results/csv/"
PATH_TO_SAVE = "../results/graphs/"

vus = 100
data = "1Mb"

files = glob.glob(f"{PATH_TO_SRC}*get-{vus}vu-{data}.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"echo": "red", "asp": "blue"}

# 100px per inch
plt.figure(figsize=(18, 10))
ln = 0
for file in files:
    df = pd.read_csv(file, sep=",", names=headers, low_memory=False, skiprows=101)
    x = range(0, len(df["durationJS"]))
    y = str_to_float(df["durationJS"])
    filename = file.split("/")[3].split("-")[0]
    plt.plot(x, y, label=filename, color=colors[filename])
    ln = len(df["durationJS"])
plt.legend()
plt.xlabel("Iterations")
plt.ylabel("Response time (ms)")
plt.title("Load times for the APIs")
plt.xticks(range(0, ln+1, 100))
plt.yticks(range(0, 3001, 100))
#plt.savefig(f"{PATH_TO_SAVE}{vus}vu-{data}.png")
plt.show()