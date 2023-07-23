import unittest
from src.interfaces.ai_interface import AIInterface

class TestAIInterface(unittest.TestCase):

    def setUp(self):
        self.ai_interface = AIInterface()

    def test_detectGhost(self):
        result = self.ai_interface.detectGhost()
        self.assertIsNotNone(result, "Failed to detect ghost")

    def test_enhanceEVP(self):
        result = self.ai_interface.enhanceEVP()
        self.assertIsNotNone(result, "Failed to enhance EVP")

    def test_detectParanormalActivity(self):
        result = self.ai_interface.detectParanormalActivity()
        self.assertIsNotNone(result, "Failed to detect paranormal activity")

    def test_configureAIModels(self):
        result = self.ai_interface.configureAIModels()
        self.assertTrue(result, "Failed to configure AI models")

if __name__ == '__main__':
    unittest.main()