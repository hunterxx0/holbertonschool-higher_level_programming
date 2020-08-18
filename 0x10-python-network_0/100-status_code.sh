#!/bin/bash
# displays the size of the body of the response
curl -sX HEAD -w "%{http_code}" "$1"
