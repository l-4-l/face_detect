# https://realpython.com/blog/python/face-recognition-with-python/
# http://pygametutorials.wikidot.com/tutorials-basic

import cv2
import sys

import pygame
from pygame.locals import *


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.img = pygame.image.load('abba.png')
        self.size = self.img.get_rect().size
        pygame.display.set_caption('AbbA')

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.img = pygame.image.load('abba.recog.png')
        elif event.type == pygame.MOUSEBUTTONUP:
            self.img == pygame.image.load('abba.png')
        self._display_surf.blit(self.img, (0, 0))

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()


# Get user supplied values
if len(sys.argv) > 1:
    imagePath = sys.argv[1]
else:
    imagePath = "abba.png"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("./haarcascades/haarcascade_eye.xml")
smileCascade = cv2.CascadeClassifier("./haarcascades/haarcascade_smile.xml")

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
    face_image = cv2.cvtColor(image[y:(y+h), x:(x+w)], cv2.COLOR_BGR2GRAY)

    eyes = eyeCascade.detectMultiScale(
        face_image,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(2, 2)
        #,flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    for (ex, ey, ew, eh) in eyes:
        cv2.circle(image, (x+ex+ew/2, y+ey+eh/2), ew/2, (0,255,255))

    smiles = smileCascade.detectMultiScale(
        face_image,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(2, 2)
    )
    for (sx, sy, sw, sh) in smiles:
        cv2.circle(image, (x+sx+sw/2, y+sy+sh/2), sw/2, (200,200, 127))




#cv2.imwrite("abba.recog.png", image)
