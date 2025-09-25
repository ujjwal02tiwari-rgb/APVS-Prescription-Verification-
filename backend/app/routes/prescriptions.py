from fastapi import APIRouter, UploadFile, File
from ..schemas.prescription_schema import PrescriptionCreate, PrescriptionResponse
from ..services.ocr_service import OCRService
from ..services.nlp_service import NLPService
from ..services.verification_service import VerificationService

router = APIRouter()
ocr = OCRService()
nlp = NLPService()
verifier = VerificationService()

@router.post("/", response_model=PrescriptionResponse)
async def create_prescription(prescription: PrescriptionCreate, file: UploadFile = File(None)):
    text = ""
    if file:
        content = await file.read()
        text = ocr.extract_text(content)
    else:
        text = prescription.content

    parsed = nlp.parse_prescription(text)
    verified = verifier.verify(parsed)

    return {
        "id": 1,
        "content": f"{text}",
        "verified": verified
    }
