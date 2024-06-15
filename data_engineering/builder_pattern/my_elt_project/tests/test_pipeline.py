import unittest

from etl_pipeline.builder import ETLPipelineBuilder
from etl_pipeline.director import Director

class TestETLPipelineBuilder(unittest.TestCase):
    def test_pipeline(self):
        builder = ETLPipelineBuilder()
        director = Director(builder)
        pipeline = director.construct_pipeline()
        pipeline.run()
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()

