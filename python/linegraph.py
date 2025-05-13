import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import *

PATH_TO_SRC = "../results/csv/"
PATH_TO_SAVE = "../results/graphs/"
IS_GET = 1 # 1 for GET, 0 for POST
vus = 50
data = "10kB"

files = glob.glob(f"{PATH_TO_SRC}*-{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.csv")

headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset","bodyLength"]
colors = {"echo": "red", "asp": "blue"}

# 100px per inch
plt.figure(figsize=(12, 5))
ln = 0
rows_to_skip = int(vus * 2 + 1)
for file in files:
    df = pd.read_csv(file, sep=",", names=headers, low_memory=False, skiprows=rows_to_skip, index_col=False)
    x = range(0, len(df["durationJS"]))
    y = str_to_float(df["durationJS"])
    filename = file.split("/")[3].split("-")[0]
    plt.plot(x, y, label=filename, color=colors[filename])
    ln = len(df["durationJS"])
plt.legend()
plt.xlabel("Iterations")
plt.ylabel("Response time (ms)")
plt.title("Load times for the APIs")
plt.xticks(range(0, ln+1, 1000))
plt.yticks(range(0, 101, 10))
plt.tight_layout()
plt.savefig(f"{PATH_TO_SAVE}line-{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.png")
plt.show()