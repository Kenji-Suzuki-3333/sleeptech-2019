import tkinter
if __name__ == "__main__":
    root = tkinter.Tk()
    var = tkinter.IntVar(
        master=root,
        value=50
    )
    
    s1 = tkinter.Scale(
        master=root,
        orient="horizontal",
        variable=var,
        )
    s1.pack()
    s2 = tkinter.Scale(
        master=root,
        orient="vertical",
        variable=var,
        )
    s2.pack()
    root.mainloop()