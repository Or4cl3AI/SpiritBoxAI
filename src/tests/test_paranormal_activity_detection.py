import unittest
from src.ai_models.paranormal_activity_detection_model import ParanormalActivityDetectionModel
from src.utils.data_processing import processData
from src.config.ai_model_config import AI_MODEL_PATH, DATA_PATH

class TestParanormalActivityDetection(unittest.TestCase):
    def setUp(self):
        self.model = ParanormalActivityDetectionModel(AI_MODEL_PATH + "/paranormal_activity_detection_model")
        self.data = processData(DATA_PATH + "/paranormal_activity_data")

    def test_detect_paranormal_activity(self):
        result = self.model.detectParanormalActivity(self.data)
        self.assertIsInstance(result, dict)
        self.assertIn('PARANORMAL_ACTIVITY_DETECTION_RESULT', result)

    def test_model_accuracy(self):
        accuracy = self.model.evaluate_accuracy(self.data)
        self.assertGreaterEqual(accuracy, 0.8)

if __name__ == '__main__':
    unittest.main()