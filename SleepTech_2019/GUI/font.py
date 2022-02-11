import tkinter as tk

root = tk.Tk()
str = 'Hello, world, こんにちは世界'

tk.Label(root, text=str, font=('Ricty Diminished', 12)).pack()
tk.Label(root, text=str, font=('Ricty Diminished', 12), fg = 'blue').pack()
tk.Label(root, text=str, font=('Ricty Diminished', 12, 'italic')).pack()
tk.Label(root, text=str, font=('Ricty Diminished', 12, 'italic'), fg ='red').pack()
tk.Label(root, text=str, font=('Ricty Diminished', 16, 'underline')).pack()
tk.Label(root, text=str, font=('Ricty Diminished', 16, 'underline'), fg = 'green').pack()

root.mainloop()
