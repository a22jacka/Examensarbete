import scipy.stats as st
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd
import matplotlib.pyplot as plt
import glob

files = glob.glob("../grafana_k6/*get.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"go": "red", "cs":"blue"}

for file in files:
    df = pd.read_csv(file, sep=",", names=headers)
    x = range(0, len(df["durationJS"]))
    y = df["durationJS"].tolist()
    filename = file.split("/")[2]
    plt.plot(x, y, label=filename, color=colors[filename[:2]])
plt.legend()
plt.xlabel("Iterations")
plt.ylabel("Response time (ms)")
plt.title("Load times for the APIs")
#plt.grid(True)
plt.figure(figsize=(1, 1), dpi=80)
plt.show()