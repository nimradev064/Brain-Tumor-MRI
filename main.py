from fastapi import FastAPI, File, UploadFile
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
import cv2

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the pre-trained model
model = tf.keras.models.load_model('model.h5')

def preprocess_image(image_path, target_size):
    img = cv2.imread(image_path)
    img = cv2.resize(img, target_size)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        UPLOAD_DIRECTORY = "Static/"
        file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)

        with open(file_location, "wb") as f:
            f.write(file.file.read())

        image = preprocess_image(file_location, (256, 256))
        prediction = model.predict(image)
        label = 'Tumor Detected' if prediction[0][0] > 0.5 else 'No Tumor Detected'
        probability = float(prediction[0][0])
        
        return {"probability": probability, "label": label}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
