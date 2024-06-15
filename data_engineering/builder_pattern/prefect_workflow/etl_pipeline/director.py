# director.py
from etl_pipeline.tasks import extract, transform, load

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_pipeline(self):
        self.builder.add_task(extract) \
                    .add_task(transform) \
                    .add_task(load)
        return self.builder.build()
