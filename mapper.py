#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    try:
        print(f"{row[2]}\t")
    except IndexError:
        continue
#artists: index 2
