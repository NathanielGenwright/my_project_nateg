#!/usr/bin/env bash
# Usage: ./parse_errors.sh <logfile>
# Prints all ERROR lines in the given log file.

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <logfile>" >&2
  exit 1
fi

logfile="$1"

if [[ ! -f "$logfile" ]]; then
  echo "File not found: $logfile" >&2
  exit 2
fi

grep "ERROR" "$logfile"
