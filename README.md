# Fill Certificate

## Script to batch fill certificates

### How does it work?
The script iterates through `data/timesheet.csv` and fills the value in the certificate and stores them in `certs/`. 
Each certificate is stored with name of the participant.

__Example:__

Certificate for Ashok Kumar would be stored in `certs/ashok_kumar.jpg`.

### How to use
* Go to config.ini and set the image height and width.
* The script automatically calculates width for the name to center it. So set the correct height and left, right offsets if needed.
* Set the font size according to your needs.
* Set the appropriate height, width and font size for time and distance fields.
> The script assumes you have 3 fields - name, distance and time. If you have different fields, you'll need to change code
to match the fields.



###References
* Font: https://www.wfonts.com/search?kwd=serif
* Code: https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil
* Docs: https://pillow.readthedocs.io/en/stable/reference/Image.html
* Similar project: https://crondev.blog/2014/06/16/make-a-certificate-creator-using-python/
