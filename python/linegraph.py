import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

files = glob.glob("../grafana_k6/p100-1000.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"go": "red", "cs": "blue"}

# 100px per inch
plt.figure(figsize=(18, 10))
ln = 0
for file in files:
    df = pd.read_csv(file, sep=",", names=headers, low_memory=False, skiprows=[0])
    x = range(0, len(df["durationJS"]))
    y = str_to_float(df["durationJS"])
    filename = file.split("/")[2]
    colour = colors[filename[:2]] if filename[:2] == "cs" or filename[:2] == "go" else "green"
    plt.plot(x, y, label=filename, color=colour)
    ln = len(df["durationJS"])
plt.legend()
plt.xlabel("Iterations")
plt.ylabel("Response time (ms)")
plt.title("Load times for the APIs")
plt.xticks(range(0, ln+1, round(ln/10)))
plt.yticks(range(0, 501, 10))
#plt.savefig("linegraph-s2-10-100.png")
plt.show()