import pytest
from app.services.parsing_service import parse_string_to_json

def test_parse_string_to_json():
    input_string = '''Nguyễn Văn A
    01/01/1990
    123456789
    Nam
    123 Đường ABC, Quận XYZ, TP. Hồ Chí Minh'''
    
    result = parse_string_to_json(input_string)
    
    assert result["full_name"] == "Nguyễn Văn A"
    assert result["date_of_birth"] == "01/01/1990"
    assert result["id_card_number"] == "123456789"
    assert result["gender"] == "Nam"
    assert result["address"] == "123 Đường ABC, Quận XYZ, TP. Hồ Chí Minh"
