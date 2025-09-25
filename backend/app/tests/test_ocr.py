from ..services.ocr_service import OCRService

def test_ocr_extract_text():
    ocr = OCRService()
    result = ocr.extract_text(b"")  # empty bytes
    assert isinstance(result, str)
