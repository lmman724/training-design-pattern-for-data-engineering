from prefect import task
import pandas as pd

@task
def extract():
    print("Extracting data...")
    data = pd.DataFrame({
        "id":[1,2,3],
        "value": ["a", "b", "c"]
    })
    return data

@task
def transform(data):
    print("Transforming data...")
    data['value'] = data['value'].str.upper()
    return data

@task
def load(data):
    print("Loading data...")
    print(data)
