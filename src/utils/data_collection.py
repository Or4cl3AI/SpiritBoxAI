```python
import os
import requests
from src.config.config import DATA_PATH

def download_file(url, filename):
    """
    Helper function to download a file
    """
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def collectData():
    """
    Function to collect data for training and testing the AI models
    """
    # Define the URLs of the data sources
    ghost_detection_data_url = "http://example.com/ghost_detection_data.csv"
    evp_enhancement_data_url = "http://example.com/evp_enhancement_data.csv"
    paranormal_activity_detection_data_url = "http://example.com/paranormal_activity_detection_data.csv"

    # Define the file paths where the data will be saved
    ghost_detection_data_file = os.path.join(DATA_PATH, "ghost_detection_data.csv")
    evp_enhancement_data_file = os.path.join(DATA_PATH, "evp_enhancement_data.csv")
    paranormal_activity_detection_data_file = os.path.join(DATA_PATH, "paranormal_activity_detection_data.csv")

    # Download the data files
    download_file(ghost_detection_data_url, ghost_detection_data_file)
    download_file(evp_enhancement_data_url, evp_enhancement_data_file)
    download_file(paranormal_activity_detection_data_url, paranormal_activity_detection_data_file)
```