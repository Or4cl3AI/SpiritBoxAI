import unittest
from src.interfaces.evp_interface import EVPInterface

class TestEVPInterface(unittest.TestCase):

    def setUp(self):
        self.evp_interface = EVPInterface()

    def test_enhanceEVP(self):
        result = self.evp_interface.enhanceEVP("src/assets/sounds/evp_sample.wav")
        self.assertIsNotNone(result)

    def test_displayEnhancedEVP(self):
        result = self.evp_interface.displayEnhancedEVP("src/assets/sounds/evp_sample.wav")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()