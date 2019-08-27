# -*- acsection: general-init -*-
import pygame as pg, petljapg
canvas = petljapg.open_window(800, 600, "Boxes 2")
# -*- acsection: main -*-

box_image = pg.image.load("box.png")  # image of a box

canvas.fill(pg.Color("lightgray"))

for i in range(4):
    canvas.blit(box_image, (420, 400-95*i))

# -*- acsection: after-main -*-
petljapg.wait_loop()
