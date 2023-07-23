import unittest
from src.interfaces.camera_interface import CameraInterface

class TestCameraInterface(unittest.TestCase):
    def setUp(self):
        self.camera_interface = CameraInterface()

    def test_initialization(self):
        self.assertIsInstance(self.camera_interface, CameraInterface)

    def test_capture_image(self):
        image = self.camera_interface.capture_image()
        self.assertIsNotNone(image)

    def test_start_video_capture(self):
        self.camera_interface.start_video_capture()
        self.assertTrue(self.camera_interface.is_video_capturing)

    def test_stop_video_capture(self):
        self.camera_interface.stop_video_capture()
        self.assertFalse(self.camera_interface.is_video_capturing)

if __name__ == '__main__':
    unittest.main()