#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
with open('data/timesheet.csv') as csvfile:
    tsreader = csv.DictReader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in tsreader:
        img = Image.open("certificate-template.jpg")
        draw = ImageDraw.Draw(img)
        # Credits:
        # https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
        # Prints Name
        # name = 'Warnakulasuriya Patabendige Ushantha Joseph Chaminda Vaas'
        image_width = int(config['image']['width'])
        image_height = int(config['image']['height'])
        W, H = (image_width, image_height)

        # Prints Name
        name = row['name']
        name_font_size = int(config['name']['font_size'])
        font = ImageFont.truetype(r'./news-serif.ttf', name_font_size)
        w, h = font.getsize(name)
        name_width = int(config['name']['width_offset_left']) + int((W-w)/2) - int(config['name']['width_offset_right'])
        name_height = int(config['name']['height'])
        draw.text((name_width, name_height), name, (0,0,0), font=font)

        # Prints Team Name
        team = row['team']
        team_width = int(config['team']['width'])
        team_height = int(config['team']['height'])
        team_font_size = int(config['team']['font_size'])
        font = ImageFont.truetype(r'./news-serif.ttf', team_font_size)
        draw.text((team_width, team_height), team, (0,0,0), font=font)

        img.save('certs/{0}.jpg'.format(name))
        img.close
