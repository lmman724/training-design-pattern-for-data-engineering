from etl_pipeline.builder import ETLPipelineBuilder
from etl_pipeline.director import Director

if __name__== "__main__":
    builder = ETLPipelineBuilder()
    director = Director(builder)

    flow = director.construct_pipeline()
    flow()