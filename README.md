
# OTP Microservice

This is a simple OTP (One-Time Password) microservice built with FastAPI. It includes API rate limiting and unit tests.

## Features

- Send and verify OTPs.
- API rate limiting (10 requests per minute).
- Ready-to-use scripts for development and testing.

## Prerequisites

- Python 3.7+
- Docker (optional)

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/otp-microservice.git
    cd otp-microservice
    ```

2.  **Run the development server:**

    ```bash
    ./run-start-dev.sh
    ```

## Scripts

This project includes the following scripts to streamline development and testing:

-   `setup-env.sh`: This script creates a Python virtual environment and installs the required dependencies from `requirements.txt`. It is automatically called by the other scripts, so you don't need to run it directly.
-   `run-start-dev.sh`: This script sets up the environment (using `setup-env.sh`) and starts the FastAPI development server with hot-reloading enabled.
-   `run-tests.sh`: This script sets up the environment (using `setup-env.sh`) and runs the unit tests using `pytest`.

## Running Tests

To run the unit tests, use the following command:

```bash
./run-tests.sh
```

This script will set up the test environment and run all the tests in the `tests` directory.

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
- **Method:** `POST
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

## API Rate Limiting

The API has a rate limit of 10 requests per minute per IP address. If you exceed the rate limit, you will receive a `429 Too Many Requests` error.

## Environment Variables

Create a `.env` file in the root of the project and add the following variables:

```
REDIS_HOST=localhost
REDIS_PORT=6379
VONAGE_API_KEY=your_vonage_api_key
VONAGE_API_SECRET=your_vonage_api_secret
```

The application uses `pydantic-settings` to manage environment variables, so it will automatically load them from the `.env` file.

## Usage Examples

### Send OTP

```bash
curl -X POST \
  http://localhost:3555/otp/send \
  -H 'Content-Type: application/json' \
  -d '{
    "phone_number": "+1234567890"
  }'
```

### Verify OTP

```bash
curl -X POST \
  http://localhost:3555/otp/verify \
  -H 'Content-Type: application/json' \
  -d '{
    "phone_number": "+1234567890",
    "otp_code": "123456"
  }'
```
