class NLPService:
    def parse_prescription(self, text: str):
        # Very simple parsing (placeholder for NLP model)
        if "Paracetamol" in text:
            return {"drug": "Paracetamol", "dosage": "500mg", "frequency": "2 per day"}
        return {"drug": "Unknown", "dosage": "", "frequency": ""}
