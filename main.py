from flask import Flask, render_template, request
from tensorflow import keras
import os
import cv2

app = Flask(__name__)
model = keras.models.load_model('space_classification_model.h5')
categories = ['stars', 'galaxies', 'planets', 'cosmos', 'constellation', 'nebula']
upload_folder = 'static/uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        image_path = os.path.join(upload_folder, uploaded_file.filename)
        uploaded_file.save(image_path)
        image = cv2.imread(image_path)
        image = cv2.resize(image, (224, 224))
        image = image / 255.0
        image = image.reshape(1, 224, 224, 3)
        predictions = model.predict(image)
        category_index = predictions.argmax()
        category = categories[category_index]
        return render_template('index.html', prediction=category, selected_file=uploaded_file.filename)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    app.run(debug=True)
