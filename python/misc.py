import pandas
def str_to_float(lst: pandas.DataFrame) -> list[float]:
        return [float(point) for point in lst]