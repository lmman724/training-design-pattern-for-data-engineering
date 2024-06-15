from etl_pipeline.pipeline import ETLPipelines
from etl_pipeline.steps.filter_transformer import FilterTransformer
from etl_pipeline.steps.join_transformer import JoinTransformer
from etl_pipeline.steps.uppercase_transformer import UppercaseTransformer

class ETLPipelineBuilder:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)
        return self

    # def add_extractor(self, extractor):
    #     self.steps.add_step(extractor)
    #     return self
    
    def add_filter_transformer(self,condition):
        self.steps.append(FilterTransformer(condition))
        return self
    
    def add_join_transformer(self, join_data, key):
        self.steps.append(JoinTransformer(join_data, key))
        return self
    
    def add_uppercase_transformer(self):
        self.steps.append(UppercaseTransformer())
        return self
    
    # def add_loader(self, loader):
    #     self.steps.append(loader)
    #     return self
    
    def build(self):
        return ETLPipelines(self.steps)

    
    