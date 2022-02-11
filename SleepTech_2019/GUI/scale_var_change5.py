import tkinter
import json
import os
import signal
import subprocess
from subprocess import Popen

#初期化用ボタンのクラス
class DefaultButton(tkinter.Button):
    def __init__(self, var, master=None):
        super().__init__( master=master, width=15, text="set default", command=self.set_default,  font=("",font_size))
        self.var = var

    def set_default(self):
        self.var.set(25)

if __name__ == "__main__":
    music_play_proc = None
    font_size = 25

    def Refresher():
        print("Refresher")
        root.after(5000, Refresher) # every second...

        # ファイルから値を読み込み
        f = open('/home/pi/GUI/test2.json', 'r')
        json_dict = json.load(f)
        f.close()

        temp = json_dict['present']['temperature']
        humi = json_dict['present']['humidity']
        lumi = json_dict['present']['luminance']

        print(temp)
        print(humi)
        print(lumi)
        temp_5.var.set(temp)
        humi_5.var.set(humi)
        illu_5.var.set(lumi)

    # clickイベント
    def btn_sleep_click():
        oyasumi_cmd = "sh /home/pi/GUI/oyasumi.sh"
        oyasumi_proc = Popen( oyasumi_cmd.strip().split(" "), shell=False )

    def btn_wakeup_click():
        ohayou_cmd = "sh /home/pi/GUI/ohayou.sh"
        ohayou_proc = Popen( ohayou_cmd.strip().split(" "), shell=False )

    def btn_playstop_click():
        stop_cmd = "sh /home/pi/GUI/play_stop.sh"
        stop_proc = Popen( stop_cmd.strip().split(" "), shell=False )


    root = tkinter.Tk()
    
    #■温度表示
    #変数の設定
    temperature = tkinter.IntVar( master=root, value=25, )
    #現在値表示用ラベルの設定
    temp_1 = tkinter.Label( master=root, text="温度", font=("",font_size))
    temp_2 = tkinter.Label( master=root, width=10, textvariable=temperature, font=("",font_size))
    temp_3 = tkinter.Label( master=root, text="℃ 設定",  font=("",font_size))
    #スケールの設定
    temp_4 = tkinter.Scale( master=root, orient="horizontal", from_ = 15, to = 35, showvalue=False, variable=temperature, )
    #ボタンの設定
    temp_5 = DefaultButton( master=root, var=temperature, )
    temp_1.grid(row=0, column=0)
    temp_2.grid(row=0, column=1)
    temp_3.grid(row=0, column=2)
    temp_4.grid(row=0, column=3)
    temp_5.grid(row=0, column=4)

    #■湿度表示
    #変数の設定
    humidity = tkinter.IntVar( master=root, value=70, )
    #現在値表示用ラベルの設定
    humi_1 = tkinter.Label( master=root, text="湿度",  font=("",font_size))
    humi_2 = tkinter.Label( master=root, width=10, textvariable=humidity,  font=("",font_size))
    humi_3 = tkinter.Label( master=root, text="％ 設定",  font=("",font_size))
    #スケールの設定
    humi_4 = tkinter.Scale( master=root, orient="horizontal", from_ = 0, to = 100, showvalue=False, variable=humidity, )
    #ボタンの設定
    humi_5 = DefaultButton( master=root, var=humidity, )
    humi_1.grid(row=1, column=0)
    humi_2.grid(row=1, column=1)
    humi_3.grid(row=1, column=2)
    humi_4.grid(row=1, column=3)
    humi_5.grid(row=1, column=4)

    #■湿度表示
    #変数の設定
    illuminance = tkinter.IntVar( master=root, value=70, )
    #現在値表示用ラベルの設定
    illu_1 = tkinter.Label( master=root, text="照度",  font=("",font_size))
    illu_2 = tkinter.Label( master=root, width=10, textvariable=illuminance,  font=("",font_size))
    illu_3 = tkinter.Label( master=root, text="％ 設定",  font=("",font_size))
    #スケールの設定
    illu_4 = tkinter.Scale( master=root, orient="horizontal", from_ = 0, to = 100, showvalue=False, variable=illuminance, )
    #ボタンの設定
    illu_5 = DefaultButton( master=root, var=illuminance, )
    illu_1.grid(row=2, column=0)
    illu_2.grid(row=2, column=1)
    illu_3.grid(row=2, column=2)
    illu_4.grid(row=2, column=3)
    illu_5.grid(row=2, column=4)

    # ボタン
    btn_sleep = tkinter.Button(master=root, text='ねる', command=btn_sleep_click, font=("",font_size))
    btn_wakeup = tkinter.Button(master=root, text='おきる', command=btn_wakeup_click, font=("",font_size))
    btn_playstop = tkinter.Button(master=root, text='とめる', command=btn_playstop_click, font=("",font_size))
    btn_sleep.grid(row=3, column=0)
    btn_wakeup.grid(row=3, column=1)
    btn_playstop.grid(row=3, column=2)

    #測定値読み込み＆更新
    Refresher()

    #メインループ
    root.mainloop()
