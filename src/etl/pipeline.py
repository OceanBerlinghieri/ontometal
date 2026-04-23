import os
from etl.repository.resource.csv_resource import CSVResource


class Pipeline:
    def __init__(self, band_repository):
        self.band_repository = band_repository

    def run(self):
        working_dir = os.getcwd()
        bands = self.band_repository.get_bands(
            path=os.path.join(working_dir, "src/etl/raw", "metal_bands.csv")
        )

        print(bands.head())
