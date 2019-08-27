# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Ограда")   # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

prozor.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo
pg.draw.rect(prozor, pg.Color("green"), (0, 200, 300, 100))  # trava

pg.draw.line(prozor, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(prozor, pg.Color('brown'), ( 10, 250), (290, 250), 10)
def crtaj_mnogougao(temena, boja, x0, y0):
    pomerena_temena = [(x+x0, y+y0) for x, y in temena]
    pg.draw.polygon(prozor, boja, pomerena_temena)

pritka = [(0, 80), (10, 70), (20, 80), (20, 270), (0, 270)]
for x0 in range(20, 300, 40):
    crtaj_mnogougao(pritka, pg.Color('brown'), x0, 0)

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
