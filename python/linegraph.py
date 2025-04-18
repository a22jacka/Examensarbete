import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

PATH_TO_SRC = "../pilot-study-results/csv/"
PATH_TO_SAVE = "../pilot-study-results/graphs/"

vus = 10
data = "100"
#post-files
#files = glob.glob(f"{PATH_TO_SRC}*post-{vus}vu.csv")
#get-files
files = glob.glob(f"{PATH_TO_SRC}*get-{vus}-{data}.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"echo": "red", "asp": "blue"}

# 100px per inch
plt.figure(figsize=(12, 5))
ln = 0
for file in files:
    df = pd.read_csv(file, sep=",", names=headers, low_memory=False, skiprows=[0])
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
plt.yticks(range(0, 101, 20))
plt.tight_layout()
#post
#plt.savefig(f"{PATH_TO_SAVE}post-line-{vus}vu.png")
#get
#plt.savefig(f"{PATH_TO_SAVE}get-line-{vus}vu-{data}.png")
plt.show()