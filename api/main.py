from fastapi import FastAPI,File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests as request

app = FastAPI()

MODEL =tf.keras.models.load_model(r'E:\AI Projects\Apple-Plant-Disease-Prediction-Project\saved_model\1\Apple_Plant_Disease_Prediction_model.h5')
CLASS_NAMES = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy']

@app.get("/ping")
async def ping():
    return 'Hello, I am alive!'

def read_file_as_image(data: bytes) -> np.ndarray:
    image=np.array(Image.open(BytesIO(data)))
    return image
     
@app.post("/predict")
async def predict(
    file: UploadFile = File(...)              
    
):
    image =read_file_as_image( await file.read())
    img_batch=np.expand_dims(image, axis=0)  # Add batch dimension
    


    predictions = MODEL.predict(img_batch)
    predicted_index = np.argmax(predictions)
    confidence = float(np.max(predictions) * 100)
    predicted_class = CLASS_NAMES[predicted_index]
    
    return {
        "class": predicted_class,
        "confidence": float(confidence)    
    }
    
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
