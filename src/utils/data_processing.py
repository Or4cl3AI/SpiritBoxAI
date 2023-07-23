```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.ai_models.ghost_detection_model import GhostDetectionDataSchema
from src.ai_models.evp_enhancement_model import EVPEnhancementDataSchema
from src.ai_models.paranormal_activity_detection_model import ParanormalActivityDetectionDataSchema

def load_data(data_path):
    """
    Function to load data from the given path
    """
    return pd.read_csv(data_path)

def process_ghost_detection_data(data_path):
    """
    Function to process data for ghost detection model
    """
    data = load_data(data_path)
    data = data[GhostDetectionDataSchema]

    # Normalize the data
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data

def process_evp_enhancement_data(data_path):
    """
    Function to process data for EVP enhancement model
    """
    data = load_data(data_path)
    data = data[EVPEnhancementDataSchema]

    # Normalize the data
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data

def process_paranormal_activity_detection_data(data_path):
    """
    Function to process data for paranormal activity detection model
    """
    data = load_data(data_path)
    data = data[ParanormalActivityDetectionDataSchema]

    # Normalize the data
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data
```