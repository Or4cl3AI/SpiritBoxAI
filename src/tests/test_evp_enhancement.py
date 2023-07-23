import unittest
from src.ai_models.evp_enhancement_model import enhanceEVP
from src.utils.data_processing import processData
from src.utils.data_collection import collectData

class TestEVPEnhancement(unittest.TestCase):
    def setUp(self):
        self.data_path = DATA_PATH
        self.model_path = AI_MODEL_PATH
        self.evp_data = collectData(self.data_path, EVPEnhancementDataSchema)

    def test_enhanceEVP(self):
        processed_data = processData(self.evp_data)
        enhanced_evp = enhanceEVP(processed_data, self.model_path)
        self.assertIsNotNone(enhanced_evp)

if __name__ == '__main__':
    unittest.main()