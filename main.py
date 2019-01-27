#!/usr/bin/python3
# vougen
# This is for to create Mikrotik Hotspot User & the voucher for it.
# It can write the created user(s) directly on the Mikrotik Routers
# Developed by Pezhman Shafigh
# January 2019


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

class vougen:

    def __init__(self, master):

        self.master = master
        master.title("VOUGEN V1.0")
        master.geometry('660x400+250+100')

        #### Initialize Label Frames ####

        self.header_LabelFrame = ttk.LabelFrame(master, height = 50, width = 640)
        self.header_LabelFrame.grid(row= 0, column= 0 , columnspan=2, padx= 5, pady= 2)
        self.header_LabelFrame.configure(borderwidth= 0)

        self.voucher_LabelFrame = ttk.LabelFrame(master, text="Voucher", height = 300, width = 320)
        self.voucher_LabelFrame.grid(row= 1, column= 0 , padx= 5, pady= 2)
        self.voucher_LabelFrame.configure(borderwidth= 2)

        self.action_LabelFrame = ttk.LabelFrame(master, text="Actions", height = 300, width = 320)
        self.action_LabelFrame.grid(row= 1, column= 1 , padx= 5, pady= 2)
        self.action_LabelFrame.configure(borderwidth= 2)


        # Widget header Frame
        self.labelvoucher = ttk.Label(self.header_LabelFrame, text="Mikrotik Hotspot User & Voucher                                ")
        self.labelvoucher.grid(row= 0 , column= 0 , sticky='w', padx= (2,80), pady= 5)

        self.btnAbout = Button(self.header_LabelFrame, text="About", command=self.BtnAbout)
        self.btnQuit = Button(self.header_LabelFrame, text="Quit", command=self.BtnQuit)

        self.btnAbout.grid(row="0", column="1",padx= (95,2), pady= 5, sticky='e')
        self.btnQuit.grid(row="0", column="2",padx= 2, pady= 5, sticky='ew')

        self.btnAbout.configure(width="5")
        self.btnQuit.configure(width="5")

        # Widget Voucher Frame


    def BtnAbout(self):
        pr_batch_set_password = subprocess.Popen([ 'python3', 'scripts/about.py' ])
    def BtnQuit(self):
        self.master.quit()


def main():

    root = Tk()
    app = vougen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
