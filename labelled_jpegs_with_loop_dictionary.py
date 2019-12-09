#the purpose of this code is to add my dictionary loop into my original labelled_jpegs_into_directory
#https://stackabuse.com/creating-and-deleting-directories-with-python/ - a website I used for learning about the os module
#https://docs.python.org/3/library/os.html - documentation for the os python module
#https://docs.python.org/3/library/os.path.html#module-os.path - documentation for the os.path python module
#qrcode was used to construct my qrcode: http://omz-software.com/editorial/docs/ios/qrcode.html
#code used to make images was based off of https://code-maven.com/create-images-with-python-pil-pillow
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#ImageDraw module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
#code also based off of https://stackoverflow.com/questions/37924130/pil-add-a-text-at-the-bottom-middle-of-image
#ImageFont module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageFont.html

#http://omz-software.com/editorial/docs/ios/qrcode.html
import qrcode

#https://docs.python.org/3/library/os.html
import os

#https://docs.python.org/3/library/shutil.html
import shutil

#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#ImageDraw module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
#ImageFont module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageFont.html
from PIL import Image, ImageDraw, ImageFont

path = "./labelled_jpegs_with_loop_dictionary2" #naming the directory/path to be created
os.mkdir(path) #creating the path

list_of_data = [] #an empty list of data to be in the qrcodes
list_of_names = [] #an empty list of the names of the qrcodes that will be associated with data

n = 1 #setting up the loop: this will be sample 1
while n <= 10: #here is where you can change the number of samples in the list
    list_of_data.append('Sample'+str(n)) #adding the sample number to the list
    list_of_names.append('SAMPLE_'+str(n)) #adding the sample name to the list
    n = n + 1 #adding one to n to go through the loop

dict_of_associated_data = dict(zip(list_of_data, list_of_names)) #connecting the lists into a dictionary

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
    shutil.move(dict_of_associated_data[data]+'.jpg', os.path.abspath(path)) #moving the qrcodes to the new folder
