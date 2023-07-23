import unittest
from src.interfaces.standard_research_tools_interface import StandardResearchToolsInterface

class TestStandardResearchToolsInterface(unittest.TestCase):

    def setUp(self):
        self.interface = StandardResearchToolsInterface()

    def test_detectGhost(self):
        result = self.interface.detectGhost()
        self.assertIsNotNone(result)

    def test_enhanceEVP(self):
        result = self.interface.enhanceEVP()
        self.assertIsNotNone(result)

    def test_detectParanormalActivity(self):
        result = self.interface.detectParanormalActivity()
        self.assertIsNotNone(result)

    def test_collectData(self):
        result = self.interface.collectData()
        self.assertIsNotNone(result)

    def test_processData(self):
        result = self.interface.processData()
        self.assertIsNotNone(result)

    def test_visualizeData(self):
        result = self.interface.visualizeData()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()