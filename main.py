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

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
import string
import random
import qrcode
import os
from librouteros import connect
import ssl
import time
import getpass


class vougen:

    def __init__(self, master):

        self.master = master
        master.title("VOUGEN V1.0")
        master.geometry('660x510+250+100')

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
        #self.btndoit.grid(row="0", column="0",padx= (2,190), sticky='e')
        self.btndoit.grid(row="0", column="1",padx= (2,2), sticky='ne')
        #self.btnQuit.grid(row="0", column="2",padx= 2, pady= 5, sticky='ew')

        self.btndoit.configure(width="5")
        #self.btnQuit.configure(width="5")

        self.textout = Text(self.footer_LabelFrame, width = 82 , height =12)
        self.textout.grid(row="0", column="0",padx= (1,0), pady = 1)

    def BtnAbout(self):
        pr_about = subprocess.Popen([ 'python3', 'about.py' ])

    def Btndoit(self):
        self.vou_gen()
        #self.textout.insert(END, vou_gen.roucomm)
        if self.wtfi.get() == 1:
           print("user.rsc file created!")
           s= "user.rsc file created!"
           self.textout.insert(END, s)
           self.textout.see(END)
           pr_csv = subprocess.Popen([ 'python3', 'rsc2csv.py' ])

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


    def vou_gen(self):

        chars=string.ascii_letters + string.digits
        wtofi = self.wtfi.get()
        wtoru = self.wtru.get()
        idnu = int(self.sboxusnu.get())
        prefix = self.entprefix.get()
        size = int(self.cboxlenpass.get())
        dnsname = self.enthotdns.get()
        plt = self.cboxplt.get()
        hotnam = self.enthotnam.get()
        ru_po = self.entroupo.get()
        ru_us = self.entrouuse.get()
        ru_pa = self.entroupass.get()
        ru_ip = self.entrouip.get()

        pdfmetrics.registerFont(TTFont('DejaVuSans','DejaVuSans.ttf'))
        pdfmetrics.registerFont(TTFont('Arial','ariblk.ttf'))

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=4,
        )

        ############################################

        filename = 'users.rsc'
        if wtofi == 1:
            for p in Path(".").glob("users.rsc"):
                p.unlink()
            with open(filename, 'w') as file_object:
                file_object.write("/ip hotspot user\n")

        if wtoru == 1:
                print("Connecting to Router...")
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                #api = connect(username='lab', password='1234', host='192.168.25.244', ssl_wrapper=ctx.wrap_socket, port=8729)
                api = connect(username=ru_us, password=ru_pa, host=ru_ip, ssl_wrapper=ctx.wrap_socket, port=ru_po)

        limit_time = plt+"d"
        userdic = {}
        for i in range(idnu):
            user = prefix+str(i)
            #passwd = (self.password_generator(size))
            passwd = ''.join(random.choice(chars) for i in range(size))
            userdic.update({user : passwd})
            roucomm = ("add limit-uptime="+limit_time+" name="+user+" password="+passwd+" server="+hotnam)
            print(roucomm)
            s = '{}\n'.format(roucomm)
            self.textout.insert(END, s)
            self.textout.see(END)
            if wtofi == 1:
                with open(filename, 'a') as file_object:
                    file_object.write(roucomm+"\n")
            if wtoru == 1:
                parms = {'limit-uptime': limit_time, 'name': user, 'password': passwd, 'server': 'hotspot1'}
                api(cmd='/ip/hotspot/user/add', **parms)


            qr.clear()
            qr.add_data('http://'+dnsname+'/login?username='+user+'&password='+passwd)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            #img.show()
            img.save(user+".png")


        print("Waiting ......")

        ## Create the print temp
        ptemp = "printtemp.jpg"
        profile = plt+" DAY Access"
        pnu = int(idnu/4)
        minra = 0
        maxra = 4
        c = canvas.Canvas("vouchers.pdf")
        for p in range(pnu):
            c.setLineWidth(.1)
            c.setFont('Helvetica', 12)

            c.drawInlineImage(ptemp, 20,0, width=240,height=300)
            c.drawInlineImage(ptemp, 320,0, width=240,height=300)
            c.drawInlineImage(ptemp, 20,400, width=240,height=300)
            c.drawInlineImage(ptemp, 320,400, width=240,height=300)



            xqr = {0:160,1:460,2:160,3:460}
            yqr = {0:505,1:505,2:105,3:105}
            xus ={0:38,1:338,2:38,3:338}
            yus ={0:555,1:555,2:155,3:155}
            xps ={0:38,1:338,2:38,3:338}
            yps ={0:515,1:515,2:115,3:115}

            c.setFont("Arial", 13)
            i = 0
            for j in range(minra,maxra):
                qrimage = prefix+str(j)+".png"
                userq = prefix+str(j)
                passq = (userdic[userq])
                xqri = (xqr[i])
                yqri = (yqr[i])
                xusi = (xus[i])
                yusi = (yus[i])
                xpsi = (xps[i])
                ypsi = (yps[i])
                c.drawInlineImage(qrimage, xqri,yqri, width=None,height=None)
                c.drawString(xusi,yusi, userq)
                c.drawString(xpsi,ypsi, passq)
                i += 1
            minra += 4
            maxra += 4
            c.setFont("Arial", 10)
            c.drawString(37,605, profile)
            c.drawString(337,605, profile)
            c.drawString(37,205, profile)
            c.drawString(337,205, profile)
            c.showPage()
        c.save()
        self.del_temp(prefix)

    def del_temp(self, prefix):
        for p in Path(".").glob(prefix+"*.png"):
            p.unlink()
        print("QR temp files Removed!")

def main():

    root = Tk()
    app = vougen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
