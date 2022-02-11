#!/bin/sh
echo "server start"

#サーバプロセスを停止
cat server_process_id.txt | xargs kill -term

python3 /home/pi/bottle/server.py

echo $! > server_process_id.txt

