import unittest
from src.ai_models.ai_enhanced_camera import AICamera

class TestAICamera(unittest.TestCase):

    def setUp(self):
        self.ai_camera = AICamera()

    def test_detect_ghost(self):
        # Assuming we have a test image in the data path
        test_image_path = f"{DATA_PATH}/test_image.jpg"
        result = self.ai_camera.detect_ghost(test_image_path)
        self.assertIsInstance(result, dict)
        self.assertIn('ghost_detected', result)

    def test_collect_data(self):
        collected_data = self.ai_camera.collect_data()
        self.assertIsInstance(collected_data, dict)
        self.assertIn('image_data', collected_data)

    def test_process_data(self):
        processed_data = self.ai_camera.process_data()
        self.assertIsInstance(processed_data, dict)
        self.assertIn('processed_image_data', processed_data)

    def test_visualize_data(self):
        visualization_result = self.ai_camera.visualize_data()
        self.assertIsInstance(visualization_result, bool)

    def test_configure_ai_models(self):
        configuration_result = self.ai_camera.configure_ai_models()
        self.assertIsInstance(configuration_result, bool)

if __name__ == '__main__':
    unittest.main()