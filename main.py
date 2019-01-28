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
from vougen import vou_gen

class vougen:

    def __init__(self, master):

        self.master = master
        master.title("VOUGEN V1.0")
        master.geometry('660x310+250+100')

        #### Initialize Label Frames ####

        self.header_LabelFrame = ttk.LabelFrame(master, height = 50, width = 640)
        self.header_LabelFrame.grid(row= 0, column= 0 , columnspan=2, padx= 5, pady= (2,0))
        self.header_LabelFrame.configure(borderwidth= 0)

        self.voucher_LabelFrame = ttk.LabelFrame(master, text="Voucher", height = 300, width = 320)
        self.voucher_LabelFrame.grid(row= 1, column= 0 , padx= 5, pady= 2)
        self.voucher_LabelFrame.configure(borderwidth= 2)

        self.action_LabelFrame = ttk.LabelFrame(master, text="Actions", height = 300, width = 320)
        self.action_LabelFrame.grid(row= 1, column= 1 , padx= 5, pady= 2)
        self.action_LabelFrame.configure(borderwidth= 2)

        self.footer_LabelFrame = ttk.LabelFrame(master, height = 50, width = 640)
        self.footer_LabelFrame.grid(row= 2, column= 0 , columnspan=2, padx= 5)
        self.footer_LabelFrame.configure(borderwidth= 0)

        # Widget header Frame
        self.logo = PhotoImage(file = 'mikrotik_logo.gif')
        self.logoheader = ttk.Label(self.header_LabelFrame,image = self.logo)
        self.logoheader.grid(row= 0 , column= 0 , sticky='w', padx= (0,210), pady= (0,1))

        self.labelheader = ttk.Label(self.header_LabelFrame, text="Hotspot User & Voucher generator")
        self.labelheader.grid(row= 1 , column= 0 , sticky='w', padx= (0,200), pady= (0,1))

        self.btnAbout = Button(self.header_LabelFrame, text="About", command=self.BtnAbout)
        self.btnQuit = Button(self.header_LabelFrame, text="Quit", command=self.BtnQuit)

        self.btnAbout.grid(row="1", column="1",padx= (95,2), pady= (0,1), sticky='e')
        self.btnQuit.grid(row="1", column="2",padx= 2, pady= (0,1) , sticky='ew')

        self.btnAbout.configure(width="5")
        self.btnQuit.configure(width="5")

        # Widget Voucher Frame
        self.labellenpass = ttk.Label(self.voucher_LabelFrame, text="Password Length :")
        self.labellenpass.grid(row= 0 , column= 0 , sticky='w', padx= 2, pady= 2)

        self.lenpass = IntVar()
        self.cboxlenpass = ttk.Combobox(self.voucher_LabelFrame, textvariable = self.lenpass)
        self.cboxlenpass.set('8')
        self.cboxlenpass.grid(row= 0 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.cboxlenpass.configure(width="4", values = ('8','9','10','11','12'))

        self.labellenpass = ttk.Label(self.voucher_LabelFrame, text="Number of Users :")
        self.labellenpass.grid(row= 1 , column= 0 , sticky='w', padx= 2, pady= 2)

        self.usnu = IntVar()
        self.sboxusnu = ttk.Spinbox(self.voucher_LabelFrame, from_ = 4, to = 400, increment = 4, textvariable = self.usnu)
        self.sboxusnu.grid(row= 1 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.sboxusnu.configure(width="3")

        self.labellenpass = ttk.Label(self.voucher_LabelFrame, text="User name prefix :")
        self.labellenpass.grid(row= 2 , column= 0 , sticky='w', padx= (2,40), pady= 2)

        self.entprefix = ttk.Entry(self.voucher_LabelFrame)
        self.entprefix.grid(row= 2 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.entprefix.configure(width="12")

        self.labelhotnam = ttk.Label(self.voucher_LabelFrame, text="Name of hotspot :")
        self.labelhotnam.grid(row= 3 , column= 0 , sticky='w', padx= (2,40), pady= 2)

        self.enthotnam = ttk.Entry(self.voucher_LabelFrame)
        self.enthotnam.grid(row= 3 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.enthotnam.configure(width="12")

        self.labelhotdns = ttk.Label(self.voucher_LabelFrame, text="hotspot DNS :")
        self.labelhotdns.grid(row= 4 , column= 0 , sticky='w', padx= (2,40), pady= 2)

        self.enthotdns = ttk.Entry(self.voucher_LabelFrame)
        self.enthotdns.grid(row= 4 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.enthotdns.configure(width="12")

        self.labelplt = ttk.Label(self.voucher_LabelFrame, text="Profile limit time Day(s) :")
        self.labelplt.grid(row= 5 , column= 0 , sticky='w', padx= 2, pady= 2)

        self.plt = IntVar()
        self.cboxplt = ttk.Combobox(self.voucher_LabelFrame, textvariable = self.plt)
        self.cboxplt.set('1')
        self.cboxplt.grid(row= 5 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.cboxplt.configure(width="4", values = ('1','7','30','60','90', '180', '365'))

        # Widget Action Frame
        self.wtfi = IntVar()
        self.cbwtfi = ttk.Checkbutton(self.action_LabelFrame, variable = self.wtfi,\
                                     text="Save to file", onvalue = 1, offvalue = 0)
        self.cbwtfi.grid(row= 0 , column= 0 , sticky='w',padx= (2,160), pady= 2)

        self.wtru = IntVar()
        self.cbwtru = ttk.Checkbutton(self.action_LabelFrame,variable = self.wtru,\
                                     text="Write on Router", onvalue = 1, offvalue = 0, command=self.active_in)
        self.cbwtru.grid(row= 1 , column= 0 , sticky='w',padx= 2, pady= 2)

        self.labelrouuse = ttk.Label(self.action_LabelFrame, text="Router User name :")
        self.labelrouuse.grid(row= 2 , column= 0 , sticky='w', padx= 2, pady= 2)

        self.entrouuse = ttk.Entry(self.action_LabelFrame)
        self.entrouuse.grid(row= 2 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.entrouuse.configure(width="15", state='disabled')

        self.labelroupass = ttk.Label(self.action_LabelFrame, text="Router password :")
        self.labelroupass.grid(row= 3 , column= 0 , sticky='w', padx= 2, pady= 2)

        self.entroupass = ttk.Entry(self.action_LabelFrame)
        self.entroupass.grid(row= 3 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.entroupass.configure(width="15", show = '*', state='disabled')

        self.labelrouip = ttk.Label(self.action_LabelFrame, text="Router ip :")
        self.labelrouip.grid(row= 4 , column= 0 , sticky='w', padx= 2, pady= 2)

        self.entrouip = ttk.Entry(self.action_LabelFrame)
        self.entrouip.grid(row= 4 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.entrouip.configure(width="15", state='disabled')

        self.labelroupo = ttk.Label(self.action_LabelFrame, text="Router port :")
        self.labelroupo.grid(row= 5 , column= 0 , sticky='w', padx= 2, pady= 2)

        self.entroupo = ttk.Entry(self.action_LabelFrame)
        self.entroupo.grid(row= 5 , column= 1 , sticky='e', padx= 2, pady= 2)
        self.entroupo.configure(width="5", state='disabled')

        # Widget footer Frame
        #self.labelfooter = ttk.Label(self.footer_LabelFrame, text="Mikrotik Hotspot User & Voucher")
        #self.labelfooter.grid(row= 0 , column= 0 , sticky='w', padx= (2,210), pady= 5)

        self.btndoit = Button(self.footer_LabelFrame, text="Do it", command=self.Btndoit)
        #self.btnQuit = Button(self.header_LabelFrame, text="Quit", command=self.BtnQuit)

        #self.btndoit.grid(row="0", column="0",padx= (95,2), pady= 5, sticky='e')
        self.btndoit.grid(row="0", column="0",padx= (2,190), sticky='e')
        #self.btnQuit.grid(row="0", column="2",padx= 2, pady= 5, sticky='ew')

        self.btndoit.configure(width="5")
        #self.btnQuit.configure(width="5")

    def BtnAbout(self):
        pr_batch_set_password = subprocess.Popen([ 'python3', 'about.py' ])

    def Btndoit(self):
        in01 = self.wtfi.get()
        in02 = self.wtru.get()
        in03 = int(self.sboxusnu.get())
        in04 = self.entprefix.get()
        in05 = int(self.cboxlenpass.get())
        in06 = self.enthotdns.get()
        in07 = self.cboxplt.get()
        in08 = self.enthotnam.get()
        in09 = self.entroupo.get()
        in10 = self.entrouuse.get()
        in11 = self.entroupass.get()
        in12 = self.entrouip.get()
        #vou_gen(wtofi = in01, idnu = in03, prefix = in04, size = in05, dnsname = in06, plt = in07, hotnam = in08)
        vou_gen(in01,in02,in03,in04,in05,in06,in07,in08,in09,in10,in11,in12)

    def active_in(self):
        if self.wtru.get() == 1:
           self.entrouuse.configure(state='enable')
           self.entroupass.configure(state='enable')
           self.entrouip.configure(state='enable')
           self.entroupo.configure(state='enable')
        else:
           self.entrouuse.configure(state='disable')
           self.entroupass.configure(state='disable')
           self.entrouip.configure(state='disable')
           self.entroupo.configure(state='disable')


    def BtnQuit(self):
        self.master.quit()

def main():

    root = Tk()
    app = vougen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
