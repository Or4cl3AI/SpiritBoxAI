```python
import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

AI_MODEL_PATH = os.getenv('AI_MODEL_PATH')
DATA_PATH = os.getenv('DATA_PATH')

class GhostDetectionDataSchema:
    def __init__(self):
        self.image_height = 128
        self.image_width = 128
        self.channels = 3

def build_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(GhostDetectionDataSchema().image_height, GhostDetectionDataSchema().image_width, GhostDetectionDataSchema().channels)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    model = build_model()

    train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)

    training_set = train_datagen.flow_from_directory(DATA_PATH + '/training_set', target_size=(GhostDetectionDataSchema().image_height, GhostDetectionDataSchema().image_width), batch_size=32, class_mode='binary')
    test_set = test_datagen.flow_from_directory(DATA_PATH + '/test_set', target_size=(GhostDetectionDataSchema().image_height, GhostDetectionDataSchema().image_width), batch_size=32, class_mode='binary')

    model.fit(training_set, steps_per_epoch=len(training_set), epochs=50, validation_data=test_set, validation_steps=len(test_set))

    model.save(AI_MODEL_PATH + '/ghost_detection_model.h5')

def detectGhost(image_path):
    model = tf.keras.models.load_model(AI_MODEL_PATH + '/ghost_detection_model.h5')
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(GhostDetectionDataSchema().image_height, GhostDetectionDataSchema().image_width))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, axis=0)

    result = model.predict(image)
    return result[0][0]
```