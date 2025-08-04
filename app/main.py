
from fastapi import FastAPI, Depends, HTTPException, status, Request
from redis import Redis
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.schemas import OtpSendRequest, OtpVerifyRequest, OtpSendResponse, OtpVerifyResponse
from app.services import OtpService, SmsService
from app.settings import settings

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

def get_cache():
    return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

@app.post("/otp/send", response_model=OtpSendResponse)
@limiter.limit("10/minute")
async def send_otp(request: Request, otp_request: OtpSendRequest, cache: Redis = Depends(get_cache)):
    otp_service = OtpService(cache)
    sms_service = SmsService()

    otp = otp_service.generate_otp(otp_request.phone_number)
    message = f"Your OTP is: {otp}"

    if sms_service.send_sms(otp_request.phone_number, message):
        return OtpSendResponse(message="OTP sent successfully")
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send OTP",
        )

@app.post("/otp/verify", response_model=OtpVerifyResponse)
@limiter.limit("10/minute")
async def verify_otp(request: Request, otp_request: OtpVerifyRequest, cache: Redis = Depends(get_cache)):
    otp_service = OtpService(cache)

    if otp_service.verify_otp(otp_request.phone_number, otp_request.otp_code):
        return OtpVerifyResponse(message="OTP verified successfully")
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired OTP"
        )
