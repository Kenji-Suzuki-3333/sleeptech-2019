import tkinter as tk
import sys

root = tk.Tk()
root.option_add("*font", ('', 14))

# variable 用のオブジェクト
action = tk.IntVar()
action.set(0)
level = tk.IntVar()
level.set(1)

# ダミー
def start(): pass

# メニューバー
menubar = tk.Menu(root)
root.configure(menu = menubar)

games = tk.Menu(menubar, tearoff = False)
levels = tk.Menu(menubar, tearoff = False)
menubar.add_cascade(label="Games", underline = 0, menu=games)
menubar.add_cascade(label="Level", underline = 0, menu=levels)

# Games
games.add_command(label = "Start", underline = 0, command = start)
games.add_separator
games.add_radiobutton(label = "first", variable = action, value = 0)
games.add_radiobutton(label = "second", variable = action, value = 1)
games.add_separator
games.add_command(label = "exit", underline = 0, command = sys.exit)

# Labels
levels.add_radiobutton(label = 'Level 1', variable = level, value = 1)
levels.add_radiobutton(label = 'Level 2', variable = level, value = 2)
levels.add_radiobutton(label = 'Level 3', variable = level, value = 3)

# ラベル
tk.Label(root, text = "***** Menu Test *****").pack()

root.mainloop()
