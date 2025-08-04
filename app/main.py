
from fastapi import FastAPI, Depends, HTTPException, status
from redis import Redis
from app.schemas import OtpSendRequest, OtpVerifyRequest, OtpSendResponse, OtpVerifyResponse
from app.services import OtpService, SmsService
from app.settings import settings

app = FastAPI()

def get_cache():
    return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

@app.post("/otp/send", response_model=OtpSendResponse)
async def send_otp(request: OtpSendRequest, cache: Redis = Depends(get_cache)):
    otp_service = OtpService(cache)
    sms_service = SmsService()

    otp = otp_service.generate_otp(request.phone_number)
    message = f"Your OTP is: {otp}"

    if sms_service.send_sms(request.phone_number, message):
        return OtpSendResponse(message="OTP sent successfully")
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP",
        )

@app.post("/otp/verify", response_model=OtpVerifyResponse)
async def verify_otp(request: OtpVerifyRequest, cache: Redis = Depends(get_cache)):
    otp_service = OtpService(cache)

    if otp_service.verify_otp(request.phone_number, request.otp_code):
        return OtpVerifyResponse(message="OTP verified successfully")
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired OTP"
        )
