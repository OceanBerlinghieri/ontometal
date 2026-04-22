
import os
from etl.repository.resource.csv_resource import CSVResource

class Pipeline():

    def run(self):
        working_dir = os.getcwd()
        csv_resource = CSVResource()

        band_path = os.path.join(working_dir, 'src', 'etl', 'raw', 'metal_bands.csv')
        
        df = csv_resource.load(file_path=band_path, header=1)
        print(df.head())