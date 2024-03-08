from load_csv import load
from pandas import DataFrame
import matplotlib.pyplot as plt

def projection_life_in_relation_to_gdp(life_expectancy, inc_per_person_gdp_inflation):
    """
    @param life_expectancy: DataFrame
    @param inc_per_person_gdp_inflation: DataFrame

    @description: displays the projection of life expectancy in relation to the gross national product of the year 1900 for each country.
    """
    try:
        if isinstance(life_expectancy, DataFrame) == False:
            raise ValueError("Life expectancy is not a DataFrame")
        if isinstance(inc_per_person_gdp_inflation, DataFrame) == False:
            raise ValueError("GDP is not a DataFrame")
        if life_expectancy.shape[0] != inc_per_person_gdp_inflation.shape[0]:
            raise ValueError("The number of countries in the datasets do not match")
        life_expectancy = life_expectancy.dropna()
        inc_per_person_gdp_inflation = inc_per_person_gdp_inflation.dropna()
        life_expectancy = life_expectancy[life_expectancy["year"] == 1900]
        inc_per_person_gdp_inflation = inc_per_person_gdp_inflation[inc_per_person_gdp_inflation["year"] == 1900]
        life_expectancy = life_expectancy[["country", "life_expectancy"]]
        inc_per_person_gdp_inflation = inc_per_person_gdp_inflation[["country", "gdpPercap_1900"]]
        df = life_expectancy.merge(inc_per_person_gdp_inflation, on="country")
        plt.scatter(df["gdpPercap_1900"], df["life_expectancy"])
        plt.xlabel("GDP per capita in 1900")
        plt.ylabel("Life expectancy in 1900")
        plt.show()
    except ValueError as ve:
        print(ve)
    except:
        print("Error displaying projection")


def main():
    life_expectancy = load("life_expectancy_years.csv")
    inc_per_person_gdp_inflation = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    projection_life_in_relation_to_gdp(life_expectancy, inc_per_person_gdp_inflation)


if __name__ == "__main__":
    main()