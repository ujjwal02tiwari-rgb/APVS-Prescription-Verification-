import hashlib

class SignatureService:
    def generate_hash(self, content: str) -> str:
        return hashlib.sha256(content.encode()).hexdigest()
