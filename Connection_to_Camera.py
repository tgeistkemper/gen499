#!/Users/tgeistkemper/anaconda3/lib/bin/python3

#the purpose of this code is to connect the camera on my laptop to the code
#OpenCV module documentation: https://docs.opencv.org/master/
#code similar to code from https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv

#https://docs.opencv.org/master/
import cv2

#initializing the camera below
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
        img_name = "opencv_frame{}.jpg".format(img_counter) #... save the file as a jpg
        cv2.imwrite(img_name, frame) #saving the actual photo as a jpg
        print("{} written!".format(img_name)) #telling the user that the jpg was written with the actual file name
        img_counter += 1 #adding 1 to the img_counter so photos are not overwritten when another is taken

cam.release() #stopping the camera from being read
cv2.destroyAllWindows() #closing the windows
