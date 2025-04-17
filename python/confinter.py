import scipy.stats as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

PATH_TO_SRC = "../pilot-study-results/csv/"
PATH_TO_SAVE = "../pilot-study-results/graphs/"

vus = 10
data = "1MB"
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"Echo": "red", "ASP.NET Core": "blue"}

# combines a specified column from 2 files into one dataframe
csdf = pd.read_csv(glob.glob(f"{PATH_TO_SRC}asp-get-{vus}vu-{data}.csv")[0], sep=",", header=None, names=headers, low_memory=False, skiprows=[0])
godf = pd.read_csv(glob.glob(f"{PATH_TO_SRC}echo-get-{vus}vu-{data}.csv")[0], sep=",", header=None, names=headers, low_memory=False, skiprows=[0])
df = pd.DataFrame({
    "ASP.NET Core": str_to_float(csdf["durationJS"]),
    "Echo": str_to_float(godf["durationJS"]),
})

def calc_ci(data, confidence = 0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), st.sem(a)
    h = se * st.t.ppf((confidence + 1) / 2., n-1)
    return -h, +h

cis = pd.DataFrame({
    "ASP.NET Core": calc_ci(df["ASP.NET Core"]),
    "Echo": calc_ci(df["Echo"]),
})

plt.figure(figsize=(12,5))
plt.bar(
    x=range(len(df.columns)),
    height=df.mean(),
    edgecolor="black",
    color=[colors[df.columns[0]], colors[df.columns[1]]],
    width=0.6,
    yerr=cis.iloc[1],
    capsize=7,
    bottom=0
)
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(0, 20, 5))
plt.ylabel("Response times (ms)")
plt.title("The confidence intervals for the APIs")
plt.tight_layout()
#post
#plt.savefig(f"{PATH_TO_SAVE}post-confinter-{vus}vu.png")
#get
#plt.savefig(f"{PATH_TO_SAVE}get-confinter-{vus}vu-{data}.png")
plt.show()