#!/usr/bin/env python3
"""
Read a JSON file and print selected fields.
Usage:
    ./read_json.py data/sample.json
"""
import sys, json, pathlib

if len(sys.argv) != 2:
    print("Usage: read_json.py <jsonfile>", file=sys.stderr)
    sys.exit(1)

p = pathlib.Path(sys.argv[1])
if not p.is_file():
    print(f"File not found: {p}", file=sys.stderr)
    sys.exit(2)

with p.open() as f:
    data = json.load(f)

customer_id = data.get("customer_id")
environment = data.get("environment")
error_count = data.get("error_count")

print(f"customer_id={customer_id}")
print(f"environment={environment}")
print(f"error_count={error_count}")
