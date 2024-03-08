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
    print(load("life_expectancy_years.csv"))
    print(load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))

if __name__ == "__main__":
    main()
