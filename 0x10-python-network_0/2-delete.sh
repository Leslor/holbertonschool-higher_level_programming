#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argumen and displays the body of the response
curl -sX DELETE "{$1}"
