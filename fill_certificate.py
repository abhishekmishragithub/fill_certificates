#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv

with open('data/participants.csv') as csvfile:
    tsreader = csv.DictReader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in tsreader:
        img = Image.open("certificate-template.jpg")
        draw = ImageDraw.Draw(img)
        name = row['name']
        # Credits:
        # https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
        # Prints Name
        # name = 'Warnakulasuriya Patabendige Ushantha Joseph Chaminda Vaas'
        font = ImageFont.truetype(r'./news-serif.ttf', 64)
        W, H = (1754,1241)
        w, h = font.getsize(name)
        draw.text(((W-w)/2, 570), name, (0,0,0), font=font)

        cert_name = name.replace(' ', '_')
        img.save('certs/{0}.jpg'.format(cert_name))
        img.close
