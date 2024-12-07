from typing import Dict, List, Union
from pydantic import BaseModel

# Output model for the API response
class OCRResult(BaseModel):
    adress: Union[str, List[str]] = None
    birth: Union[str, List[str]] = None
    brand: Union[str, List[str]] = None
    gender: Union[str, List[str]] = None
    name: Union[str, List[str]] = None
    phone: Union[str, List[str]] = None
