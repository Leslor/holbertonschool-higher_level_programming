#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI OPTIONS "{$1}"| grep "Allow:" | cut -d ":" -f2| sed -e 's/^[[:space:]]*//'
