```python
import cv2
from src.ai_models.ai_enhanced_camera import AIEnhancedCamera

class CameraInterface:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.ai_camera = AIEnhancedCamera()

    def capture_frame(self):
        ret, frame = self.camera.read()
        return ret, frame

    def process_frame(self, frame):
        processed_frame = self.ai_camera.process_frame(frame)
        return processed_frame

    def display_frame(self, frame):
        cv2.imshow('AI Enhanced Camera', frame)

    def release_camera(self):
        self.camera.release()

    def run(self):
        while True:
            ret, frame = self.capture_frame()
            if ret:
                processed_frame = self.process_frame(frame)
                self.display_frame(processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.release_camera()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_interface = CameraInterface()
    camera_interface.run()
```