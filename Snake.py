import random
import pgzrun
import pygame

WIDTH = 800
HEIGHT = 600

koniecGry = False

wysokoscPaska = 50
kolorRamki = "green4"
kolorPol = (50, 175, 25)

rozmiarX = 16
rozmiarY = 16
liczbaPol = rozmiarX * rozmiarY
rozmiarPola = (26, 26)

rozmiarPlanszy = (rozmiarPola[0] * rozmiarX, rozmiarPola[1] * rozmiarY)
polozeniePlanszy = Rect(0, 0, rozmiarX * rozmiarPola[0], rozmiarY * rozmiarPola[1])
polozeniePlanszy.move_ip((WIDTH - rozmiarPlanszy[0]) / 2, wysokoscPaska + ((HEIGHT - wysokoscPaska) - rozmiarPlanszy[1]) / 2)
polozeniePaska = Rect(polozeniePlanszy.x, 0, polozeniePlanszy.width, wysokoscPaska)

plansza = []

pozycjaKursora = (-1, -1)

nacisniecia_klawiszy = 0
licznikCzasu = 0


jablko = 1
zatruteJablko = 2

ikona_usmiech = Actor('grinning_cat', center=polozeniePaska.center)
ikona_usmiech_2 = Actor('cat_with_wry_smile', center=polozeniePaska.center)
ikona_smutek = Actor('crying_cat', center=polozeniePaska.center)
ikona_usmiech_aktywny = Actor('smiling_cat_with_heart_eyes', center=polozeniePaska.center)
ikona_calus = Actor('kissing_cat', center=polozeniePaska.center)

def on_mouse_move(pos):
    global pozycjaKursora
    pozycjaKursora = pos

def generowanieJablka():
    i = 1
    n = 0
    x = random.randint(0, rozmiarX - 1)
    y = random.randint(0, rozmiarY - 1)
    rg = Rect((glowa[0] * rozmiarPola[0] + polozeniePlanszy.x, glowa[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
    if not rg.collidepoint(x,y) and plansza[y][x] != zatruteJablko:
        for w in waz:
            r = Rect((w[0] * rozmiarPola[0] + polozeniePlanszy.x, w[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
            if  not r.collidepoint(x, y):
                plansza[y][x] |= jablko
                i -= 1
            elif r.collidepoint(x, y):
                n += 1
                break
        if i != 0 and n == 0:
            plansza[y][x] |= jablko
    elif rg.collidepoint(x, y):
        n += 1
    while n != 0:
        i = 1
        n = 0
        x = random.randint(0, rozmiarX - 1)
        y = random.randint(0, rozmiarY - 1)
        rg = Rect((glowa[0] * rozmiarPola[0] + polozeniePlanszy.x, glowa[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
        if not rg.collidepoint(x,y) and plansza[y][x] != zatruteJablko:
            for w in waz:
                r = Rect((w[0] * rozmiarPola[0] + polozeniePlanszy.x, w[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
                if  not r.collidepoint(x, y):
                    plansza[y][x] |= jablko
                    i -= 1
                elif r.collidepoint(x, y):
                    n += 1
                    break
            if i != 0 and n == 0:
                plansza[y][x] |= jablko
        elif rg.collidepoint(x, y):
            n += 1

def generowanieZatrutegoJablka():
    i = 1
    n = 0
    x = random.randint(0, rozmiarX - 1)
    y = random.randint(0, rozmiarY - 1)
    rg = Rect((glowa[0] * rozmiarPola[0] + polozeniePlanszy.x, glowa[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
    if not rg.collidepoint(x,y) and plansza[y][x] != jablko:
        for w in waz:
            r = Rect((w[0] * rozmiarPola[0] + polozeniePlanszy.x, w[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
            if  not r.collidepoint(x, y):
                plansza[y][x] |= zatruteJablko
                i -= 1
            elif r.collidepoint(x, y):
                n += 1
                break
        if i != 0 and n == 0:
            plansza[y][x] |= zatruteJablko
    elif rg.collidepoint(x, y):
        n += 1
    while n != 0:
        i = 1
        n = 0
        x = random.randint(0, rozmiarX - 1)
        y = random.randint(0, rozmiarY - 1)
        rg = Rect((glowa[0] * rozmiarPola[0] + polozeniePlanszy.x, glowa[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
        if not rg.collidepoint(x,y) and plansza[y][x] != jablko:
            for w in waz:
                r = Rect((w[0] * rozmiarPola[0] + polozeniePlanszy.x, w[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
                if  not r.collidepoint(x, y):
                    plansza[y][x] |= zatruteJablko
                    i -= 1
                elif r.collidepoint(x, y):
                    n += 1
                    break
            if i != 0 and n == 0:
                plansza[y][x] |= zatruteJablko
        elif rg.collidepoint(x, y):
            n += 1

def draw():
    global waz_w_ruchu, waz
    screen.fill('black')
    screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    r = polozeniePlanszy.inflate(2, 2)
    for i in range(3):
        screen.draw.rect(r, kolorRamki)
        r = r.inflate(2, 2)
    for x in range(rozmiarX):
        for y in range(rozmiarY):
            r = Rect((x * rozmiarPola[0] + polozeniePlanszy.x, y * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
            screen.draw.filled_rect(r, kolorPol)
            screen.draw.rect(r, kolorRamki)

            if plansza[y][x] == jablko:
                size = images.apple_small.get_size()
                screen.blit(images.apple_small, (r.x + (r.w - size[0]) / 2, r.y + (r.h - size[1]) / 2))
            elif plansza[y][x] == zatruteJablko:
                size = images.poison_apple.get_size()
                screen.blit(images.poison_apple, (r.x + (r.w - size[0]) / 2, r.y + (r.h - size[1]) / 2))

    i = 0
    color = (30, 250, 200)
    waz_w_ruchu = waz.copy()
    waz_w_ruchu.insert(0, glowa)
    for w in waz_w_ruchu:
        r = Rect((w[0] * rozmiarPola[0] + polozeniePlanszy.x, w[1] * rozmiarPola[1] + polozeniePlanszy.y),rozmiarPola)
        if (i > 0):
           color = (10, 250, 50)
        screen.draw.filled_circle((r.x + rozmiarPola[0] / 2, r.y + rozmiarPola[1] / 2), 10, color)
        i += 1


    screen.draw.text('{:03d}'.format(czas), midright=(polozeniePaska.right, polozeniePaska.centery),
        fontsize=wysokoscPaska, color='red', fontname = 'crashed_scoreboard')
    screen.draw.text('{:03d}'.format(IloscJablek), midleft=(polozeniePaska.left, polozeniePaska.centery),
        fontsize=wysokoscPaska, color='red', fontname = 'crashed_scoreboard')

    if (ikona_usmiech_aktywny.collidepoint(pozycjaKursora)):
        ikona_calus.draw()
    elif (koniecGry):
        if wygrana:
            ikona_usmiech_aktywny.draw()
        else:
            ikona_smutek.draw()
    else:
        if nacisniecia_klawiszy == 1:
            ikona_usmiech_2.draw()
        else:
            ikona_usmiech.draw()

def update(dt):

    return

def on_key_down(key):
    global kierunek, nacisniecia_klawiszy
    if key == keys.LEFT:
        kierunek = (-1, 0)
    elif key == keys.RIGHT:
        kierunek = (1, 0)
    elif key == keys.UP:
        kierunek = (0, -1)
    elif key == keys.DOWN:
        kierunek = (0, 1)
    elif key == keys.ESCAPE:
        exit()
    nacisniecia_klawiszy = 1

def on_key_up():
    global nacisniecia_klawiszy
    nacisniecia_klawiszy = 0

def on_mouse_down(pos):
    if ikona_calus.collidepoint(pos):
        stop(False)
        start()
    elif ikona_smutek.collidepoint(pos):
        stop(False)
        start()
    elif ikona_usmiech.collidepoint(pos):
        stop(False)
        start()
    elif ikona_usmiech_2.collidepoint(pos):
        stop(False)
        start()
    elif ikona_usmiech_aktywny.collidepoint(pos):
        stop(False)
        start()

def zerujPlansze():
    global plansza
    plansza = [[0]*rozmiarX for i in range(rozmiarY)]

def aktualizujCzas():
    global waz, glowa, dlugosc_weza, IloscJablek, licznik, predkosc, czas, licznikCzasu
    
    if czas > 999:
        czas = 999
        stop(False)
    licznikCzasu += 1
    if licznikCzasu == 100:
        czas += 1
        licznikCzasu = 0

    licznik += 0.01
    if licznik >= predkosc:
        licznik = 0

        waz.insert(0, glowa)
        waz = waz[:dlugosc_weza]

        glowa = (glowa[0] + kierunek[0], glowa[1] + kierunek[1])

        if IloscJablek == 25:
            stop(True)
            return

        if glowa[0] < 0:
            stop(False)
            return

        if glowa[0] >= rozmiarX:
            stop(False)
            return

        if glowa[1] < 0:
            stop(False)
            return

        if glowa[1] >= rozmiarY:
            stop(False)
            return

        for w in waz:
            if glowa[0] == w[0] and glowa[1] == w[1]:
                stop(False)
                return

        if not koniecGry:
            if plansza[glowa[1]][glowa[0]] == jablko:
                dlugosc_weza += 1
                if predkosc > 0.04:
                    predkosc -= 0.03
                plansza[glowa[1]][glowa[0]] = 0
                generowanieJablka()
                IloscJablek += 1
            elif plansza[glowa[1]][glowa[0]] == zatruteJablko:
                if predkosc < 0.5:
                    predkosc += 0.03
                plansza[glowa[1]][glowa[0]] = 0
                generowanieZatrutegoJablka()

def stop(_wygrana):
    global koniecGry, wygrana
    clock.unschedule(aktualizujCzas)
    koniecGry = True
    wygrana = _wygrana

def start():
    global czas, wygrana, IloscJablek, waz, predkosc, licznik, glowa, waz_w_ruchu, dlugosc_weza, kierunek, koniecGry
    koniecGry = False
    IloscJablek = 0
    czas = 0
    wygrana = False
    waz = []
    waz_w_ruchu = []
    predkosc = 0.5
    licznik = 0
    dlugosc_weza = 1
    glowa = (random.randint(4, rozmiarX - 4), random.randint(4, rozmiarY - 4))
    kierunek = (1, 0)
    zerujPlansze()
    generowanieJablka()
    generowanieZatrutegoJablka()

    clock.schedule_interval(aktualizujCzas, 0.01)


start()

pgzrun.go()