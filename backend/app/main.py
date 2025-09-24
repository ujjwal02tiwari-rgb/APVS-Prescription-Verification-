from fastapi import FastAPI
from .routes import auth, prescriptions, pharmacy, insurance
from .utils.logger import logger

app = FastAPI(
    title="PharmBot AI",
    description="AI-powered prescription digitization and quick-commerce platform",
    version="1.0.0",
)

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(prescriptions.router, prefix="/prescriptions", tags=["Prescriptions"])
app.include_router(pharmacy.router, prefix="/pharmacy", tags=["Pharmacy"])
app.include_router(insurance.router, prefix="/insurance", tags=["Insurance"])

@app.get("/")
def health_check():
    logger.info("Health check called")
    return {"status": "ok", "service": "PharmBot AI"}
