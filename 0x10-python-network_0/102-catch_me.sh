#!/bin/bash
# displays the size of the body of the response
curl -d "user_id=98" -H "Origin: HolbertonSchool" -sLX put 0.0.0.0:5000/catch_me
