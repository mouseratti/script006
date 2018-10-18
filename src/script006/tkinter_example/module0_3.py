import tkinter

class MyButton(tkinter.Button):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid(row=3,column=3,rowspan=2,columnspan=3)
        self['text'] = "im {}".format(self)
        self.bind("<Button-1>", self.command_handler)
        self.bind("<Control-KeyPress-q>", lambda x: print("{} emitted".format(x)))





    def __str__(self):
        return "{} at {}".format(self.__class__, hex(id(self)) )


    def command_handler(self, *args, **kwargs):
        print("{} clicked with args:{} and  kwargs: {}".format(self, args, kwargs))


if __name__ == '__main__':
    mainwindow=tkinter.Tk()
    mainwindow.title('Example')
    mainwindow.geometry('500x400+300+200') # ширина=500, высота=400, x=300, y=200
    b1 = MyButton(mainwindow)
    mainwindow.mainloop()
