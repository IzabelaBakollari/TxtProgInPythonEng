# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Вежба 5")  # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo

pg.draw.rect(prozor, pg.Color("darkgray"), (120, 50, 60, 140)) # zgrada

for y in range(5):     # sprat
    for x in range(2): # strana (0 - leva, 1 - desna)
        if (x+y) % 2 == 0:
            boja = pg.Color("yellow")
        else:
            boja = pg.Color("black")
        kvadrat = (130 + 25 * x, 60 + 20 * y, 15, 15)
        pg.draw.rect(prozor, boja, kvadrat)                    # prozor

pg.draw.rect(prozor, pg.Color("black"),  (140, 160, 20, 30))   # kapija

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
