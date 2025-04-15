import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

PATH_TO_SRC = "../pilot-study-results/csv/"
PATH_TO_SAVE = "../pilot-study-results/graphs/"

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

# 100px per inch
plt.figure(figsize=(12, 5))
plt.bar(
    x=range(len(df.columns)),
    height=df.mean(),
    color=[colors["cs"], colors["go"]],
    edgecolor="black",
    width=0.6,
    yerr=df.sem(),
    capsize=7,
    alpha=0.5,
    bottom=0
)
plt.xticks(range(len(df.columns)), ["ASP.NET Core", "Echo"])
plt.ylabel('Response times (ms)')
plt.title('Comparison for both APIs')
plt.savefig(f"{PATH_TO_SAVE}stderr-{vus}vu-{data}.png")
plt.show()