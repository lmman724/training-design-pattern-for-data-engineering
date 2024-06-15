import unittest

from prefect_workflow.builder import ETLPipelineBuilder
from prefect_workflow.director import Director
# from prefect_workflow.tasks import extract, transform, load

class TestETLPipelineBuilder(unittest.TestCase):
    def test_pipeline(self):
        builder = ETLPipelineBuilder()
        director = Director(builder)
        flow = director.construct_pipeline()
        state = flow.run()
        self.assertTrue(state.is_successful())

if __name__ == "__main__":
    unittest.main()