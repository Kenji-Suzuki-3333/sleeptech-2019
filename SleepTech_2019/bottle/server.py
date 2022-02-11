from bottle import route, run, template
import subprocess
from subprocess import Popen

@route('/stopwatch/<command>')
def stopwatch(command):
    if command == 'start':
        # /stopwatch/startに対応する処理
        print("start")
        oyasumi_cmd = "sh /home/pi/GUI/oyasumi.sh"
        oyasumi_proc = Popen( oyasumi_cmd.strip().split(" "), shell=False )
    elif command == 'lap':
        # /stopwatch/lapに対応する処理
        print("lap")
        ohayou_cmd = "sh /home/pi/GUI/ohayou.sh"
        ohayou_proc = Popen( ohayou_cmd.strip().split(" "), shell=False )
    elif command == 'stop':
        # /stopwatch/stopに対応する処理
        print("stop")
        stop_cmd = "sh /home/pi/GUI/play_stop.sh"
        stop_proc = Popen( stop_cmd.strip().split(" "), shell=False )

run(host='localhost', port=8080)
