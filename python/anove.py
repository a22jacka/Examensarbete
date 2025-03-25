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
df = pd.DataFrame({
    "cs": str_to_float(csdf["durationJS"]),
    "go": str_to_float(godf["durationJS"]),   
})

stats, p_value = st.f_oneway(*[df["cs"], df["go"]])
print(f'Anova stats: {str(stats)}, p_value: {str(p_value)}, Difference: {p_value < stats}')
