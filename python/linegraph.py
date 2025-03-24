import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

files = glob.glob("../grafana_k6/*get_t.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"go": "red", "cs": "blue"}

# 100px per inch
plt.figure(figsize=(18, 10))
for file in files:
    df = pd.read_csv(file, sep=",", names=headers, low_memory=False, skiprows=[0])
    x = range(0, len(df["durationJS"]))
    y = str_to_float(df["durationJS"])
    filename = file.split("/")[2]
    plt.plot(x, y, label=filename, color=colors[filename[:2]])
plt.legend()
plt.xlabel("Iterations")
plt.ylabel("Response time (ms)")
plt.title("Load times for the APIs")
plt.xticks(range(0, 100001, 10000))
plt.yticks(range(0, 401, 20))
plt.savefig("linegraph.png")
plt.show()