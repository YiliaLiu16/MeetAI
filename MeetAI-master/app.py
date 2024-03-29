from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from PIL import Image
import numpy as np
import io
import uvicorn
import base64
# Allow cross-origin requests
from fastapi.middleware.cors import CORSMiddleware

base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gesture2id = {
    'Thumb_Up': 3,
    'Open_Palm': 4,
}

class ImageData(BaseModel):
    image: str

@app.post("/upload")
async def recognize_gesture(image_data: ImageData):
    # Read the image data from base64 string
    base64_str = image_data.image.split(',')[1]
    image_bytes = base64.b64decode(base64_str)
    with open("cached_image.jpg", "wb") as f:
        f.write(image_bytes)
    
    # Convert the image data to a PIL image
    pil_image = Image.open(io.BytesIO(image_bytes))
    pil_image = pil_image.convert("RGB")

    # Convert the PIL image to a numpy array
    image_array = np.array(pil_image)

    # Create a MediaPipe Image object
    mp_image = mp.Image(data=image_array, image_format=mp.ImageFormat.SRGB)

    # Perform gesture recognition using MediaPipe
    recognition_result = recognizer.recognize(mp_image)
    print(recognition_result)
    if len(recognition_result.gestures) == 0:
        return {"emoji": -1}
    else:
        top_gesture = recognition_result.gestures[0][0]
        category_id = gesture2id[top_gesture.category_name] if top_gesture.category_name in gesture2id else -1
        # Return the result
        if category_id == -1:
            return {"gesture": top_gesture.category_name, "confidence": top_gesture.score}
        else:
            return {"emoji": category_id, "confidence": top_gesture.score}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
