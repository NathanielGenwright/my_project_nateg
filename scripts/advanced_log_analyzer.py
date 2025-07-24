#!/usr/bin/env python3
"""
Advanced Log Analyzer

This script provides more sophisticated log analysis capabilities:
- Extracts timestamps and calculates time between errors
- Identifies the most frequent error types
- Generates a summary report as a CSV file
"""

import re
import csv
import argparse
from collections import Counter
from datetime import datetime

def parse_log_line(line):
    """Parse a log line and extract components like timestamp, level, and message."""
    # Example regex for common log format: 2025-07-23 14:30:45 [ERROR] Message
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.*)'
    match = re.match(pattern, line)
    if match:
        timestamp_str, level, message = match.groups()
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        return {
            'timestamp': timestamp,
            'level': level,
            'message': message
        }
    return None

def analyze_log_file(filename):
    """Analyze the log file and return statistics."""
    error_timestamps = []
    error_messages = []
    log_counts = {'ERROR': 0, 'WARN': 0, 'INFO': 0}
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    level = log_entry['level']
                    if level in log_counts:
                        log_counts[level] += 1
                    
                    if level == 'ERROR':
                        error_timestamps.append(log_entry['timestamp'])
                        error_messages.append(log_entry['message'])
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    
    # Calculate time between errors
    time_between_errors = []
    for i in range(1, len(error_timestamps)):
        delta = (error_timestamps[i] - error_timestamps[i-1]).total_seconds()
        time_between_errors.append(delta)
    
    # Find most common error types
    error_types = Counter(error_messages)
    most_common_errors = error_types.most_common(5)  # Top 5 errors
    
    return {
        'log_counts': log_counts,
        'time_between_errors': time_between_errors,
        'most_common_errors': most_common_errors
    }

def generate_csv_report(filename, analysis):
    """Generate a CSV report with the analysis results."""
    if not analysis:
        return
    
    # Create CSV report
    report_filename = f"{filename.split('/')[-1].split('.')[0]}_analysis.csv"
    
    with open(report_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write log counts
        writer.writerow(['Log Level Counts'])
        for level, count in analysis['log_counts'].items():
            writer.writerow([level, count])
        
        writer.writerow([])  # Empty row as separator
        
        # Write time between errors
        if analysis['time_between_errors']:
            writer.writerow(['Time Between Errors (seconds)'])
            for i, time_delta in enumerate(analysis['time_between_errors']):
                writer.writerow([f"Error {i+1} to {i+2}", time_delta])
            
            avg_time = sum(analysis['time_between_errors']) / len(analysis['time_between_errors'])
            writer.writerow(['Average Time Between Errors', f"{avg_time:.2f}"])
        
        writer.writerow([])  # Empty row as separator
        
        # Write most common errors
        writer.writerow(['Most Common Error Messages', 'Count'])
        for error_msg, count in analysis['most_common_errors']:
            writer.writerow([error_msg, count])
    
    print(f"Analysis report generated: {report_filename}")

def main():
    parser = argparse.ArgumentParser(description='Advanced log file analyzer')
    parser.add_argument('logfile', help='Path to the log file to analyze')
    args = parser.parse_args()
    
    analysis = analyze_log_file(args.logfile)
    if analysis:
        print("\nLog Analysis Summary:")
        print("--------------------")
        print(f"ERROR count: {analysis['log_counts']['ERROR']}")
        print(f"WARN count: {analysis['log_counts']['WARN']}")
        print(f"INFO count: {analysis['log_counts']['INFO']}")
        
        if analysis['time_between_errors']:
            avg_time = sum(analysis['time_between_errors']) / len(analysis['time_between_errors'])
            print(f"\nAverage time between errors: {avg_time:.2f} seconds")
        
        print("\nMost common errors:")
        for i, (error, count) in enumerate(analysis['most_common_errors']):
            if i < 3:  # Show only top 3 in console output
                print(f"  {i+1}. {error} ({count} occurrences)")
        
        generate_csv_report(args.logfile, analysis)

if __name__ == "__main__":
    main()
