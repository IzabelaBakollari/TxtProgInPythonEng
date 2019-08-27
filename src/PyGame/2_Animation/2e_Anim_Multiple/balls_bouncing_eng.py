import random, pygame as pg, petljapg
(width, height) = (500, 300)
canvas = petljapg.open_window(width, height, "Balls")

colors = (
    pg.Color("red"), pg.Color("yellow"), pg.Color("blue"),
    pg.Color("cyan"), pg.Color("green"), pg.Color("purple")
)

# Make a list of 10 ball. The ball is determined by 
# position (x, y), displacement (dx, dy), size (r) and color.
balls = []
for _ in range(10):
    r = random.randint(10, 30)
    x = random.randint(r, width - r)
    y = random.randint(r, height - r)
    color = random.choice(colors)
    dx, dy = 0, 0
    while dx == 0 and dy == 0: # we don't want the balls that stand still
        dx = random.randint(-8, 8)
        dy = random.randint(-8, 8)
    balls.append((x, y, dx, dy, r, color))
    
def new_frame():
    global balls
    for i in range(10):
        x, y, dx, dy, r, color = balls[i]
        (x, y) = (x + dx, y + dy)
        if x - r < 0 or x + r > width: 
            dx = -dx
        if y - r < 0 or y + r > height: 
            dy = -dy
        balls[i] = (x, y, dx, dy, r, color)
        
    canvas.fill(pg.Color("darkgray"))
    for x, y, dx, dy, r, color in balls:
        pg.draw.circle(canvas, color, (x, y), r)

petljapg.frame_loop(50, new_frame)