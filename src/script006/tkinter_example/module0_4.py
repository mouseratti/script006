import tkinter

class MyButton(tkinter.Button):

    def __init__(self, master, entry, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._entry = entry
        self.grid(row=4,column=3,rowspan=2,columnspan=3)
        self['text'] = "im {}".format(self)
        self.bind("<Button-1>", self.on_button1)

    def __str__(self): return "{} at {}".format(self.__class__, hex(id(self)) )

    def on_button1(self, *args, **kwargs):
        print("{} clicked with args:{} and  kwargs: {}".format(self, args, kwargs))
        self._entry.hook()


##################################
class MyEntry(tkinter.Entry):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid(row=1,column=3,rowspan=1,columnspan=3)
        self.insert(0,"Enter some text")

    def hook(self):
        text = ' '.join(_ for _ in self.get().split()[::-1])
        self.delete(0,tkinter.END)
        self.insert(0, text)



if __name__ == '__main__':
    mainwindow=tkinter.Tk()
    mainwindow.title('Example')
    mainwindow.geometry('500x400+300+200') # ширина=500, высота=400, x=300, y=200
    e1 = MyEntry(mainwindow)
    b1 = MyButton(mainwindow, e1)
    mainwindow.mainloop()
