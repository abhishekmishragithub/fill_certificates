#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv

with open('data/timesheet.csv') as csvfile:
    tsreader = csv.DictReader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in tsreader:
        img = Image.open("certificate-template.jpg")
        draw = ImageDraw.Draw(img)
        name = row['name']
        team = row['team']
        # Credits:
        # https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
        # Prints Name
        # name = 'Warnakulasuriya Patabendige Ushantha Joseph Chaminda Vaas'
        font = ImageFont.truetype(r'./news-serif.ttf', 64)
        W, H = (1754,1241)
        w, h = font.getsize(name)
        draw.text((((W-w)/2)-285, 500), name, (0,0,0), font=font)
        # Prints Distance
        font = ImageFont.truetype(r'./news-serif.ttf', 40)
        draw.text((300, 620), team, (0,0,0), font=font)

        img.save('certs/{0}.jpg'.format(name))
        img.close
