#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk

def pushed(self):
	self["text"] = "押されたよ"

#rootウィンドウを作成
root = tk.Tk()
#rootウィンドウのタイトルを変える
root.title("Tkinterテスト")
#rootウィンドウの大きさを320x240に
#root.geometry("320x240")
root.geometry("640x480")

#Label部品を作る
label = tk.Label(root, text="Tkinterのテストです")
#表示する
label.grid()

#ボタンを作る
button = tk.Button(root, text="ボタン", command= lambda : pushed(button))
#表示
#button.pack()
button.grid()

#メインループ
root.mainloop()

