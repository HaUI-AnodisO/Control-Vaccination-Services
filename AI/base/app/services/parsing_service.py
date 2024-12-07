def parse_string_to_json(input_string: str) -> dict:
    lines = input_string.split("\n")
    return {
        "full_name": lines[0].strip() if len(lines) > 0 else "",
        "date_of_birth": lines[1].strip() if len(lines) > 1 else "",
        "id_card_number": lines[2].strip() if len(lines) > 2 else "",
        "gender": lines[3].strip() if len(lines) > 3 else "",
        "address": lines[4].strip() if len(lines) > 4 else "",
    }
