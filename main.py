import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "PING PONG"
kolor_tla= (64, 64, 64)

lewa = Actor("left")
lewa.x = 20
lewa.y = HEIGHT/2
lewa.vy = 5
lewa.punkty = 0
lewa.wygrana = False

prawa = Actor("right")
prawa.x = WIDTH-20
prawa.y = HEIGHT/2
prawa.vy = 5
prawa.wygrana = False

pilka = Actor("ball_basket1")
pilka.x = WIDTH/2
pilka.y = HEIGHT/2
pilka.vx = 5
pilka.vy = 5
prawa.punkty = 0

lista_pilek = ["ball", "ball_basket1"]

def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH/2, 40), (WIDTH/2, HEIGHT - 40), color = "yellow")
    screen.draw.line((40, 40), (WIDTH-40, 40), color="yellow")
    screen.draw.line((40, HEIGHT - 40), (WIDTH - 40, HEIGHT-40), color="yellow")
    screen.draw.line((40, 40), (40, HEIGHT- 40), color="yellow")
    screen.draw.line((WIDTH-40, 40), (WIDTH-40, HEIGHT - 40), color="yellow")
    lewa.draw()
    prawa.draw()
    pilka.draw()
    licz_punkty()
    wypisz_wynik()

def licz_punkty():
        screen.draw.text(f"Lewy: {lewa.punkty}", color = "yellow", center = (WIDTH /4 - 20, 20), fontsize = 48)
        screen.draw.text(f"Prawy: {prawa.punkty}", color = "yellow", center = (3*(WIDTH/4) - 20, 20), fontsize = 48)

def wypisz_wynik():
    if lewa.wygrana:
        screen.draw.text("LEWY WYGRYWA!!!", color = "yellow", center = (WIDTH / 2, HEIGHT / 2), fontsize = 96)

    if prawa.wygrana:
        screen.draw.text("PRAWY WYGRYWA!!!", color = "yellow", center = (WIDTH / 2, HEIGHT / 2), fontsize = 96)


def update():
    if not (lewa.wygrana or prawa.wygrana):
        ruch_graczy()
        ruch_pilki()

def ruch_graczy():
    if keyboard.w and lewa.top > 40:
        lewa.y -= lewa.vy

    if keyboard.s and lewa.bottom < HEIGHT - 40:
        lewa.y += lewa.vy

    if keyboard.up and prawa.top > 40:
       prawa.y -= prawa.vy

    if keyboard.down and prawa.bottom < HEIGHT - 40:
        prawa.y += prawa.vy

def ruch_pilki():
    pilka.x += pilka.vx
    pilka.y += pilka.vy

    if pilka.top <= 40:
        pilka.vy *= -1

    if pilka.bottom >= HEIGHT - 40:
        pilka.vy *= -1

    if lewa.colliderect(pilka) and pilka.vx < 0:
        pilka.vx *= -1

    if prawa.colliderect(pilka) and pilka.vx > 0:
        pilka.vx *= -1

    if pilka.x <= 0:
        reset_pilki()
        prawa.punkty += 1
        pilka.image = random.choice(lista_pilek)

    if pilka.x >= WIDTH:
        reset_pilki()
        lewa.punkty += 1
        pilka.image = random.choice(lista_pilek)

    if prawa.punkty == 11:
        prawa.wygrana = True

    if lewa.punkty == 11:
        lewa.wygrana = True


def reset_pilki():
    pilka.x = WIDTH/2
    pilka.y = HEIGHT/2
    pilka.vx = random.choice([-5, 5])
    pilka.vy = random.choice([-5,5])


pgzrun.go()