#!/bin/bash

# Set input and output directories
INPUT_DIR="/data/Twitter dataset/"  # Change this to the correct dataset path if needed
OUTPUT_JSON_DIR="outputs/json"
OUTPUT_LOG_DIR="outputs/logs"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_JSON_DIR"
mkdir -p "$OUTPUT_LOG_DIR"

# Loop through all tweet zip files from 2020
for file in "$INPUT_DIR"/geoTwitter20-*.zip; do
    echo "Processing $file..."

    #Extract filename without path
    filename=$(basename "$file")

    # Run map.py with nohup to keep it running after logout and & to parallelize
    nohup python3 src/map.py --input_path="$file" --output_folder "$OUTPUT_JSON_DIR" > "$OUTPUT_LOG_DIR/$(basename "$file").log" 2>&1 &
done

echo "All map.py tasks started in parallel."
