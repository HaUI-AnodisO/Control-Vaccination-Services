from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg

def load_ocr_model() -> Predictor:
    """Load VietOCR model."""
    config = Cfg.load_config_from_name('vgg_transformer')
    config['device'] = 'cuda'  # Use GPU if available
    return Predictor(config)
