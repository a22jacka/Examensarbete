import scipy.stats as st
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

files = glob.glob("../grafana_k6/*get_t.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"go": "red", "cs": "blue"}

# combines a specified column from 2 files into one dataframe
csdf = pd.read_csv(files[0], sep=",", header=None, names=headers, low_memory=False, skiprows=[0])
godf = pd.read_csv(files[1], sep=",", header=None, names=headers, low_memory=False, skiprows=[0])
df = pd.DataFrame({"cs": str_to_float(csdf["durationJS"])})
df["go"] = str_to_float(godf["durationJS"])

# 100px per inch
plt.figure(figsize=(18, 10))
plt.bar(
    x=range(len(df.columns)),
    height=df.mean(),
    color=[colors["cs"], colors["go"]],
    edgecolor="black",
    width=0.6,
    yerr=df.sem(),
    capsize=7,
    alpha=0.5,
    bottom=7
)
plt.xticks(range(len(df.columns)), df.columns)
plt.ylabel('Response times (ms)')
plt.title('Comparison for both APIs')
plt.savefig("segraph.png")
plt.show()