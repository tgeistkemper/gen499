#the purpose of this code is to learn how to encode data in a way that is more suitable for the information in the qrcode
#as a jpeg
#qrcode was used to construct my qrcode: http://omz-software.com/editorial/docs/ios/qrcode.html
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

#http://omz-software.com/editorial/docs/ios/qrcode.html
import qrcode

#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
from PIL import Image

#version = 1: 21*21 which is the smallest version
#error_correction = qrcode.constants.ERROR_CORRECT_L: the smallest qrcode version
#box_size = 10: makes the image larger without making the qrcode more pixelated
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10)

qr.add_data('Group1_Sample1') #adding the data
qr.make() #making the qrcode
img = qr.make_image() #making the qrcode an image
img.save("complex_sample1.jpg") #saving the image
