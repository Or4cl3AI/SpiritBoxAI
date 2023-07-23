```python
# AI Model Configuration

AI_MODEL_PATH = {
    'ghost_detection': 'src/ai_models/ghost_detection_model.py',
    'evp_enhancement': 'src/ai_models/evp_enhancement_model.py',
    'paranormal_activity_detection': 'src/ai_models/paranormal_activity_detection_model.py',
    'ai_enhanced_camera': 'src/ai_models/ai_enhanced_camera.py',
    'standard_research_tools': 'src/ai_models/standard_research_tools.py',
    'advanced_research_tools': 'src/ai_models/advanced_research_tools.py'
}

DATA_PATH = {
    'ghost_detection': 'src/assets/data/ghost_detection_data.csv',
    'evp_enhancement': 'src/assets/data/evp_enhancement_data.csv',
    'paranormal_activity_detection': 'src/assets/data/paranormal_activity_detection_data.csv'
}

DATA_SCHEMA = {
    'ghost_detection': 'GhostDetectionDataSchema',
    'evp_enhancement': 'EVPEnhancementDataSchema',
    'paranormal_activity_detection': 'ParanormalActivityDetectionDataSchema'
}

# Function names
FUNCTION_NAMES = {
    'detect_ghost': 'detectGhost',
    'enhance_evp': 'enhanceEVP',
    'detect_paranormal_activity': 'detectParanormalActivity',
    'collect_data': 'collectData',
    'process_data': 'processData',
    'visualize_data': 'visualizeData',
    'test_models': 'testModels',
    'configure_ai_models': 'configureAIModels',
    'configure_interfaces': 'configureInterfaces'
}
```