#the purpose of this code is to decode a qrcode using pyzbar
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
#qrcode was used to construct my qrcode: http://omz-software.com/editorial/docs/ios/qrcode.html
#pyzbar documentation: https://pypi.org/project/pyzbar/

#pyzbar documentation: https://pypi.org/project/pyzbar/
from pyzbar.pyzbar import decode

#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
from PIL import Image

img = Image.open('sample1.jpg') #opening a qrcode I previously made
print(decode(img)) #decoding the qrcode and printing the output
img.close() #closing the image so it can't be edited anymore and is completely done
