#the purpose of this code is to find a better font size for the qrcodes
#ImageFont module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageFont.html
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#ImageDraw module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
#code based off of: https://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image
#qrcode was used to construct my qrcode: http://omz-software.com/editorial/docs/ios/qrcode.html
#https://docs.python.org/3/library/os.html - documentation for the os python module

#https://docs.python.org/3/library/os.html
import os

#ImageFont module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageFont.html
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#ImageDraw module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
from PIL import Image, ImageDraw, ImageFont

#http://omz-software.com/editorial/docs/ios/qrcode.html
import qrcode

#below is a list of data for each data of list_of_data in order.
list_of_data = ['SAMPLE 1', 'SAMPLE 2']

#below is a list of data, each of which is going to be linked to by a qrcode.
list_of_associated = ['SAMPLE_1', 'SAMPLE_2']

#below is a dictionary created by the zip function. The dictionary consists of list_of_data and list_of_associated
dict_of_associated_data = dict(zip(list_of_data, list_of_associated))

#below begins a for loop involving every item ('data') in the list, list_of_data.
for data in list_of_data:
    #version = 1: 21*21 which is the smallest version
    #error_correction = qrcode.constants.ERROR_CORRECT_L: the smallest qrcode version
    #box_size = 10: makes the image larger without making the qrcode more pixelated
    qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10)
    qr.add_data(data) #adding the data for a qrcode from list_of_data
    qr.make() #creating the qrcode
    list_qrcode = qr.make_image() #making the qrcode an image file
    list_qrcode.save(dict_of_associated_data[data]+'.jpg')
    img = Image.open(dict_of_associated_data[data]+'.jpg') #opening the png I just made
    edit_img = ImageDraw.Draw(img) #getting the png ready to edit
    fontsize = 20 #size of the font
    text = dict_of_associated_data[data] #text to be written on image
    font = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', fontsize) #getting the font
    w, h = img.size #finding the size of the image
    text_w, text_h = font.getsize(text) #finding the size of the text
    #Below: editing the image: w - text_w // 2 is taking the size of the image minus the size of the text and dividing it by
    #two (centering it) (because it is the x value), h - text_h is putting the text to the bottom (because it is the y value),
    #and 'Sample1' is the text to be drawn.
    edit_img.text(((w - text_w) // 2, h - text_h), text, font = font)
    img.save(dict_of_associated_data[data]+'.jpg') #saving the image as a jpg
    img.close() #closing the image so it can't be edited anymore and is completely done
