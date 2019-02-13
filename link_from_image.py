from PIL import Image
import re
import pytesseract
import os
import cv2
import webbrowser

# image file that is in the same directory as this script
img = cv2.imread("test.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

file = "{}.jpg".format(os.getpid())
cv2.imwrite(file, gray)

text = pytesseract.image_to_string(Image.open(file))
os.remove(file)

print(text)