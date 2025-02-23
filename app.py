from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import joblib
from PIL import Image
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
with open('model.pkl', 'rb') as file:
    model = joblib.load(file)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route for image upload
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if the file is present in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'})

        file = request.files['file']

        # Save the file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess the image (resize, convert to array, etc.)
        image = Image.open(filepath).convert('RGB')
        image = image.resize((224, 224))  # Example: Resize to 224x224
        image_array = np.array(image) / 255.0  # Normalize pixel values
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Make prediction using the model
        prediction = model.predict(image_array)
        prediction_label = "Forged" if prediction[0] > 0.5 else "Authentic"

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction_label})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)