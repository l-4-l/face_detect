# https://realpython.com/blog/python/face-recognition-with-python/

import cv2
import sys

# Get user supplied values
if len(sys.argv) > 1:
    imagePath = sys.argv[1]
else:
    imagePath = "abba.png"

cascPath = "./haarcascades/haarcascade_frontalface_default.xml"
cascEyePath = "./haarcascades/haarcascade_eye.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier(cascEyePath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #,flags = cv2.CV_HAAR_SCALE_IMAGE
)


print("Found {0} faces".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    eyes = eyeCascade.detectMultiScale(
        cv2.cvtColor(image[y:(y+h), x:(x+w)], cv2.COLOR_BGR2GRAY),
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(2, 2)
        #,flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    for (ex, ey, ew, eh) in eyes:
        cv2.circle(image, (x+ex+ew/2, y+ey+eh/2), ew/2, (0,255,255))
        #def circle(img, center, radius, color, thickness=None, lineType=None, shift=None)




cv2.imwrite("abba.recog.png", image)
