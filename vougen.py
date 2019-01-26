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
