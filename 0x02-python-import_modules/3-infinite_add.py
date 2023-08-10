#!/usr/bin/python3

import sys

_len = len(sys.argv)
result = 0
if _len == 1:
    print("{:d}".format(result))
else:
    for i in range(1, _len):
        result += int(sys.argv[i])
    print("{:d}".format(result))
