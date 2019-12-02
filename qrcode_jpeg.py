#the purpose of this code is to learn how to save a qrcode as a jpeg file
#qrcode was used to construct my qrcode: http://omz-software.com/editorial/docs/ios/qrcode.html
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

#http://omz-software.com/editorial/docs/ios/qrcode.html
import qrcode

#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
from PIL import Image

img = qrcode.make(version = 1) #making a simple qrcode (with no data) as an image file
img.save("sample1.jpg") #saving the image as a jpg
