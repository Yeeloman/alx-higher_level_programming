#!/usr/bin/python3

import sys

_len = len(sys.argv)
if _len == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(_len - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
