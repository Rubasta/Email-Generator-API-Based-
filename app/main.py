from fastapi import FastAPI
from pydantic import BaseModel
from .email_service import generate_email

app = FastAPI(title="AI Email Generator")

class EmailRequest(BaseModel):
    recipient: str
    sender_role: str
    purpose: str
    tone: str
    key_points: str
    length: str

@app.post("/generate-email")
def create_email(request: EmailRequest):
    result = generate_email(request.dict())
    return {"email": result}