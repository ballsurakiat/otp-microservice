
from pydantic import BaseModel, Field

class OtpSendRequest(BaseModel):
    phone_number: str = Field(..., min_length=10, max_length=15, pattern=r"^\+?[1-9]\d{1,14}$")

class OtpVerifyRequest(BaseModel):
    phone_number: str = Field(..., min_length=10, max_length=15, pattern=r"^\+?[1-9]\d{1,14}$")
    otp_code: str = Field(..., min_length=6, max_length=6)

class OtpSendResponse(BaseModel):
    message: str

class OtpVerifyResponse(BaseModel):
    message: str
