from fastapi import APIRouter
from ..services.commerce_service import CommerceService

router = APIRouter()
commerce = CommerceService()

@router.post("/order")
def order_medicine(drug: str, provider: str = "blinkit"):
    return commerce.order_medicine(drug, provider)
