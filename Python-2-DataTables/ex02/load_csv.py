import pandas as pd
from pandas import DataFrame

def load(path: str) -> DataFrame:
    """
    @param path: str
    @return: DataFrame

    @description: Load and print the dimensions of the dataset from the given path.
    """
    try:
        if isinstance(path, str) == False:
            raise ValueError("Path is not a string")
        if path[-4:] != ".csv":
            raise ValueError("Path is not a .csv file")
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except:
        print("Error loading dataset")
        return None

def main():
    file_path = "population_total.csv"
    print(load(file_path))

if __name__ == "__main__":
    main()
