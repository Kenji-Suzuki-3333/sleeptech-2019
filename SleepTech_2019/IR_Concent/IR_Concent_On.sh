#!/bin/sh

echo "IR Concent ON"

curl --noproxy 192.168.11.2 -X POST 'http://192.168.11.2/messages' -H 'X-Requested-With: curl' -H 'accept: application/json' -d '{"format":"us","freq":38,"data":[2534,2716,794,898,790,901,811,1918,812,1923,793,1939,813,1917,795,897,790,896,813]}'


