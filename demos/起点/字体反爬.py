#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
from fontTools.ttLib import TTFont
import re
from PIL import Image, ImageDraw, ImageFont

html = open("test.html", 'r', encoding="utf-8").read()
base64_string = html.split("base64,")[1].split("'")[0]
bin_data = base64.decodebytes(base64_string.encode())
with open("base.woff", r"wb") as f:
    f.write(bin_data)

font_list = re.findall('&#x(\w+)', html)
for font_secret in font_list:
    one_font = int(font_secret, 16)
    font = TTFont('base.woff')
    # font.saveXML('test.xml')
    c = font['cmap'].tables[2].ttFont.tables['cmap'].tables[1].cmap
    # print("c::::::", c)
    gly_font = c[one_font]
    b = font['cmap'].tables[2].ttFont.getReverseGlyphMap()
    # print("b:::::::", b)
    print(b[gly_font] - 1)
