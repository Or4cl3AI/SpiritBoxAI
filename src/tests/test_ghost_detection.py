import unittest
from src.ai_models.ghost_detection_model import GhostDetectionModel
from src.utils.data_processing import processData
from src.config.ai_model_config import AI_MODEL_PATH, GhostDetectionDataSchema

class TestGhostDetection(unittest.TestCase):
    def setUp(self):
        self.model = GhostDetectionModel(AI_MODEL_PATH)
        self.data_schema = GhostDetectionDataSchema

    def test_detect_ghost(self):
        # Load and process the test data
        test_data = processData('src/assets/data/test_ghost_data.csv', self.data_schema)

        for data in test_data:
            # Run the ghost detection model
            result = self.model.detectGhost(data)

            # Check if the result is in the expected format
            self.assertIsInstance(result, dict)
            self.assertIn('probability', result)
            self.assertIn('label', result)

            # Check if the probability is a float between 0 and 1
            self.assertIsInstance(result['probability'], float)
            self.assertGreaterEqual(result['probability'], 0)
            self.assertLessEqual(result['probability'], 1)

            # Check if the label is a string
            self.assertIsInstance(result['label'], str)

if __name__ == '__main__':
    unittest.main()