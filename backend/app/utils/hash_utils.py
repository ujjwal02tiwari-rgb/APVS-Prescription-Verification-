import hashlib

def hash_string(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()
