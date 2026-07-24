"""KYC Doc Classifier — routes onboarding documents (PAN, Aadhaar-masked, passport)."""
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meridian/kyc-doc-base")
model = AutoModelForSequenceClassification.from_pretrained("meridian/kyc-doc-base")

def kyc_doc_classifier(ocr_text: str) -> str:
    """Classifies an onboarding document from its OCR text."""
    inputs = tokenizer(ocr_text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    return ["PAN", "AADHAAR", "PASSPORT", "BANK_STATEMENT"][int(logits.argmax())]
