
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def mock_sms_service(mocker):
    return mocker.patch("app.services.SmsService.send_sms", return_value=True)

@pytest.fixture
def mock_otp_service(mocker):
    return mocker.patch("app.services.OtpService.verify_otp")

def test_send_otp_success(mock_sms_service):
    response = client.post("/otp/send", json={"phone_number": "+1234567890"})
    assert response.status_code == 200
    assert response.json() == {"message": "OTP sent successfully"}
    mock_sms_service.assert_called_once()

def test_send_otp_failure(mocker):
    mocker.patch("app.services.SmsService.send_sms", return_value=False)
    response = client.post("/otp/send", json={"phone_number": "+1234567890"})
    assert response.status_code == 500
    assert response.json() == {"detail": "Failed to send OTP"}

def test_verify_otp_success(mock_otp_service):
    mock_otp_service.return_value = True
    response = client.post("/otp/verify", json={"phone_number": "+1234567890", "otp_code": "123456"})
    assert response.status_code == 200
    assert response.json() == {"message": "OTP verified successfully"}

def test_verify_otp_failure(mock_otp_service):
    mock_otp_service.return_value = False
    response = client.post("/otp/verify", json={"phone_number": "+1234567890", "otp_code": "123456"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid or expired OTP"}
