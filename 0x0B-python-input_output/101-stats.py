#!/usr/bin/python3
"""file"""

import sys


def print_after_interrupt(total_file_size, status_code_counts):
    """print_after_intrp.

    :param total_file_size:
    :param status_code_counts:
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


if __name__ == "__main__":
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0,
                          401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 7:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                total_file_size += file_size
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                line_count += 1

            if line_count == 10:
                print(f"File size: {total_file_size}")
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print("{}: {}".format(code, count))

    except KeyboardInterrupt:
        print_after_interrupt(total_file_size, status_code_counts)
        raise
