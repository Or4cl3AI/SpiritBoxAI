```python
import os
from flask import Flask, request, jsonify
from src.ai_models.paranormal_activity_detection_model import detectParanormalActivity

app = Flask(__name__)

AI_MODEL_PATH = os.getenv('AI_MODEL_PATH')

@app.route('/detect_paranormal_activity', methods=['POST'])
def handle_detect_paranormal_activity():
    data = request.get_json()
    result = detectParanormalActivity(data, AI_MODEL_PATH)
    return jsonify({
        'message': 'PARANORMAL_ACTIVITY_DETECTION_RESULT',
        'data': result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```