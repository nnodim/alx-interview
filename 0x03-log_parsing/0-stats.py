#!/usr/bin/python3
"""
A python script that reads stdin line by line and computes metrics
"""
import sys

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}
line_count = 0


def print_stats():
    """
    A function to print the statistics
    """
    global total_size, status_codes
    print("File size: {}".format(total_size))
    for status, value in sorted(status_codes.keys()):
        if value != 0:
            print("{}: {}".format(status, value))


try:
    for line in sys.stdin:
        token_list = line.split()

        if len(token_list) > 4:
            total_size += int(token_list[-1])
            status_code = token_list[-2]
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
        line_count += 1
        if line_count == 10:
            line_count = 0
            print_stats()

except Exception as err:
    pass

finally:
    print_stats()
