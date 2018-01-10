# https://stackoverflow.com/questions/20502237/how-to-save-captured-image-to-disk-using-pygame
# https://www.pygame.org/docs/ref/pixelarray.html
# https://www.pygame.org/docs/ref/surface.html
# https://www.pygame.org/docs/tut/SurfarrayIntro.html

import pygame.camera
import pygame.image
import sys
import numpy as np
from array import array


def append_img_from_cam(img_arr, webcam):
    img_copy = pygame.surfarray.array2d(webcam.get_image())
    img_arr.append(img_copy)


pygame.camera.init()
cameras = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cameras[0])
webcam.start()

# grab first frame
img = []
append_img_from_cam(img, webcam)
image = webcam.get_image().copy()  #temp

WIDTH = image.get_width()
HEIGHT = image.get_height()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("CamView")


def avg_images(img):
    images_count = len(img)

    image_l = img[0].copy()  # result
    #arr = pygame.surfarray.pixels3d(image_l)
    #arr_float = arr.copy()
    #for i in range(len(arr_float)):
    #    for j in range(len(arr_float[i])):
    #        for k in range(len(arr_float[i][j])):
    #            arr_float[i][j][k] = float(arr_float[i][j][k]) / images_count

    if images_count > 1:

        for y in range(1, images_count):
            arr_i = pygame.surfarray.pixels3d(img[y])

            #arr_float = numpy.add(arr_float, arr_i)
            #for i in range(len(arr)):
            #    for j in range(len(arr_i[i])):
            #        for k in range(len(arr_i[i][j])):
            #            arr_float[i][j][k] += float(arr_i[i][j][k]) / images_count
            #np.mean(list_of_arrays[t - N + 1:t + 1], axis=0)
            del arr_i
            img[y].unlock()

    #del arr
    #image_l.unlock()
    return image_l


while True :
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    screen.blit(image, (0, 0))
    pygame.display.flip()
    # grab next frame
    append_img_from_cam(img, webcam)

    if len(img) > 3:
        img.pop(0)

    image = avg_images(img)



#pygame.image.save(img, "image.jpg")
