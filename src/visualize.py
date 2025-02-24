#!/usr/bin/env python3

import argparse
import json
import os
import matplotlib.pyplot as plt

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True, help="Path to the reduced JSON file")
parser.add_argument('--key', required=True, help="Hashtag to visualize")
args = parser.parse_args()

# Load data from the JSON file
try:
    with open(args.input_path, 'r') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading file {args.input_path}: {e}")
    exit(1)

# Extract and sort data for the given key
if args.key not in data:
    print(f"Key '{args.key}' not found in {args.input_path}")
    exit(1)

key_data = data[args.key]
sorted_items = sorted(key_data.items(), key=lambda x: x[1])[-10:]  # Top 10

# Prepare data for plotting
labels, values = zip(*sorted_items)

# Generate bar plot
plt.figure(figsize=(12, 6))
plt.bar(labels, values, color='skyblue')
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')
plt.title(f"Top 10 occurrences of {args.key} in {os.path.basename(args.input_path)}")
plt.tight_layout()

# Save figure
output_filename = f"{os.path.basename(args.input_path)}_{args.key.replace('#', '')}.png"
output_path = os.path.join("outputs", output_filename)
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Saved visualization to {output_path}")
