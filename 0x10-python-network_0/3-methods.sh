#!/bin/bash
# displays the size of the body of the response
curl -siX OPTIONS $1 | awk '/Allow/{print $0}' | sed -n 's/Allow: //p'
