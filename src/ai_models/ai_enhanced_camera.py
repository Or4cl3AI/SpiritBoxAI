```python
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

AI_MODEL_PATH = "../config/ai_model_config.py"

class AIEnhancedCamera:
    def __init__(self):
        self.model = load_model(AI_MODEL_PATH + '/ai_enhanced_camera_model.h5')

    def detect_ghost(self, image):
        # Preprocess image
        image = cv2.resize(image, (224, 224))
        image = image.astype("float") / 255.0
        image = tf.expand_dims(image, axis=0)

        # Predict ghost presence
        prediction = self.model.predict(image)
        return prediction

    def capture_image(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow('AI Enhanced Camera', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        return frame
```