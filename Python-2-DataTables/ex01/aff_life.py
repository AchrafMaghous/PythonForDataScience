import matplotlib.pyplot as plt
from load_csv import load
from pandas import DataFrame


def show_graph_of_morocco(dataFrame: DataFrame):
    """
    @param dataFrame: DataFrame
    @return: None

    @description: Show a graph of the life expectancy in corresponding campus in Morocco.
    """
    try:
        if isinstance(dataFrame, DataFrame) == False:
            raise ValueError("Data is not a DataFrame")
        if "Morocco" not in dataFrame["country"].values:
            raise ValueError("Morocco is not in the dataset")
        morocco = dataFrame[dataFrame["country"] == "Morocco"]
        years = morocco.columns[1:]
        life_expectancy_years = morocco.values[0][1:]
        
        # Convert years to strings
        years = [str(year) for year in years]
        
        plt.plot(years, life_expectancy_years)
        plt.title("Morocco Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        
        # Set the x-axis ticks
        plt.xticks(range(0, len(years), 40))
        
        plt.show()
    except Exception as e:
        print("Error showing graph", e)

def main():
    show_graph_of_morocco(load("life_expectancy_years.csv"))

if __name__ == "__main__":
    main()