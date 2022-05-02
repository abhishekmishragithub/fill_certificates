#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import configparser
import argparse

image_path="certs"
parser = argparse.ArgumentParser()
parser.add_argument("--datafile", help="Pass optional file path. Default: data/timesheet.csv")
args = parser.parse_args()
if args.datafile:
    filepath = args.datafile
else:
    filepath = "data/timesheet.csv"

config = configparser.ConfigParser()
config.read('config.ini')

with open(filepath) as csvfile:
    tsreader = csv.DictReader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in tsreader:
        img = Image.open("certificate-template.jpg")
        draw = ImageDraw.Draw(img)
        # Credits:
        # https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil

        image_width = int(config['image']['width'])
        image_height = int(config['image']['height'])
        W, H = (image_width, image_height)

        for key, value in row.items():
            item = row[key].strip()
            font_size = config.getint(key, 'font_size')
            font = ImageFont.truetype(r'./news-serif.ttf', font_size)
            w, h = font.getsize(item)
            item_left_offset = config.getint(key, 'width_offset_left', fallback=0)
            item_right_offset = config.getint(key, 'width_offset_right', fallback=0)
            try:
                item_width = config.getint(key, 'width', fallback=0)
            except KeyError:
                item_canvas_center = int((W-w)/2)
                item_width = item_left_offset + item_canvas_center - item_right_offset
            item_height = int(config.get(key, 'height'))
            draw.text((item_width, item_height), item, (0, 0, 0), font=font)

        cert_name = row['name'].lower().replace(' ', '_')
        cert_path=f'{image_path}/{cert_name}.jpg'
        img.save(cert_path)
        img.close()
        print(f"Image {cert_path} saved!")
