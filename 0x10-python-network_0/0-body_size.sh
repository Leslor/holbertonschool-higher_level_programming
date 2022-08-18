#!/bin/bash
#Bash script that takes in a URL, sends a
#request to that URL, and displays the size
#of the body of the response
var=$(curl -sI "${1}" | grep -i "Content-Length:")
[[ $var =~ [^0-9]+([0-9]+) ]]
echo "${BASH_REMATCH[1]}"
