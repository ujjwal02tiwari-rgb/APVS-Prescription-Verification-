class CommerceService:
    def order_medicine(self, drug_name: str, provider: str = "blinkit"):
        
        return {"status": "order placed", "provider": provider, "drug": drug_name}
