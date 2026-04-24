from pandas import DataFrame


class CountryNormalization:
    def __init__(self):
        pass

    # TODO: Get country ISO codes, map country names to ISO codes, 
    # handle edge cases (e.g., "USA" -> "United States", "UK" -> "United Kingdom")
    def normalize(self, df: DataFrame) -> DataFrame:
        return df