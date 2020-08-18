#!/bin/bash
# displays the size of the body of the response
curl -sX POST -H "Content-Type: application/json" "$1" -d @"$2"
