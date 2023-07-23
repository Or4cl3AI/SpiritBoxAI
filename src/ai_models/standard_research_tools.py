```python
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

AI_MODEL_PATH = os.getenv('AI_MODEL_PATH')

class StandardResearchTools:
    def __init__(self):
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=2)

    def load_data(self, filename):
        data_path = os.path.join(AI_MODEL_PATH, filename)
        data = np.load(data_path)
        return data

    def standardize_data(self, data):
        standardized_data = self.scaler.fit_transform(data)
        return standardized_data

    def reduce_dimensionality(self, data):
        reduced_data = self.pca.fit_transform(data)
        return reduced_data

    def preprocess_data(self, filename):
        data = self.load_data(filename)
        standardized_data = self.standardize_data(data)
        reduced_data = self.reduce_dimensionality(standardized_data)
        return reduced_data
```