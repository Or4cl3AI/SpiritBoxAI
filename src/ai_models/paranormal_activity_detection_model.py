```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from src.utils.data_processing import processData
from src.config.ai_model_config import ParanormalActivityDetectionModelConfig

class ParanormalActivityDetectionModel:
    def __init__(self):
        self.config = ParanormalActivityDetectionModelConfig()
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()

        model.add(LSTM(self.config.units, input_shape=(self.config.look_back, 1), return_sequences=True))
        model.add(Dropout(self.config.dropout))
        model.add(LSTM(self.config.units, return_sequences=False))
        model.add(Dropout(self.config.dropout))
        model.add(Dense(self.config.output_size))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def train_model(self, trainX, trainY, epochs, batch_size):
        self.model.fit(trainX, trainY, epochs=epochs, batch_size=batch_size)

    def evaluate_model(self, testX, testY):
        score = self.model.evaluate(testX, testY)
        return score

    def predict(self, data):
        processed_data = processData(data, self.config.look_back)
        prediction = self.model.predict(processed_data)
        return prediction

    def save_model(self, model_path):
        self.model.save(model_path)

    def load_model(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
```