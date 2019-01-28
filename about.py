#### Imports ####
import tkinter as tk
from tkinter import *
import subprocess
import ast
import os

#### Initialize tkinter
root = Tk()
root.title("About")
root.geometry("+300+150")
mainWindow = Frame(root)
mainWindow.grid()

LICENCE = """MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

def BtnClose():
    root.quit()

l = Label(mainWindow, text="Developed by: Pezhman Shafigh\nhttps://github.com/scriptik/vougen\nVersion: 1.0\nLicence: {}\n".format(LICENCE))
l.grid(row="0", column="0", sticky=E+W+N+S)

btnClose = Button(mainWindow, command=BtnClose, text="Close")
btnClose.grid(row="1", column="0", sticky=E+W+N+S)

root.mainloop()
