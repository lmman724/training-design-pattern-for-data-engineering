from etl_pipeline.builder import ETLPipelineBuilder

from etl_pipeline.director import Director

if __name__ == "__main__":
    builder = ETLPipelineBuilder()
    director = Director(builder)

    print("Running pipeline with filter:")
    pipeline_with_filter = director.construct_pipeline_with_filters()
    pipeline_with_filter.run()