import pandas as pd

class JoinTransformer:
    def __init__(self, join_data, key):
        self.join_data = join_data
        self.key = key
    def __call__(self, data):
        print("Joining data...")
        join_data = pd.merge(data, self.join_data, on= self.key)
        return join_data