from pandas import DataFrame

from etl.entities.country import Country


class CountryNormalization:
    def __init__(self):
        pass

    # TODO: Get country ISO codes, map country names to ISO codes, 
    # handle edge cases (e.g., "USA" -> "United States", "UK" -> "United Kingdom")
    def normalize(self, countries: DataFrame) -> DataFrame:
        normalized_countries = []
        for _, country in countries.iterrows():
            normalized_countries.append(Country(name=country['Country']))
        
        result = DataFrame([vars(c) for c in normalized_countries])
        return result
