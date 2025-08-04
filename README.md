
# OTP Microservice

This is a simple OTP (One-Time Password) microservice built with FastAPI.

## Prerequisites

- Python 3.7+
- Docker (optional)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/otp-microservice.git
   cd otp-microservice
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## API Endpoints

### 1. Send OTP

- **URL:** `/otp/send`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "phone_number": "+1234567890"
  }
  ```

- **Response:**

  ```json
  {
    "message": "OTP sent successfully"
  }
  ```

### 2. Verify OTP

- **URL:** `/otp/verify`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "phone_number": "+1234567890",
    "otp_code": "123456"
  }
  ```

- **Response:**

  ```json
  {
    "message": "OTP verified successfully"
  }
  ```

## Environment Variables

- `REDIS_HOST`: The hostname of the Redis server.
- `REDIS_PORT`: The port of the Redis server.
- `VONAGE_API_KEY`: Your Vonage API key.
- `VONAGE_API_SECRET`: Your Vonage API secret.

## Usage Examples

### Send OTP

```bash
curl -X POST \
  http://localhost:8000/otp/send \
  -H 'Content-Type: application/json' \
  -d '{
    "phone_number": "+1234567890"
  }'
```

### Verify OTP

```bash
curl -X POST \
  http://localhost:8000/otp/verify \
  -H 'Content-Type: application/json' \
  -d '{
    "phone_number": "+1234567890",
    "otp_code": "123456"
  }'
```
