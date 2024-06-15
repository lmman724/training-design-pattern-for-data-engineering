from .steps.extractor import Extractor
from .steps.loader import Loader
import pandas as pd

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_pipeline_with_filters(self):
        self.builder.add_step(Extractor()) \
            .add_filter_transformer(lambda df: df["value"].str.contains("a")) \
            .add_uppercase_transformer() \
            .add_step(Loader())
        return self.builder.build()
    
    # def construct_pipeline(self):
    #     join_data = pd.DataFrame({
    #         "id":[1,2],
    #         "extra": ['data1', 'data2']

    #     })
    #     self.builder.add_step(Extractor()) \
    #         .add_join_transformer(join_data, "id") \
    #         .add_step(Loader())
    #     return self.builder.build()
    
