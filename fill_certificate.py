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

        image_width = int(config['image']['width'])
        image_height = int(config['image']['height'])
        W, H = (image_width, image_height)

        # Prints Name
        # name = 'Warnakulasuriya Patabendige Ushantha Joseph Chaminda Vaas'
        name = row['name']
        name_font_size = int(config['name']['font_size'])
        font = ImageFont.truetype(r'./news-serif.ttf', name_font_size)
        w, h = font.getsize(name)
        name_width = int(config['name']['width_offset_left']) + int((W-w)/2) - int(config['name']['width_offset_right'])
        name_height = int(config['name']['height'])
        draw.text((name_width, name_height), name, (0, 0, 0), font=font)

        # Prints Distance
        distance = row['distance']
        distance_width = int(config['distance']['width'])
        distance_height = int(config['distance']['height'])
        distance_font_size = int(config['distance']['font_size'])
        font = ImageFont.truetype(r'./news-serif.ttf', distance_font_size)
        draw.text((distance_width, distance_height), distance, (0, 0, 0), font=font)

        # Prints Time
        time = row['time']
        time_width = int(config['time']['width'])
        time_height = int(config['time']['height'])
        time_font_size = int(config['time']['font_size'])
        font = ImageFont.truetype(r'./news-serif.ttf', time_font_size)
        draw.text((time_width, time_height), time, (0, 0, 0), font=font)

        cert_name = name.lower().replace(' ', '_')
        img.save('certs/{0}.jpg'.format(cert_name))
        img.close()
