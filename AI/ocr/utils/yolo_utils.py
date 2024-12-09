from ultralytics import YOLO
from PIL import Image
from typing import Dict

def load_yolo_model(model_path: str) -> YOLO:
    """Load YOLO model."""
    return YOLO(model_path)

def get_label_map() -> Dict[int, str]:
    """Define label map for YOLO."""
    return {
        0: "adress",
        1: "birth",
        2: "brand",
        3: "gender",
        4: "name",
        5: "phone",
        6: "stamp"
    }
