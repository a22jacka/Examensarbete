import pandas as pd
import matplotlib.pyplot as plt
import glob
from misc import str_to_float

PATH_TO_SRC = "../results/csv/"
PATH_TO_SAVE = "../results/graphs/"

IS_GET = 1 # 1 for GET, 0 for POST
vus = 100
data = "10kB"
rows_to_skip = vus * 2 + 1
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset","bodyLength"]
colors = {"Echo": "red", "ASP.NET Core": "blue"}

# combines a specified column from 2 files into one dataframe
csdf = pd.read_csv(glob.glob(f"{PATH_TO_SRC}asp-{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.csv")[0], sep=",", header=None, names=headers, low_memory=False, skiprows=rows_to_skip, index_col=False)
godf = pd.read_csv(glob.glob(f"{PATH_TO_SRC}echo-{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.csv")[0], sep=",", header=None, names=headers, low_memory=False, skiprows=rows_to_skip, index_col=False)
df = pd.DataFrame({
    "ASP.NET Core": str_to_float(csdf["durationJS"]),
    "Echo": str_to_float(godf["durationJS"]),
})
# 100px per inch
plt.figure(figsize=(7, 5))
y_err = df.sem()
plt.bar(
    x=range(len(df.columns)),
    height=df.mean(),
    color=[colors[df.columns[0]], colors[df.columns[1]]],
    edgecolor="black",
    width=0.5,
    yerr=y_err,
    capsize=7,
    bottom=0
)
plt.xticks(range(len(df.columns)), [f"{df.columns[0]}\n{round(y_err[0], 3)}", f"{df.columns[1]}\n{round(y_err[1], 3)}"])
plt.yticks(range(0, 41, 5))
plt.ylabel('Response times (ms)')
plt.title('Comparison for both APIs')
plt.tight_layout()
plt.savefig(f"{PATH_TO_SAVE}stderr-{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.png")
plt.show()