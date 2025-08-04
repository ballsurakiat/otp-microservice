#!/bin/bash

# Source the setup script
source "$(dirname "$0")/setup-env.sh"

# Run tests
echo "Running tests..."
python -m pytest
