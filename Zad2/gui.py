import Tkinter
from Tkinter import *
import tkMessageBox
from createFiles import createFiles

top = Tkinter.Tk()

def createCallBack():
  createFiles(eFolderName.get())

# Przycisk do generowania plikow
buttonGenerate = Tkinter.Button(top, text ="Create Files", command = createCallBack)
buttonGenerate.pack(side = TOP)

# Pole teksowe
eFolderName = Entry(top)
eFolderName.pack()
eFolderName.insert(END,"folder name")

top.mainloop()
