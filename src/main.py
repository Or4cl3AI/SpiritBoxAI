```python
import os
from ai_models.ghost_detection_model import GhostDetectionModel
from ai_models.evp_enhancement_model import EVPEnhancementModel
from ai_models.paranormal_activity_detection_model import ParanormalActivityDetectionModel
from ai_models.ai_enhanced_camera import AIEnhancedCamera
from interfaces.user_interface import UserInterface
from utils.data_collection import collectData
from utils.data_processing import processData
from utils.data_visualization import visualizeData

# Define paths
AI_MODEL_PATH = os.path.join(os.getcwd(), 'src/ai_models/')
DATA_PATH = os.path.join(os.getcwd(), 'src/assets/data/')
ASSETS_PATH = os.path.join(os.getcwd(), 'src/assets/')

# Initialize models
ghost_detection_model = GhostDetectionModel(AI_MODEL_PATH)
evp_enhancement_model = EVPEnhancementModel(AI_MODEL_PATH)
paranormal_activity_detection_model = ParanormalActivityDetectionModel(AI_MODEL_PATH)
ai_enhanced_camera = AIEnhancedCamera(AI_MODEL_PATH)

# Initialize user interface
user_interface = UserInterface()

# Collect data
collectData(DATA_PATH)

# Process data
processData(DATA_PATH)

# Visualize data
visualizeData(DATA_PATH)

# Run models
ghost_detection_model.detectGhost(ASSETS_PATH)
evp_enhancement_model.enhanceEVP(ASSETS_PATH)
paranormal_activity_detection_model.detectParanormalActivity(ASSETS_PATH)
ai_enhanced_camera.capture(ASSETS_PATH)

# Display results on user interface
user_interface.displayResults(ghost_detection_model, evp_enhancement_model, paranormal_activity_detection_model, ai_enhanced_camera)
```