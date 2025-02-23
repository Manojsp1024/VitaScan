**Overview**
Image Forgery Detection is a deep learning-based system designed to detect tampered or forged images. The project utilizes feature extraction techniques such as Histogram of Oriented Gradients (HOG) and Local Binary Patterns (LBP), and a trained model to classify images as tampered or authentic.

**Features**
Detects tampering in images using deep learning.
Utilizes HOG and LBP feature extraction.
Web-based interface for easy image upload and analysis.
Backend API for model inference.

**Project Structure**
Frontend: UI with HTML, CSS, and JavaScript.
Backend: Flask/Django/FastAPI-based API.
Model: Pre-trained machine learning model for forgery detection.
Data: Sample test images.
Notebooks: Jupyter notebooks for experimentation.

**Installation & Usage**

Clone Repository: git clone 
Setup Virtual Environment & Install Dependencies:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Run Backend: python app.py (Starts at http://127.0.0.1:5000/)
Open Frontend: Load frontend/i.html in a browser to upload and analyze images.
