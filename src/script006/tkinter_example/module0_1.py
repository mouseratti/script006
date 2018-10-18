import tkinter
from time import sleep


if __name__ == '__main__':
    mainwindow=tkinter.Tk()
    mainwindow.title('Example')
    mainwindow.geometry('500x400+300+200') # ширина=500, высота=400, x=300, y=200
    b1 = tkinter.Button(command=lambda: print("b1 clicked"), text="CLICKME!")
    # b2 = tkinter.Button(command=lambda: print("b2 clicked"), text="CLICKME 2!")
    b1.grid(row=3, column=1, columnspan=3)
    # b2.grid(row=3, column=5, columnspan=3)
    mainwindow.mainloop()
