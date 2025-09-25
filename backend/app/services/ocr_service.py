import pytesseract
from PIL import Image
import io

class OCRService:
    def extract_text(self, image_bytes: bytes) -> str:
        try:
            img = Image.open(io.BytesIO(image_bytes))
            text = pytesseract.image_to_string(img)
            return text.strip()
        except Exception as e:
            return f"OCR Error: {str(e)}"
