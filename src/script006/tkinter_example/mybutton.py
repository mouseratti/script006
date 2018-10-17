from tkinter import Button



class MyButton(Button):

    def __init__(self, master=None):
        super().__init__(master, command=self.on_click)
        self.pack()

    def on_click(self, *args, **kwargs):
        print("on_click")

