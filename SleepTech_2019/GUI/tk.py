import os, sys, time
import tkinter as tk

def pushed(self):
    print("clicked")
    self["text"] = "押されたよ"

# メインウィンドウ作成
root = tk.Tk()

#メインウィンドウのタイトルを変更
root.title("Tkinter test")

#メインウィンドウを640x480にする
root.geometry("640x480")


#ラベルを追加
label = tk.Label(root, text="Hello,World")
#表示
label.grid()

button = tk.Button(root, text="ボタン", command= lambda : pushed(button))
button.pack()

root.mainloop()

