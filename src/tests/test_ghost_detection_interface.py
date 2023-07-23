import unittest
from src.interfaces.ghost_detection_interface import GhostDetectionInterface

class TestGhostDetectionInterface(unittest.TestCase):

    def setUp(self):
        self.interface = GhostDetectionInterface()

    def test_detectGhost(self):
        result = self.interface.detectGhost()
        self.assertIsNotNone(result)

    def test_displayGhostDetectionResult(self):
        test_result = {"GHOST_DETECTION_RESULT": True}
        self.interface.displayGhostDetectionResult(test_result)
        self.assertEqual(self.interface.ghostDetectionCanvas.get('text'), 'Ghost Detected')

    def test_resetInterface(self):
        self.interface.resetInterface()
        self.assertEqual(self.interface.ghostDetectionCanvas.get('text'), '')

if __name__ == '__main__':
    unittest.main()