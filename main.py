#!/usr/bin/python3
# vougen
# This is for to create Mikrotik Hotspot User & the voucher for it.
# It can write the created user(s) directly on the Mikrotik Routers
# Developed by Pezhman Shafigh
# January 2019


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class vougen:

    def __init__(self, master):

        self.master = master
        master.title("VOUGEN V1.0")
        master.geometry('660x400+250+100')

        #### Initialize Label Frames ####
        self.labelvoucher = ttk.Label(master, text="Mikrotik Hotspot User & Voucher")
        self.labelvoucher.grid(row= 0 , column= 0 , sticky=W, padx= 5, pady= 2)

        self.voucher_LabelFrame = ttk.LabelFrame(master, text="Voucher", height = 300, width = 320)
        self.voucher_LabelFrame.grid(row= 1, column= 0 , padx= 5, pady= 2)
        self.voucher_LabelFrame.configure(borderwidth= 2)

        self.action_LabelFrame = ttk.LabelFrame(master, text="Actions", height = 300, width = 320)
        self.action_LabelFrame.grid(row= 1, column= 1 , padx= 5, pady= 2)
        self.action_LabelFrame.configure(borderwidth= 2)




def main():

    root = Tk()
    app = vougen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
