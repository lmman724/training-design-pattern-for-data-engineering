class ETLPipelines:
    def __init__(self,steps):
        self.steps = steps
    
    def add_step(self, step):
        self.steps.append(step)

    def run(self):
        data = None
        for step in self.steps:
            data = step(data)
        return data

