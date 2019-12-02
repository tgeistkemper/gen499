#the purpose of this code is to find qrcodes on an image not specified as a qrcode
#OpenCV module documentation: https://docs.opencv.org/master/
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
#qrcode was used to construct my qrcode: http://omz-software.com/editorial/docs/ios/qrcode.html
#pyzbar documentation: https://pypi.org/project/pyzbar/

#code below similar to https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
#pyzbar documentation: https://pypi.org/project/pyzbar/
from pyzbar import pyzbar

#OpenCV module documentation: https://docs.opencv.org/master/
import cv2

#part of python documentation
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) #read the image input

barcodes = pyzbar.decode(image) #decoding the qrcode with pyzbar

for barcode in barcodes:
    (x, y, w, h) = barcode.rect #getting the box qrcode_location
    cv2.rectangle(image, (x,y), (x + w, y + h), (0,0,255), 2) #drawing the bounding box on the qrcode
    barcode_data = barcode.data.decode("utf-8") #converting the image in bytes to a string
    barcode_type = barcode.type #changing bytes to strings
    text = "{} ({})".format(barcode_data, barcode_type) #drawing the barcode data on the image
    cv2.putText(image, text, (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) #drawing the barcode type on the image
    print("[INFO] Found {} barcode: {}".format(barcode_type, barcode_data)) #printing the barcode type and data to terminal

cv2.imshow("Image", image) #showing the output image
cv2.waitKey(0) #waiting for 0 to be pressed before ending
