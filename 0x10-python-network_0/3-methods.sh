#!/bin/bash
# a Bash script that takes in a URL
# and displays all HTTP methods the server will accepts
curl -sX OPTIONS -i "$1" | grep "Allow" | awk -F ': ' '{print $2}'
