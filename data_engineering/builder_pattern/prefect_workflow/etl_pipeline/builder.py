from prefect import Flow,flow

class ETLPipelineBuilder:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        return self
    
    def build(self):
        @flow(name="simple ETL pipeline")
        def flow_fn():
            data = self.tasks[0]()
            for task in self.tasks[1:]:
                data = task(data)
            return data
        return flow_fn