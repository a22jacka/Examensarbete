import scipy.stats as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

PATH_TO_SRC = "../results/csv/"
PATH_TO_SAVE = "../results/graphs/"

vus = 100
data = "1MB"

files = glob.glob(f"{PATH_TO_SRC}*get-{vus}vu-{data}.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"go": "red", "cs": "blue"}

# combines a specified column from 2 files into one dataframe
csdf = pd.read_csv(files[0], sep=",", header=None, names=headers, low_memory=False, skiprows=[0])
godf = pd.read_csv(files[1], sep=",", header=None, names=headers, low_memory=False, skiprows=[0])
df = pd.DataFrame({
    "cs": str_to_float(csdf["durationJS"]),
    "go": str_to_float(godf["durationJS"]),   
})

def calc_ci(data, confidence = 0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), st.sem(a)
    h = se * st.t.ppf((confidence + 1) / 2., n-1)
    return -h, +h

cis = pd.DataFrame({
    "cs": calc_ci(df["cs"]),
    "go": calc_ci(df["go"]),
})

plt.figure(figsize=(18,10))
plt.bar(
    x=range(len(df.columns)),
    height=df.mean(),
    edgecolor="black",
    color=[colors["cs"], colors["go"]],
    width=0.6,
    yerr=cis.iloc[1],
    capsize=7,
    bottom=7
)
plt.xticks(range(len(df.columns)), ["ASP.NET Core", "Echo"])
plt.ylabel("Response times (ms)")
plt.title("The confidence intervals for the APIs")
#plt.savefig("cigraph.png")
plt.show()