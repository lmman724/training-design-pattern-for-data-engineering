import pandas as pd

class UppercaseTransformer:
    def __call__(self, data):
        print("Transforming data to uppercase...")
        data['value'] = data['value'].str.upper()
        return data