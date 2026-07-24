"""PII masking helpers shared by services."""
import re

def mask_pan(text: str) -> str:
    return re.sub(r"[A-Z]{5}[0-9]{4}[A-Z]", "*****####*", text)
