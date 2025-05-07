import pandas
import glob

def str_to_float(column: pandas.DataFrame) -> list[float]:
    return [float(point) for point in column]

def combine_average_of_dataframes(column: str, frames: list[pandas.DataFrame]) -> list[float]:
    if (len(frames) == 0): 
        return pandas.DataFrame.empty
    
    points = []
    print(len(frames[0][column]))
    length = len(frames[0][column])
    for point in range(length):
        sum = 0
        for frame in frames:
            sum += frame[column][point]
        points.append(sum/len(frames))

    return points


files = glob.glob(f"../pilot-study-results/csv/*get*10vu*.csv")
headers = ["testId","status","startTime","endTime","durationJS","durationK6","vus","limit","offset"]
dataFrames = []
for file in files:
    dataFrames.append(pandas.read_csv(file, sep=",", names=headers, low_memory=False, skiprows=[0]))
average_points = combine_average_of_dataframes("durationJS", dataFrames)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,5))
plt.plot(
    range(0, 2000),
    combine_average_of_dataframes("durationJS", dataFrames),
    color="blue",
    label="average value of points"
)
plt.xticks(range(0, 2001, 100))
plt.yticks(range(0, 100, 10))
plt.show()