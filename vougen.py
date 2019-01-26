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
wtoru = 1
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
