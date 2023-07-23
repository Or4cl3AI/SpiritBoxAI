import unittest
from src.interfaces.user_interface import UserInterface

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.ui = UserInterface()

    def test_detectGhost(self):
        result = self.ui.detectGhost()
        self.assertIsNotNone(result, "Failed to detect ghost")

    def test_enhanceEVP(self):
        result = self.ui.enhanceEVP()
        self.assertIsNotNone(result, "Failed to enhance EVP")

    def test_detectParanormalActivity(self):
        result = self.ui.detectParanormalActivity()
        self.assertIsNotNone(result, "Failed to detect paranormal activity")

    def test_collectData(self):
        result = self.ui.collectData()
        self.assertIsNotNone(result, "Failed to collect data")

    def test_processData(self):
        result = self.ui.processData()
        self.assertIsNotNone(result, "Failed to process data")

    def test_visualizeData(self):
        result = self.ui.visualizeData()
        self.assertIsNotNone(result, "Failed to visualize data")

    def test_configureAIModels(self):
        result = self.ui.configureAIModels()
        self.assertIsNotNone(result, "Failed to configure AI models")

    def test_configureInterfaces(self):
        result = self.ui.configureInterfaces()
        self.assertIsNotNone(result, "Failed to configure interfaces")

if __name__ == '__main__':
    unittest.main()