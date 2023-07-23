```python
import os
from src.ai_models.ghost_detection_model import detectGhost
from src.ai_models.evp_enhancement_model import enhanceEVP
from src.ai_models.paranormal_activity_detection_model import detectParanormalActivity

class AIInterface:
    def __init__(self):
        self.ai_model_path = os.getenv('AI_MODEL_PATH')

    def load_models(self):
        self.ghost_detection_model = detectGhost(self.ai_model_path)
        self.evp_enhancement_model = enhanceEVP(self.ai_model_path)
        self.paranormal_activity_detection_model = detectParanormalActivity(self.ai_model_path)

    def detect_ghost(self, data):
        return self.ghost_detection_model.predict(data)

    def enhance_evp(self, data):
        return self.evp_enhancement_model.predict(data)

    def detect_paranormal_activity(self, data):
        return self.paranormal_activity_detection_model.predict(data)
```