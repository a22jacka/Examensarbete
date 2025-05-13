import scipy.stats as st
import pandas as pd
import glob
from misc import str_to_float

PATH_TO_SRC = "../pilot-study-results/csv/"
PATH_TO_SAVE = "../pilot-study-results/graphs/"

#vus = 10
#data = "1MB"
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset","bodyLength"]

for IS_GET in range(2):
    for vus in [10, 50, 100]:
        for data in ["10kB", "100kB", "1MB"]:
            rows_to_skip = vus * 2 + 1
            # combines a specified column from 2 files into one dataframe
            csdf = pd.read_csv(glob.glob(f"{PATH_TO_SRC}asp-{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.csv")[0], sep=",", header=None, names=headers, low_memory=False, skiprows=rows_to_skip, index_col=False)
            godf = pd.read_csv(glob.glob(f"{PATH_TO_SRC}echo-{("get" if IS_GET else "post")}-{vus}vu{(f"-{data}" if IS_GET else "")}.csv")[0], sep=",", header=None, names=headers, low_memory=False, skiprows=rows_to_skip, index_col=False )
            df = pd.DataFrame({
                "ASP.NET Core": str_to_float(csdf["durationJS"]),
                "Echo": str_to_float(godf["durationJS"]),
            })
            stats, p_value = st.f_oneway(df["ASP.NET Core"], df["Echo"])
            print(f"Calculation for {vus} VUs {"GET" if IS_GET else "POST"}ing {data if IS_GET else ""}")
            print(f'Anova stats: {str(stats)}, p_value: {str(p_value)}, Difference: {p_value < stats}\n')