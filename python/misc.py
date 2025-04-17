import pandas
def str_to_float(column: pandas.DataFrame) -> list[float]:
        return [float(point) for point in column]