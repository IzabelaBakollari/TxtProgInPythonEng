# -*- acsection: general-init -*-
import pygame as pg, petljapg
canvas = petljapg.open_window(300, 300, "fence")

# -*- acsection: main -*-
def draw_polygon(points, color, x0, y0):
    shifted_points = []
    for x, y in points:
        shifted_points.append((x+x0, y+y0))
    pg.draw.polygon(canvas, color, shifted_points)

canvas.fill(pg.Color("skyblue"))
pg.draw.rect(canvas, pg.Color("green"), (0, 200, 300, 100))  # grass

pg.draw.line(canvas, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(canvas, pg.Color('brown'), ( 10, 250), (290, 250), 10)
picket = [(0, 80), (10, 70), (20, 80), (20, 270), (0, 270)]
for x0 in range(20, 300, 40):
    draw_polygon(picket, pg.Color('brown'), x0, 0)

# -*- acsection: after-main -*-
petljapg.wait_loop()
