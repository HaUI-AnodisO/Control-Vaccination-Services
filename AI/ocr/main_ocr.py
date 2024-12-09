# Copyright 2024 HaUI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fastapi import FastAPI, UploadFile, HTTPException, APIRouter
from PIL import Image
from ocr.models import OCRResult
from ocr.utils.image_utils import crop_image, preprocess_image
from ocr.utils.ocr_utils import clean_text
from ocr.utils.yolo_utils import load_yolo_model, get_label_map
from ocr.config import load_ocr_model, YOLO_MODEL_PATH, CONFIDENCE_THRESHOLD
import numpy as np
import json

app = APIRouter()

# Load YOLO and OCR models
yolo_model = load_yolo_model(YOLO_MODEL_PATH)
ocr_model = load_ocr_model()
label_map = get_label_map()

@app.post("/process-image", response_model=OCRResult)
async def process_image(file: UploadFile):
    """Process the uploaded image and return extracted OCR data."""
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

    # Load image
    image = Image.open(file.file)
    result = yolo_model.predict(image, conf=CONFIDENCE_THRESHOLD)[0]

    # Prepare result dictionary
    result_dict = {}

    for r, cls in zip(result.boxes.xyxy, result.boxes.cls):
        label = label_map[int(cls)]

        if label == "stamp":  # Skip "stamp" label
            continue

        # Crop and preprocess image
        crop_img = crop_image(image, r)
        crop_img = preprocess_image(crop_img)

        # Convert to PIL for OCR
        if isinstance(crop_img, np.ndarray):
            crop_img = Image.fromarray(crop_img)

        text = ocr_model.predict(crop_img)  # Perform OCR
        text = clean_text(text)  # Clean text

        if label in result_dict:
            if isinstance(result_dict[label], list):
                result_dict[label].append(text)
            else:
                result_dict[label] = [result_dict[label], text]
        else:
            result_dict[label] = text

    return OCRResult(**result_dict)
