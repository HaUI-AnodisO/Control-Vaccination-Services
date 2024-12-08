import re

def clean_text(text: str) -> str:
    """Clean text to remove invalid dots."""
    cleaned_text = text.replace('.', '')
    return cleaned_text
