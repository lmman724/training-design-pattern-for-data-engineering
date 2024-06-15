class FilterTransformer:
    def __init__(self, condition):
        self.condition = condition
    def __call__(self, data):
        print("Filtering data...")
        filter_data =data[self.condition(data)]

        return filter_data

    
