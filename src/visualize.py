#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import matplotlib

# open the input path
with open(args.input_path, encoding='utf-8') as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

for k,v in items:
    print(k,':',v)

plot_title = 'count of hashtag by country'
png_title = args.input_path+args.key+'.png'

top_10 = sorted(items[:10], key=lambda x: x[1])
keys, values = zip(*top_10)
plt.xlabel("country")
plt.ylabel("Count")
plt.title(plot_title)
plt.bar(keys, values)
plt.tight_layout()
plt.savefig(png_title, bbox_inches="tight")
