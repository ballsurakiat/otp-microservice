#!/bin/bash

# Source the setup script
source "$(dirname "$0")/setup-env.sh"

# Run the development server
echo "Starting development server..."
uvicorn app.main:app --host 0.0.0.0 --port 3555 --reload