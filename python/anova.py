import scipy.stats as st
import pandas as pd
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

stats, p_value = st.f_oneway(df["ASP.NET Core"], df["Echo"])
print(f"Calculation for {vus} VUs getting {data} each")
print(f'Anova stats: {str(stats)}, p_value: {str(p_value)}, Difference: {p_value < stats}')