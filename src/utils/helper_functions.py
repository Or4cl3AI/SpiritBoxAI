```python
import os
import json
import numpy as np
from sklearn.model_selection import train_test_split

AI_MODEL_PATH = os.getenv('AI_MODEL_PATH')
DATA_PATH = os.getenv('DATA_PATH')
ASSETS_PATH = os.getenv('ASSETS_PATH')

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def split_data(data, test_size=0.2, random_state=42):
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    return train_data, test_data

def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def denormalize_data(data, min_value, max_value):
    return data * (max_value - min_value) + min_value

def load_model(model_name):
    model_path = os.path.join(AI_MODEL_PATH, model_name)
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        raise Exception(f'Model {model_name} not found at {model_path}')

def save_model(model, model_name):
    model_path = os.path.join(AI_MODEL_PATH, model_name)
    joblib.dump(model, model_path)

def load_asset(asset_name):
    asset_path = os.path.join(ASSETS_PATH, asset_name)
    if os.path.exists(asset_path):
        return asset_path
    else:
        raise Exception(f'Asset {asset_name} not found at {asset_path}')
```