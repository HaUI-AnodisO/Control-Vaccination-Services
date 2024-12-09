from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import os
from dotenv import load_dotenv
load_dotenv() 

YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH", "ocr/best.pt")
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", 0.25))
OCR_CONFIG_NAME = os.getenv("OCR_CONFIG_NAME", "vgg_transformer")
OCR_DEVICE = os.getenv("OCR_DEVICE", "cuda")

def load_ocr_model() -> Predictor:
    """Load VietOCR model."""
    config = Cfg.load_config_from_name(OCR_CONFIG_NAME)
    # config['device'] = OCR_DEVICE  # Use GPU if available
    return Predictor(config)
