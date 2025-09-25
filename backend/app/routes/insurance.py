from fastapi import APIRouter

router = APIRouter()

@router.get("/validate")
def validate_insurance(policy_number: str):
    return {"policy_number": policy_number, "valid": True}
