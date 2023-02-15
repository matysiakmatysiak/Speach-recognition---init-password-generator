import tkinter
import sys
from methods import record, wyjscie

def gui():
    root = tkinter.Tk()
    root.geometry('1024x768')
    label = tkinter.Label(root, text='Speech Recognition by Michal')
    label.pack()
    b = tkinter.Button(root, text='Rozpocznij nagrywanie i zapisz do pliku', command=record)
    b.pack()
    b_2 = tkinter.Button(root, text='Wyjscie', command=wyjscie)
    b_2.pack()
    root.mainloop()