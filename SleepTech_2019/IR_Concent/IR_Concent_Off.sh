#!/bin/sh

echo "IR Concent ON"

curl --noproxy 192.168.11.2 -X POST 'http://192.168.11.2/messages' -H 'X-Requested-With: curl' -H 'accept: application/json' -d '{"format":"us","freq":32,"data":[2534,2712,796,896,794,1939,792,899,789,898,793,1941,792,899,791,1938,811,1920,792,54188,2555,2697,793,895,811,1920,815,878,810,878,811,1921,810,879,791,1939,796,1938,812,54169,7734,1939,2504,880,809,1921,792,897,811,1920,811,1921,792]}'


