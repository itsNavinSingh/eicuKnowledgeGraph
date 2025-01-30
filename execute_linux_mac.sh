#!/bin/bash

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing required Python packages..."
pip install -r requirements.txt

# Prompt user for input directory
echo "Enter the input directory path:"
read input_path

# Create a result directory if it doesn't exist
result_dir="result"
mkdir -p "$result_dir"

# Loop through all Python files in the current directory
for file in *.py; do
    if [[ -f "$file" ]]; then
        echo "$file execution started"
        python3 "$file" "$input_path"
        echo "$file execution completed"
    fi
done

echo "All scripts executed."

# execution command
# chmod +x execute_linux_mac.sh
# ./execute_linux_mac.sh

