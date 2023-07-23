```python
# src/config/interface_config.py

# DOM Element IDs
GHOST_DETECTION_CANVAS_ID = "ghostDetectionCanvas"
EVP_ENHANCEMENT_PLAYER_ID = "evpEnhancementPlayer"
PARANORMAL_ACTIVITY_CHART_ID = "paranormalActivityChart"

# Message Names
GHOST_DETECTION_RESULT_MSG = "GHOST_DETECTION_RESULT"
EVP_ENHANCEMENT_RESULT_MSG = "EVP_ENHANCEMENT_RESULT"
PARANORMAL_ACTIVITY_DETECTION_RESULT_MSG = "PARANORMAL_ACTIVITY_DETECTION_RESULT"

# Interface Configuration
INTERFACE_CONFIG = {
    "ghost_detection": {
        "canvas_id": GHOST_DETECTION_CANVAS_ID,
        "result_msg": GHOST_DETECTION_RESULT_MSG
    },
    "evp_enhancement": {
        "player_id": EVP_ENHANCEMENT_PLAYER_ID,
        "result_msg": EVP_ENHANCEMENT_RESULT_MSG
    },
    "paranormal_activity_detection": {
        "chart_id": PARANORMAL_ACTIVITY_CHART_ID,
        "result_msg": PARANORMAL_ACTIVITY_DETECTION_RESULT_MSG
    }
}
```