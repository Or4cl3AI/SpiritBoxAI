import unittest
from src.interfaces.paranormal_activity_detection_interface import ParanormalActivityDetectionInterface

class TestParanormalActivityDetectionInterface(unittest.TestCase):

    def setUp(self):
        self.interface = ParanormalActivityDetectionInterface()

    def test_detect_paranormal_activity(self):
        result = self.interface.detectParanormalActivity()
        self.assertIsNotNone(result)

    def test_display_results(self):
        test_data = {"activity_level": 5, "location": "Living Room"}
        self.interface.displayResults(test_data)
        self.assertEqual(self.interface.paranormalActivityChart.data, test_data)

    def test_reset_interface(self):
        self.interface.resetInterface()
        self.assertIsNone(self.interface.paranormalActivityChart.data)

if __name__ == '__main__':
    unittest.main()