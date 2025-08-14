# 🍏 Apple Plant Disease Detector

This project predicts **Apple Plant Leaf Diseases** using a **Convolutional Neural Network (CNN)** model built with TensorFlow/Keras and served with **FastAPI**.  
Frontend is built using **HTML, CSS, JavaScript** and communicates with the backend API for predictions.

---

## 📂 Project Structure
```
Apple-Plant-Disease-Prediction-Project/
│
├── main.py                         # FastAPI Backend
├── saved_model/                     # Trained Model Files
├── frontend/
│   ├── index.html                    # Frontend UI
│   ├── background.jpg                # Background image
│   └── (other assets)
└── README.md                         # This file
```

---

## 💻 System Requirements
- **Python:** 3.8 or higher  
- **RAM:** Minimum 4GB (8GB+ recommended for training)  
- **GPU:** Optional (recommended for faster training)  
- **Browser:** Chrome, Firefox, or Edge (latest versions)  

---

## 📊 Dataset
- **Source:** [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)  
- **Classes Used:**
  - `Apple___Apple_scab`
  - `Apple___Black_rot`
  - `Apple___Cedar_apple_rust`
  - `Apple___healthy`
- Images resized to **256x256 pixels** for model training.

---

## 🧠 Model Training Summary
1. **Architecture:** CNN with Conv2D, MaxPooling2D, BatchNormalization, Dense layers.  
2. **Optimizer:** Adam (learning rate = 0.001)  
3. **Loss Function:** Categorical Crossentropy  
4. **Training Epochs:** 50 
5. **Accuracy Achieved:** ~97% on validation set  
6. **Saved Model:** `saved_model/1/Apple_Plant_Disease_Prediction_model.h5`  

---

## 🚀 How to Run the Project

### **1️⃣ Backend Setup**
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn tensorflow pillow numpy python-multipart
   ```
2. Start backend server:
   ```bash
   python main.py
   ```
3. If successful, you'll see:
   ```
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
   ```

---

### **2️⃣ Frontend Setup**
1. Open a new terminal.
2. Navigate to frontend:
   ```bash
   cd frontend
   ```
3. Run local server:
   ```bash
   python -m http.server 5500
   ```
4. Open in browser:
   ```
   http://localhost:5500/index.html
   ```

---

## 🌱 Usage
1. Select an **Apple Leaf image** from your device.
2. Click **Predict**.
3. The app shows predicted disease class and confidence score.

---


## 🛠 Tech Stack
- **Backend:** FastAPI, TensorFlow/Keras, Pillow, NumPy
- **Frontend:** HTML, CSS, JavaScript
- **Model:** CNN (Convolutional Neural Network)

---

## 👨‍💻 Author
**Muhammad Uzair**

---

## 📜 License
This project is for **educational and research purposes only**.
