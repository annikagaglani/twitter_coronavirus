#!/usr/bin/env python3

import os
import json
import argparse
from collections import Counter, defaultdict

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--output_folder', default='outputs', help="Folder containing map outputs")
args = parser.parse_args()

# Function to merge Counter dictionaries
def merge_counters(files):
    merged_counter = defaultdict(Counter)
    for file_path in files:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for key, subdict in data.items():
                    for subkey, count in subdict.items():
                        merged_counter[key][subkey] += count
        except Exception as e:
            print(f"Skipping {file_path} due to error: {e}")
    return merged_counter

# Find all .lang and .country files
lang_files = [os.path.join(args.output_folder, f) for f in os.listdir(args.output_folder) if f.endswith('.lang')]
country_files = [os.path.join(args.output_folder, f) for f in os.listdir(args.output_folder) if f.endswith('.country')]

# Merge all language data
merged_lang = merge_counters(lang_files)
merged_country = merge_counters(country_files)

# Write merged results
output_lang_path = os.path.join(args.output_folder, 'reduced.lang')
output_country_path = os.path.join(args.output_folder, 'reduced.country')

print(f"Saving reduced language data to {output_lang_path}")
with open(output_lang_path, 'w') as f:
    json.dump(merged_lang, f, indent=2)

print(f"Saving reduced country data to {output_country_path}")
with open(output_country_path, 'w') as f:
    json.dump(merged_country, f, indent=2)

print("Reduction complete!")
