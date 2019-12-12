#the purpose of this code is to figure out how to paste an image onto another image
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#ImageDraw module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/

#ImageFont module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/ImageFont.html
from PIL import Image, ImageDraw, ImageFont

#http://omz-software.com/editorial/docs/ios/qrcode.html
import qrcode

#version = 1: 21*21 which is the smallest version
#error_correction = qrcode.constants.ERROR_CORRECT_L: the smallest qrcode version
#box_size = 10: makes the image larger without making the qrcode more pixelated
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10)
qr.add_data("Sample1") #adding the data for a qrcode
qr.make() #creating the qrcode
list_qrcode = qr.make_image() #making the qrcode an image file
list_qrcode.save('sample1.jpg') #saving the qrcode image as a jpeg

width = 2480 #width of a piece of paper in pixels
height = 3508 #height of a piece of paper in pixels

img2 = Image.new(mode = "1", size = (width, height)) #creating a new image

img = Image.open('sample1.jpg') #opening the qrcode image
img = img.resize((620,620))

img2.paste(img, (620,620))
img2.save('newimage.jpg')
img.close()
img2.close()
