#!/usr/bin/python3
import sys
import re

def print_stats(file_size, status_codes):
    print(f"File size: {file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)', line)
            if match:
                status_code = int(match.group(3))
                file_size += int(match.group(4))
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                count += 1
                if count % 10 == 0:
                    print_stats(file_size, status_codes)
        
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        sys.exit(0)

    print_stats(file_size, status_codes)

if __name__ == "__main__":
    main()

