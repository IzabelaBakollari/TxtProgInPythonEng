# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Кућа")     # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("lightblue")) # bojimo pozadinu ekrana u svetlo plavo

pg.draw.circle(prozor, pg.Color("orange"), (250, 180), 30)   # sunce
pg.draw.rect(prozor, pg.Color("green"), (0, 200, 300, 100))  # trava
pg.draw.rect(prozor, pg.Color("brown"), (50, 150, 150, 100)) # kuca
pg.draw.polygon(prozor, pg.Color("red"), [(50, 150), (125, 100), (200, 150)]) # krov

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
