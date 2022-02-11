import tkinter
import json

#初期化用ボタンのクラス
class DefaultButton(tkinter.Button):
    def __init__(self, var, master=None):
        super().__init__(
            master=master,
            width=15,
            text="set default(25)",
            command=self.set_default,
            )
        self.var = var

    def set_default(self):
        self.var.set(25)



if __name__ == "__main__":

    def Refresher():
        print("hello")
        root.after(5000, Refresher) # every second...

        # ファイルから値を読み込み
        f = open('test2.json', 'r')
        json_dict = json.load(f)
        f.close()

        temp = json_dict['present']['temperature']
        humi = json_dict['present']['humidity']
        lumi = json_dict['present']['luminance']

        print(temp)
        print(humi)
        print(lumi)
        b.var.set(temp)



    root = tkinter.Tk()
    
    #変数の設定
    temperature = tkinter.IntVar(
        master=root,
        value=25,
    )

    #現在値表示用ラベルの設定
    l = tkinter.Label(
        master=root,
        width=10,
        textvariable=temperature,
    )
    l.pack()

    #スケールの設定
    s = tkinter.Scale(
        master=root,
        orient="horizontal",
        from_ = 15,
        to = 35,
        showvalue=False,
        variable=temperature,
        )
    s.pack()

    #ボタンの設定
    b = DefaultButton(
        master=root,
        var=temperature,
        )
    b.pack()

    Refresher()
    root.mainloop()
