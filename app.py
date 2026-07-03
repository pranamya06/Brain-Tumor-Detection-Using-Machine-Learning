import tensorflow as tf
from flask import Flask, render_template, request
import numpy as np
import cv2

app = Flask(__name__,template_folder='template')
#model = tf.keras.models.load_model('braintumortest.h5')
model = None 
#tf.compat.v1.disable_eager_execution() 

def load_model():
    global model
    model = tf.keras.models.load_model('braintumortest.h5')
    
@app.before_first_request
def before_first_request():
    load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return 'Model not loaded'
    
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (150, 150))
    img_array = np.array(img)
    img_array = img_array.reshape(1, 150, 150, 3)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    classes = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']
    result = classes[class_idx]
    return result

if __name__ == '__main__':
    app.run(debug=True)
