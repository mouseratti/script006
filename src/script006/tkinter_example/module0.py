import tkinter
from time import sleep


if __name__ == '__main__':
    mainwindow=tkinter.Tk()
    mainwindow.title('Example')
    mainwindow.geometry('500x400+300+200') # ширина=500, высота=400, x=300, y=200
    sleep(5)
    mainwindow.mainloop()
