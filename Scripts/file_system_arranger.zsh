#!/bin/zsh

# Define the module names
modules=("argParser" "chat" "executor" "extractor" "security")

# Create directories and move files
for module in "${modules[@]}"; do
    mkdir -p modules/$module/tests
    mv modules/$module.py modules/$module/$module.py
done

# Create __init__.py files in module directories
for module in "${modules[@]}"; do
    touch modules/$module/__init__.py
done

# Create tests directory in the root
mkdir tests

# The script doesn't move your test files because it's not clear where they are currently located
# You should move them manually to the appropriate locations
echo "Please move your test files to the appropriate directories."

