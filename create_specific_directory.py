#The purpose of this code is to learn how to make a directory for my qrcodes that is general for any computer software and
#show exactly where the directory is located in the absolute path.
#https://stackabuse.com/creating-and-deleting-directories-with-python/ - a website I used for learning about the os module
#https://docs.python.org/3/library/os.html - documentation for the os python module
#https://docs.python.org/3/library/os.path.html#module-os.path - documentation for the os.path python module

#https://docs.python.org/3/library/os.html
import os

path = "qrcode_location" #naming the directory or "path" to be created

if os.path.isdir(path) == True: #if the directory already exists...
    print("This directory already exists.") #Do not create this directory as it will result in an error. Print this instead
    print("The path of this directory is:", os.path.abspath(path)) #printing the absolute path of the directory
else: #if the directory does not already exist...
    print("Creating new directory.")
    os.mkdir(path)
    print("New directory made.") #Print statement letting the user know the directory was made
    print("The path of this new directory is:", os.path.abspath(path)) #printing the path of the new directory
