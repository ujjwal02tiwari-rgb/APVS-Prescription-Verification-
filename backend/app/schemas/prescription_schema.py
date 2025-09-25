from pydantic import BaseModel

class PrescriptionCreate(BaseModel):
    doctor_id: int
    patient_id: int
    content: str

class PrescriptionResponse(BaseModel):
    id: int
    content: str
    verified: bool

    class Config:
        orm_mode = True
