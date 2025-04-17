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

# 100px per inch
plt.figure(figsize=(12, 5))
plt.bar(
    x=range(len(df.columns)),
    height=df.mean(),
    color=[colors[df.columns[0]], colors[df.columns[1]]],
    edgecolor="black",
    width=0.6,
    yerr=df.sem(),
    capsize=7,
    alpha=0.5,
    bottom=0
)
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(0, 21, 5))
plt.ylabel('Response times (ms)')
plt.title('Comparison for both APIs')
plt.tight_layout()
#post
#plt.savefig(f"{PATH_TO_SAVE}post-stderr-{vus}vu.png")
#get
#plt.savefig(f"{PATH_TO_SAVE}post-stferr-{vus}vu-{data}.png")
plt.show()