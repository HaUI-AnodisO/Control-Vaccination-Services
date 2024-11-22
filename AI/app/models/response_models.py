from pydantic import BaseModel
from typing import Optional

class ResponseData(BaseModel):
    raw_text: str
    markdown: str
    json_data: dict

class ParsedData(BaseModel):
    full_name: str
    date_of_birth: str
    id_card_number: str
    gender: str
    address: Optional[str] = None
