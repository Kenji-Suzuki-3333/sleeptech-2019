#!/bin/sh
echo "ohayou"

■音楽制御
#音楽再生していたプロセスを停止
cat cvlc_process_id.txt | xargs kill -term
#バックグラウンドで音楽再生
cvlc /home/pi/music/Wake_me_Up.mp3 &
#プロセスkill用にプロセスIDを保存
echo $! > cvlc_process_id.txt
echo cvlc_process_id.txt

#■扇風機制御（どれか一つでいい）
#扇風機off
#echo "USB off"
#sudo sh /home/pi/USBHubControl/usb_off.sh

#IFTTTにGetupのWebhookを投げる
#echo "send IFTTT to Getup"
#sh /home/pi/IFTTT/GetupToIftttWebhook.sh

#赤外線リモコンOff
sh /home/pi/IR_Concent/IR_Concent_Off.sh

#■ライト制御
#MiLightオン
#echo "MiLight ON"
#python3 /home/pi/Milight/feedin.py

#USB LEN ON
sh /home/pi/USB_LED/USB_LED_On.sh



