```python
import matplotlib.pyplot as plt
import pandas as pd

def visualizeData(DATA_PATH, GhostDetectionDataSchema, EVPEnhancementDataSchema, ParanormalActivityDetectionDataSchema):
    # Load data
    ghost_detection_data = pd.read_csv(DATA_PATH + 'ghost_detection_data.csv')
    evp_enhancement_data = pd.read_csv(DATA_PATH + 'evp_enhancement_data.csv')
    paranormal_activity_detection_data = pd.read_csv(DATA_PATH + 'paranormal_activity_detection_data.csv')

    # Validate data schema
    assert ghost_detection_data.columns.tolist() == GhostDetectionDataSchema
    assert evp_enhancement_data.columns.tolist() == EVPEnhancementDataSchema
    assert paranormal_activity_detection_data.columns.tolist() == ParanormalActivityDetectionDataSchema

    # Visualize ghost detection data
    plt.figure(figsize=(10, 6))
    plt.title('Ghost Detection Data')
    ghost_detection_data.hist()
    plt.savefig(DATA_PATH + 'ghost_detection_data.png')

    # Visualize EVP enhancement data
    plt.figure(figsize=(10, 6))
    plt.title('EVP Enhancement Data')
    evp_enhancement_data.hist()
    plt.savefig(DATA_PATH + 'evp_enhancement_data.png')

    # Visualize paranormal activity detection data
    plt.figure(figsize=(10, 6))
    plt.title('Paranormal Activity Detection Data')
    paranormal_activity_detection_data.hist()
    plt.savefig(DATA_PATH + 'paranormal_activity_detection_data.png')
```