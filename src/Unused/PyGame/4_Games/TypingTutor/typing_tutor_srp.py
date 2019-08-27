# -*- acsection: general-init -*-
import pygame as pg, random

pg.init() # uključujemo rad biblioteke PyGame
pg.display.set_caption("Куцање - пуцање")
(sirina, visina) = (600, 400)
prozor = pg.display.set_mode((sirina, visina))   # otvaramo prozor

# -*- acsection: main -*-

def ispisi(poruka, x, y):
    font = pg.font.SysFont("Arial", 32)           # font kojim će biti prikazan tekst
    tekst = font.render(poruka, True, pg.Color("green")) # gradimo sličicu sa tekstom
    prozor.blit(tekst, (x, y)) # prikazujemo sličicu na odgovarajućem mestu na ekranu

def crtanje():
    prozor.fill(pg.Color("black"))    # bojimo prozor u crno
    if not igra_zavrsena:
        # ako igra jos traje, ispisi slova koja padaju i broj poena
        for slovo, x, y in slova_koja_padaju:
            ispisi(slovo, x, y)
        ispisi('poeni: ' + str(poeni), 0, visina - 40)
    else:
        # u protivnom ispisi poruku za kraj
        ispisi('Kraj igre', 100, 100)
        ispisi('Osvojili ste ' + str(poeni) + ' poena', 100, 200)

def novi_frejm():
    global slova_koja_padaju, vreme_do_slova, sledece_x
    global prvo_slovo_za_biranje, slova_od_kojih_se_bira, igra_zavrsena
    # pomeri sva padajuca slova dva piksela nize, proveri da li se jos igra
    nova_slova = []
    for slovo, x, y in slova_koja_padaju:
        if y < visina - 40: 
            nova_slova.append((slovo, x, y + 2))
        else:
            # ako je neko slovo stglo do dna prozora, to je kraj igre
            igra_zavrsena = True 
            
    # azuriraj spisak slova koja padaju
    vreme_do_slova -= 1
    if vreme_do_slova <= 0: # ako treba dodati jos jedno slovo koje pada...
        vreme_do_slova = 20
        sledece_x += 20
        if sledece_x >= sirina:
            # red na prozoru je popunjen, azuriraj slova koja igraju
            sledece_x -= sirina
            if prvo_slovo_za_biranje + BROJ_SLOVA_ZA_BIRANJE < len(slova):
                prvo_slovo_za_biranje += 1
                slova_od_kojih_se_bira = slova[prvo_slovo_za_biranje : prvo_slovo_za_biranje + BROJ_SLOVA_ZA_BIRANJE]
        # dodaj jos jedno slovo koje pada
        slovo = random.choice(slova_od_kojih_se_bira)
        nova_slova.append((slovo, sledece_x, 0))

    slova_koja_padaju = nova_slova
    
def obradi_dogadjaj(dogadjaj):
    global slova_koja_padaju, poeni
    if dogadjaj.type == pg.KEYDOWN: # pritisak tastera na tastaturi
        otkucano_slovo = dogadjaj.unicode.upper()
        if len(slova_koja_padaju) > 0: # ako ima slova koaj padaju
            slovo, x, y = slova_koja_padaju[0] # najnize slovo koje pada
            if otkucano_slovo == slovo:
                del slova_koja_padaju[0]
                poeni += 10 # nagrada za otkucano najnize slovo 
            else:
                poeni -= 4  # kazna za pogresno slovo
            
# slova = 'АСДФЈКЛЧЕИРУТЗГХЊОЉПЦ,ВМБНЏЅ.-'
slova = 'ASDFJKL;EIRUTYGHWOQPC,VMBNXZ.-'
BROJ_SLOVA_ZA_BIRANJE = 4
prvo_slovo_za_biranje = 0
slova_od_kojih_se_bira = slova[prvo_slovo_za_biranje : prvo_slovo_za_biranje + BROJ_SLOVA_ZA_BIRANJE]
slova_koja_padaju = []
vreme_do_slova = 0
sledece_x = 0
poeni = 0
igra_zavrsena = False
# -*- acsection: after-main -*-

kraj = False
sat = pg.time.Clock() # sat koji određuje broj frejmova u sekundi
while not kraj:
    novi_frejm()
    crtanje()
    pg.display.update()       # ažuriramo prikaz sadržaja prozora
    
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:      # isključivanje prozora
            kraj = True
        else:
            obradi_dogadjaj(dogadjaj)
        
    sat.tick(30)

pg.quit()  # isključujemo rad biblioteke PyGame
