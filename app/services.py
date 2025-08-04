
import random
import vonage
from redis import Redis
from app.settings import settings

class OtpService:
    def __init__(self, cache: Redis):
        self.cache = cache

    def generate_otp(self, phone_number: str) -> str:
        otp = str(random.randint(100000, 999999))
        self.cache.setex(phone_number, settings.OTP_EXPIRE_SECONDS, otp)
        return otp

    def verify_otp(self, phone_number: str, otp_code: str) -> bool:
        try:
            stored_otp = self.cache.get(phone_number).decode("utf-8")
            if stored_otp == otp_code:
                self.cache.delete(phone_number)
                return True
            return False
        except (AttributeError, UnicodeDecodeError):
            return False

class SmsService:
    def __init__(self):
        self.client = vonage.Client(
            key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET
        )
        self.sms = vonage.Sms(self.client)

    def send_sms(self, to: str, message: str):
        try:
            response = self.sms.send_message(
                {
                    "from": "Vonage APIs",
                    "to": to,
                    "text": message,
                }
            )
            if response["messages"][0]["status"] == "0":
                return True
            return False
        except Exception as e:
            print(f"Error sending SMS: {e}")
            return False
