#!/usr/bin/env python

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


pdfmetrics.registerFont(TTFont('DejaVuSans','DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('Arial','ariblk.ttf'))


def password_generator(size=9, chars=string.ascii_letters + string.digits):
    """
    Returns a string of random characters, useful in generating temporary
    passwords for automated password resets.

    size: default=8; override to provide smaller/larger passwords
    chars: default=A-Za-z0-9; override to provide more/less diversity
    """
    return ''.join(random.choice(chars) for i in range(size))


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=2,
    border=4,
)


filename = 'users.rsc'
wtofi = 1
wtoru = 0
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
        api = connect(username='lab', password='1234', host='192.168.25.244', ssl_wrapper=ctx.wrap_socket, port=8729)

preus = "10"
limit_time = "1d"
userdic = {}
idnu = 12
dnsname = "barad.store"
for i in range(idnu):
    user = "barst"+preus+str(i)
    passwd = (password_generator())
    userdic.update({user : passwd})
    roucomm = ("add limit-uptime="+limit_time+" name="+user+" password="+passwd+" server=hotspot1")
    print(roucomm)
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
profile =  "1 DAY Access"
pnu = int(idnu/4)
minra = 0
maxra = 4
canvas = canvas.Canvas("vouchers.pdf")
for p in range(pnu):
    canvas.setLineWidth(.1)
    canvas.setFont('Helvetica', 12)

    canvas.drawInlineImage(ptemp, 20,0, width=240,height=300)
    canvas.drawInlineImage(ptemp, 320,0, width=240,height=300)
    canvas.drawInlineImage(ptemp, 20,400, width=240,height=300)
    canvas.drawInlineImage(ptemp, 320,400, width=240,height=300)



    xqr = {0:160,1:460,2:160,3:460}
    yqr = {0:505,1:505,2:105,3:105}
    xus ={0:38,1:338,2:38,3:338}
    yus ={0:555,1:555,2:155,3:155}
    xps ={0:38,1:338,2:38,3:338}
    yps ={0:515,1:515,2:115,3:115}

    canvas.setFont("Arial", 13)
    i = 0
    for j in range(minra,maxra):
        qrimage = "barst"+preus+str(j)+".png"
        userq = "barst"+preus+str(j)
        passq = (userdic[userq])
        xqri = (xqr[i])
        yqri = (yqr[i])
        xusi = (xus[i])
        yusi = (yus[i])
        xpsi = (xps[i])
        ypsi = (yps[i])
        canvas.drawInlineImage(qrimage, xqri,yqri, width=None,height=None)
        canvas.drawString(xusi,yusi, userq)
        canvas.drawString(xpsi,ypsi, passq)
        i += 1
    minra += 4
    maxra += 4
    canvas.setFont("Arial", 10)
    canvas.drawString(37,605, profile)
    canvas.drawString(337,605, profile)
    canvas.drawString(37,205, profile)
    canvas.drawString(337,205, profile)
    canvas.showPage()
canvas.save()


for p in Path(".").glob("barst*.png"):
    p.unlink()
print("QR temp files Removed!")
