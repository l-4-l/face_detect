# https://stackoverflow.com/questions/20502237/how-to-save-captured-image-to-disk-using-pygame
# https://www.pygame.org/docs/ref/pixelarray.html
# https://www.pygame.org/docs/ref/surface.html
# https://www.pygame.org/docs/tut/SurfarrayIntro.html

import pygame.camera
import pygame.image
import sys
import numpy as np
from array import array


def append_img_from_cam(img_arr, webcam_l):
    img_new = pygame.surfarray.array3d(webcam_l.get_image())
    img_arr.append(img_new)


pygame.camera.init()
cameras = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cameras[0])
webcam.start()


img = []
append_img_from_cam(img, webcam)
image_1 = webcam.get_image().copy()
screen = pygame.display.set_mode((image_1.get_width(), image_1.get_height()))


def avg_images(img):
    rz = np.mean(img, axis=0)
    return rz


image = img[0]
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    sf = pygame.surfarray.make_surface(image)
    screen.blit(sf, (0, 0))
    pygame.display.flip()
    # grab next frame
    append_img_from_cam(img, webcam)

    if len(img) > 10:
        img.pop(0)

    image = avg_images(img)

#pygame.image.save(img, "image.jpg")
