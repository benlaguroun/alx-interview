#!/usr/bin/python3
import sys
import signal

def print_stats(file_size, status_codes):
    """Print statistics"""
    print("File size: {}".format(file_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] != 0:
            print("{}: {}".format(status_code, status_codes[status_code]))

def signal_handler(sig, frame):
    """Signal handler"""
    print_stats(total_size, status_codes)

status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) > 2:
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += int(file_size)
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

