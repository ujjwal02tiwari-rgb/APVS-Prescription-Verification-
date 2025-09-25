from ..services.verification_service import VerificationService

def test_verification_service():
    verifier = VerificationService()
    assert verifier.verify({"drug": "Paracetamol"})
    assert not verifier.verify({"drug": "Unknown"})
