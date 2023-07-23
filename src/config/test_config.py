```python
# src/config/test_config.py

# Paths to the test data for each AI model
GHOST_DETECTION_TEST_DATA_PATH = f"{DATA_PATH}/test/ghost_detection"
EVP_ENHANCEMENT_TEST_DATA_PATH = f"{DATA_PATH}/test/evp_enhancement"
PARANORMAL_ACTIVITY_DETECTION_TEST_DATA_PATH = f"{DATA_PATH}/test/paranormal_activity_detection"

# Paths to the expected results for each AI model
GHOST_DETECTION_EXPECTED_RESULTS_PATH = f"{DATA_PATH}/expected_results/ghost_detection"
EVP_ENHANCEMENT_EXPECTED_RESULTS_PATH = f"{DATA_PATH}/expected_results/evp_enhancement"
PARANORMAL_ACTIVITY_DETECTION_EXPECTED_RESULTS_PATH = f"{DATA_PATH}/expected_results/paranormal_activity_detection"

# Test configuration for each AI model
GHOST_DETECTION_TEST_CONFIG = {
    "data_path": GHOST_DETECTION_TEST_DATA_PATH,
    "expected_results_path": GHOST_DETECTION_EXPECTED_RESULTS_PATH,
    "model_path": AI_MODEL_PATH,
}

EVP_ENHANCEMENT_TEST_CONFIG = {
    "data_path": EVP_ENHANCEMENT_TEST_DATA_PATH,
    "expected_results_path": EVP_ENHANCEMENT_EXPECTED_RESULTS_PATH,
    "model_path": AI_MODEL_PATH,
}

PARANORMAL_ACTIVITY_DETECTION_TEST_CONFIG = {
    "data_path": PARANORMAL_ACTIVITY_DETECTION_TEST_DATA_PATH,
    "expected_results_path": PARANORMAL_ACTIVITY_DETECTION_EXPECTED_RESULTS_PATH,
    "model_path": AI_MODEL_PATH,
}
```