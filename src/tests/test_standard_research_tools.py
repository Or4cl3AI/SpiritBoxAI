import unittest
from src.ai_models.standard_research_tools import StandardResearchTools

class TestStandardResearchTools(unittest.TestCase):

    def setUp(self):
        self.standard_tools = StandardResearchTools()

    def test_detectGhost(self):
        result = self.standard_tools.detectGhost()
        self.assertIsNotNone(result, "Failed to detect ghost")

    def test_enhanceEVP(self):
        result = self.standard_tools.enhanceEVP()
        self.assertIsNotNone(result, "Failed to enhance EVP")

    def test_detectParanormalActivity(self):
        result = self.standard_tools.detectParanormalActivity()
        self.assertIsNotNone(result, "Failed to detect paranormal activity")

    def test_collectData(self):
        result = self.standard_tools.collectData()
        self.assertIsNotNone(result, "Failed to collect data")

    def test_processData(self):
        result = self.standard_tools.processData()
        self.assertIsNotNone(result, "Failed to process data")

    def test_visualizeData(self):
        result = self.standard_tools.visualizeData()
        self.assertIsNotNone(result, "Failed to visualize data")

if __name__ == '__main__':
    unittest.main()