#!/bin/sh
echo "oyasumi"

#■音楽制御
#音楽再生していたプロセスを停止
cat cvlc_process_id.txt | xargs kill -term
#バックグラウンドで音楽再生
cvlc /home/pi/music/Ukiyobanare.mp3 &
#プロセスkill用にプロセスIDを保存
echo $! > cvlc_process_id.txt
echo cvlc_process_id.txt

#■扇風機制御（どれか一つでいい）
#扇風機on
#echo "USB on"
#sudo sh /home/pi/USBHubControl/usb_on.sh

#IFTTTにSleepのWebhookを投げる
#echo "send IFTTT to Sleep"
#sh /home/pi/IFTTT/SleepToIftttWebhook.sh

#赤外線リモコンOn
sh /home/pi/IR_Concent/IR_Concent_On.sh

#■ライト制御
#MiLightオフ
#echo "MiLight OFF"
#python3 /home/pi/Milight/feedout.py

#USB LEN Off
sh /home/pi/USB_LED/USB_LED_Off.sh

