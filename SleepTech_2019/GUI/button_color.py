import tkinter as tk

root = tk.Tk()
root.option_add('*Button.font', ('Ricty Diminished', 12))
root.option_add('*Button.background', 'cyan')

buff = tk.StringVar()
buff.set("")

# ラベルの生成
label = tk.Label(root, textvariable = buff)
label.pack(anchor = tk.W)

# コールバック関数の生成
def make_cmd(n):
    return lambda : buff.set('button {} pressed'.format(n))

# ボタンの生成
for x in range(4):
    button = tk.Button(root, text = 'Button {}'.format(x), command = make_cmd(x))
    button.pack(side = tk.LEFT)

root.mainloop()
