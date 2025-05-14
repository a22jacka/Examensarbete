import pandas as pd
import glob

headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset","bodyLength"]
files = glob.glob(f"../results/csv/*.csv")
statuses = {
    "2XX": 0,
    "4XX": 0,
    "5XX": 0,
}

def convert_num(n: int) -> str:
    return f"{int(n/100)}XX"

for file in files:
    df = pd.read_csv(file, sep=",", names=headers, low_memory=False, skiprows=[0], index_col=False)
    for i in range(len(df["status"])):
       statuses[convert_num(df["status"][i])] += 1

print("")
print(statuses)
print("")