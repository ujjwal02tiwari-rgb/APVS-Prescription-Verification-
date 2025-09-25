from fastapi import APIRouter
from ..schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    # Dummy user response
    return {"id": 1, "email": user.email, "role": user.role}
