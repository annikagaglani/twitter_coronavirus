#!/usr/bin/env python3

import os
import json
import argparse
from collections import Counter, defaultdict

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
args = parser.parse_args()

total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            total[k] += tmp[k]

# write the output path
with open(args.output_path,'w') as f:
    f.write(json.dumps(total))
