import pandas as pd

class Extractor:
    def __call__(self,_):
        print("Extracting data...")
        data = pd.DataFrame({
            "id": [1, 2, 3],
            "value" : ["a", "b", "c"]
        })
        return data
