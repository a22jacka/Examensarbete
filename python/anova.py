import scipy.stats as st
import pandas as pd
import glob
from misc import str_to_float

PATH_TO_SRC = "../pilot-study-results/csv/"
PATH_TO_SAVE = "../pilot-study-results/graphs/"

vus = 100
data = "1MB"

#post-files
files = glob.glob(f"{PATH_TO_SRC}*post-{vus}vu.csv")
#get-files
#files = glob.glob(f"{PATH_TO_SRC}*get-{vus}vu-{data}.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
colors = {"go": "red", "cs": "blue"}

# combines a specified column from 2 files into one dataframe
csdf = pd.read_csv(files[0], sep=",", header=None, names=headers, low_memory=False, skiprows=[0])
godf = pd.read_csv(files[1], sep=",", header=None, names=headers, low_memory=False, skiprows=[0])
df = pd.DataFrame({
    "cs": str_to_float(csdf["durationJS"]),
    "go": str_to_float(godf["durationJS"]),   
})

stats, p_value = st.f_oneway(*[df["cs"], df["go"]])
print(f"Calculation for {vus} VUs getting {data} each")
print(f'Anova stats: {str(stats)}, p_value: {str(p_value)}, Difference: {p_value < stats}')
