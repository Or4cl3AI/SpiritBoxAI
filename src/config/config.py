```python
# src/config/config.py

# Paths
AI_MODEL_PATH = "src/ai_models/"
DATA_PATH = "src/assets/data/"
ASSETS_PATH = "src/assets/"

# Data Schemas
GhostDetectionDataSchema = {
    "type": "object",
    "properties": {
        "image": {"type": "string"},
        "label": {"type": "string"}
    },
    "required": ["image", "label"]
}

EVPEnhancementDataSchema = {
    "type": "object",
    "properties": {
        "audio": {"type": "string"},
        "label": {"type": "string"}
    },
    "required": ["audio", "label"]
}

ParanormalActivityDetectionDataSchema = {
    "type": "object",
    "properties": {
        "sensor_data": {"type": "array"},
        "label": {"type": "string"}
    },
    "required": ["sensor_data", "label"]
}

# DOM Element IDs
ghostDetectionCanvas = "ghostDetectionCanvas"
evpEnhancementPlayer = "evpEnhancementPlayer"
paranormalActivityChart = "paranormalActivityChart"

# Message Names
GHOST_DETECTION_RESULT = "GHOST_DETECTION_RESULT"
EVP_ENHANCEMENT_RESULT = "EVP_ENHANCEMENT_RESULT"
PARANORMAL_ACTIVITY_DETECTION_RESULT = "PARANORMAL_ACTIVITY_DETECTION_RESULT"

# Function Names
detectGhost = "detectGhost"
enhanceEVP = "enhanceEVP"
detectParanormalActivity = "detectParanormalActivity"
collectData = "collectData"
processData = "processData"
visualizeData = "visualizeData"
testModels = "testModels"
configureAIModels = "configureAIModels"
configureInterfaces = "configureInterfaces"
```