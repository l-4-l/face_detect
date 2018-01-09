# https://stackoverflow.com/questions/20502237/how-to-save-captured-image-to-disk-using-pygame
# https://www.pygame.org/docs/ref/pixelarray.html
# https://www.pygame.org/docs/ref/surface.html
# https://www.pygame.org/docs/tut/SurfarrayIntro.html

import pygame.camera
import pygame.image
import sys
from array import array

pygame.camera.init()

cameras = pygame.camera.list_cameras()

print "Using camera %s ..." % cameras[0]

webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame
img = []
img.append(webcam.get_image())
image = img[0].copy()

WIDTH = image.get_width()
HEIGHT = image.get_height()

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
#pygame.display.set_caption("CamView")

def avg_images(img):
    image_l = img[0].copy() # result
    arr = pygame.surfarray.pixels3d(image_l)

    images_count = len(img)
    if images_count > 1:
        for i in range(1, images_count):
            arr_i = pygame.surfarray.pixels3d(img[i])
            arr[:, :, 0] += arr_i[:, :, 0]
            arr[:, :, 1] += arr_i[:, :, 1]
            arr[:, :, 2] += arr_i[:, :, 2]
            img[i].unlock()
            del arr_i
        #arr = [x // len(img) for x in arr]
        arr[:, :, 0] = [x // images_count for x in arr[:, :, 0]]
        arr[:, :, 1] = [x // images_count for x in arr[:, :, 1]]
        arr[:, :, 2] = [x // images_count for x in arr[:, :, 2]]

    del arr
    image_l.unlock()
    return image_l


while True :
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    screen.blit(image, (0, 0))
    pygame.display.flip()
    # grab next frame
    img.append(webcam.get_image())

    if len (img) > 10:
        img.pop(0)

    image = avg_images(img)



#pygame.image.save(img, "image.jpg")
