class VerificationService:
    def verify(self, prescription_data: dict) -> bool:
        
        return prescription_data.get("drug") != "Unknown"
