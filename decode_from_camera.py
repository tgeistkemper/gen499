#the purpose of this code is to decode a qrcode from a camera screen
#OpenCV module documentation: https://docs.opencv.org/master/
#Image module documentation: https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#PIL documentation: https://pillow.readthedocs.io/en/stable/
#qrcode was used to construct my qrcode: http://omz-software.com/editorial/docs/ios/qrcode.html
#pyzbar documentation: https://pypi.org/project/pyzbar/

#code below similar to https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
#pyzbar documentation: https://pypi.org/project/pyzbar/
from pyzbar import pyzbar
from pyzbar.pyzbar import decode

#https://docs.opencv.org/master/
import cv2

#part of python documentation
import argparse

cv2.namedWindow('test') #initializing/naming the window test
cam = cv2.VideoCapture(0) #index of the camera is 0
img_counter = 0 #the number of images captured is 0

while True:
    ret, frame = cam.read() #reading the frames
    cv2.imshow('test', frame) #showing the window with the frames
    if not ret: #if the camera read isn't working...
        break #...exit the loop
    k = cv2.waitKey(1) #wait for a key to be pressed: either esc or space bar

    if k%256 == 27: #if esc is pressed...
        print('Escape hit, closing the window...') #...tell the user what the program is doing...
        break #... and exit the loop
    elif k%256 == 32: #if space bar is pressed...
        barcodes = pyzbar.decode(frame) #decoding the qrcode with pyzbar
        for barcode in barcodes:
            print(decode(frame)) #decoding the qrcode and printing the output
            (x, y, w, h) = barcode.rect #getting the box qrcode_location
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0,0,255), 2) #drawing the bounding box on the qrcode
            barcode_data = barcode.data.decode("utf-8") #converting the image in bytes to a string
            barcode_type = barcode.type #changing bytes to strings
            text = "{} ({})".format(barcode_data, barcode_type) #drawing the barcode data on the image
            cv2.putText(frame, text, (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) #drawing the barcode type on the image
            print("[INFO] Found {} barcode: {}".format(barcode_type, barcode_data)) #printing the barcode type and data to terminal
            cv2.imshow("Image", frame) #showing the output image
            cv2.waitKey(0) #waiting for 0 to be pressed before ending
            img_name = "opencv_frame{}.jpg".format(img_counter) #... save the file as a jpg
            photo = cv2.imwrite(img_name, frame) #saving the actual photo as a jpg
            print("{} written!".format(img_name)) #telling the user that the jpg was written with the actual file name
            img_counter += 1 #adding 1 to the img_counter so photos are not overwritten when another is taken
            break

cam.release() #stopping the camera from being read
cv2.destroyAllWindows() #closing the windows
