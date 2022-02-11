#!/usr/bin/python3
# -*- coding: utf8 -*-

import tkinter as tk

root = tk.Tk()

buff = tk.StringVar()
buff.set("")

# ラベルの生成
label = tk.Label(root, textvariable = buff)
label.pack()

# コールバック関数の生成
def make_cmd(n):
    return lambda : buff.set('button {} pressed'.format(n))

# ボタンの生成
for x in range(4):
    button = tk.Button(root, text = 'Button {}'.format(x), command = make_cmd(x))
    button.pack(side = 'left')

root.mainloop()
