import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import *

PATH_TO_SRC = "../results/measurement-error-research/no-sleep-const-local/"
PATH_TO_SAVE = PATH_TO_SRC
#PATH_TO_SAVE = "../results/measurement-error-research/no-sleep/"
IS_GET = 0 # 1 for GET, 0 for POST
vus = 100
data = "100kB"

files = glob.glob(f"{PATH_TO_SRC}*{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.csv")

headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"echo": "red", "asp": "blue"}

# 100px per inch
plt.figure(figsize=(12, 5))
ln = 0
for file in files:
    df = pd.read_csv(file, sep=",", names=headers, low_memory=False, skiprows=[0])
    x = range(0, len(df["durationJS"]))
    y = str_to_float(df["durationJS"])
    filename = file.split("/")[4].split("-")[0]
    plt.plot(x, y, label=filename, color=colors[filename])
    ln = len(df["durationJS"])
plt.legend()
plt.xlabel("Iterations")
plt.ylabel("Response time (ms)")
plt.title("Load times for the APIs")
plt.xticks(range(0, ln+1, 100))
plt.yticks(range(0, 241, 20)) 
plt.tight_layout()
plt.savefig(f"{PATH_TO_SAVE}{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.png")
plt.show()