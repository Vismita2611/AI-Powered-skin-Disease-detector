# AI-Powered-skin-Disease-detector
# Skin Disease Predictor 🩺

A deep learning-based web application that predicts skin diseases from images using a Convolutional Neural Network (CNN). Built with TensorFlow/Keras and deployed as a Flask web app, this project allows users to upload an image of a skin condition and receive a predicted diagnosis instantly.

> ⚠️ **Disclaimer:** This project is intended for educational purposes only. It is **not** a substitute for professional medical diagnosis. Always consult a qualified dermatologist for medical concerns.

---

## 🚀 Features

- 🖼️ Upload a skin image and get an instant prediction
- 🧠 CNN-based image classification model built with TensorFlow/Keras
- 🌐 Simple, user-friendly Flask web interface
- 📊 Displays prediction confidence/probability
- ⚡ Lightweight and easy to run locally

---

## 🏗️ Tech Stack

| Component        | Technology         |
|-------------------|---------------------|
| Language          | Python              |
| Deep Learning     | TensorFlow / Keras  |
| Web Framework     | Flask               |
| Frontend          | HTML, CSS           |
| Model Type        | CNN (Image Classification) |

---

## 📁 Project Structure

```
skin-disease-predictor/
│
├── model/
│   └── skin_disease_model.h5      # Trained CNN model
│
├── static/
│   ├── css/                       # Stylesheets
│   └── uploads/                   # Uploaded images
│
├── templates/
│   ├── index.html                 # Home page
│   └── result.html                # Prediction result page
│
├── app.py                         # Flask application entry point
├── model_training.ipynb           # Notebook used to train the CNN
├── requirements.txt               # Python dependencies
└── README.md
```

---

## 🧠 Model Overview

The model is a Convolutional Neural Network trained on a labeled dataset of skin disease images. It performs the following pipeline:

1. **Preprocessing** – Images are resized, normalized, and augmented for training.
2. **Architecture** – A CNN with multiple convolutional, pooling, and dense layers.
3. **Training** – The model is trained using categorical cross-entropy loss and the Adam optimizer.
4. **Evaluation** – Accuracy and loss are tracked on a validation set.
5. **Export** – The trained model is saved as a `.h5` file for use in the Flask app.

> Update this section with your actual dataset name, number of classes, and model accuracy once finalized.



## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/skin-disease-predictor.git
cd skin-disease-predictor
```

### 2. Create a virtual environment 
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python app.py
```

### 5. Open in browser
Navigate to:
```
http://127.0.0.1:5000/
```

---

## 🖥️ Usage

1. Open the web app in your browser.
2. Upload an image of the skin condition.
3. Click **Predict**.
4. View the predicted disease class along with the confidence score.

---

## 📊 Results

| Metric              | Value        |
|---------------------|--------------|
| Training Accuracy   | 90%          |
| Validation Accuracy | 89%          |
| Test Accuracy       | 90%          |



## 📦 Requirements

Key dependencies (see `requirements.txt` for the full list):

```
tensorflow
flask
numpy
pillow
opencv-python
```

---

## 🔮 Future Improvements

- [ ] Increase dataset size and diversity for better generalization
- [ ] Add Grad-CAM visualizations to explain predictions
- [ ] Deploy the app on cloud platforms (Heroku/Render/AWS)
- [ ] Add multi-language support
- [ ] Improve UI/UX with a more polished frontend

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, open issues, or submit pull requests.

---



## 👤 Author

**Vismita**
Final-year Information Science & Engineering student | Aspiring Software/ML Engineer

- LinkedIn: *[https://www.linkedin.com/in/vismita-mudur-7a43133a3?utm_source=share_via&utm_content=profile&utm_medium=member_android]*
