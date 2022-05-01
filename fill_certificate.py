#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
image_width = config['image']['width']
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
        W, H = (image_width,height)
        w, h = font.getsize(name)

        # Prints Name
        name_width = config['name']['width_offset_left'] + (W-w)/2 - config['name']['width_offset_right']
        name_height = config['name']['height']
        name_font_size = config['name']['font_size']
        font = ImageFont.truetype(r'./news-serif.ttf', name_font_size)
        draw.text(name_width, name_height), name, (0,0,0), font=font)

        # Prints Distance
        distance_width = config['distance']['width']
        distance_height = config['distance']['height']
        distance_font_size = config['distance']['font_size']
        font = ImageFont.truetype(r'./news-serif.ttf', distance_font_size)
        draw.text((distance_width, distance_height), distance, (0,0,0), font=font)

        # Prints Time
        time_width = config['time']['width']
        time_height = config['time']['height']
        time_font_size = config['time']['font_size']
        font = ImageFont.truetype(r'./news-serif.ttf', time_font_size)
        draw.text((time_width, time_height), time, (0,0,0), font=font)

        img.save('certs/{0}.jpg'.format(name))
        img.close
