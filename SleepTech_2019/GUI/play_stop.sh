#!/bin/sh
echo "play stop"

#音楽再生していたプロセスを停止
cat cvlc_process_id.txt | xargs kill -term

