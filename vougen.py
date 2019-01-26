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
