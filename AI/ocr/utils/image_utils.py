import cv2
import numpy as np
from PIL import Image
from typing import Union

def display_img(cv_img: np.ndarray, title: str = "Image") -> None:
    """Display an OpenCV image."""
    from matplotlib import pyplot as plt
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 8))
    plt.imshow(cv_img)
    plt.title(title)
    plt.axis('off')
    plt.show()

def crop_image(image: Union[Image.Image, np.ndarray], roi: np.ndarray) -> np.ndarray:
    """Crop a region of interest (ROI) from an image."""
    if isinstance(image, Image.Image):
        image = np.array(image)

    x1, y1, x2, y2 = map(int, roi)
    x1 = max(0, min(x1, image.shape[1]))
    y1 = max(0, min(y1, image.shape[0]))
    x2 = max(0, min(x2, image.shape[1]))
    y2 = max(0, min(y2, image.shape[0]))

    return image[y1:y2, x1:x2]

def preprocess_image(img: np.ndarray) -> np.ndarray:
    """Preprocess image for better OCR."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.multiply(gray, 1.5)
    blured1 = cv2.medianBlur(gray, 3)
    blured2 = cv2.medianBlur(gray, 51)
    divided = np.ma.divide(blured1, blured2).data
    normed = np.uint8(255 * divided / divided.max())
    _, threshed = cv2.threshold(normed, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    return threshed
