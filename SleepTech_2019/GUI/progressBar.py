import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

var = tk.IntVar()
var.set(0)

pb1_id = None

def exec_pb1():
    global pb1_id
    var.set(var.get() + 1)
    if var.get() < 100:
        pb1_id = root.after(40, exec_pb1)

def start_pb1():
    var.set(0)
    exec_pb1()

def stop_pb1():
    global pb1_id
    if pb1_id is not None:
        root.after_cancel(pb1_id)
        pb1_id = None

pb1 = ttk.Progressbar(root, length = 200, variable = var)
pb2 = ttk.Progressbar(root, length = 200, mode = 'indeterminate')
pb1.pack()
f1 = ttk.Frame()
ttk.Button(f1, text = 'Start', command = start_pb1).pack(side = tk.LEFT)
ttk.Button(f1, text = 'Stop', command = stop_pb1).pack(side = tk.LEFT)
f1.pack()

pb2.pack()
f2 = ttk.Frame()
ttk.Button(f2, text = 'Start', command = lambda : pb2.start(10)).pack(side = tk.LEFT)
ttk.Button(f2, text = 'Stop',  command = lambda : pb2.stop()).pack(side = tk.LEFT)
f2.pack()

root.mainloop()
