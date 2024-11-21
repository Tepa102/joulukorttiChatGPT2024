import pygame
import sys

# Alustetaan pygame
pygame.init()

# Näytön asetukset
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joulukortti oikealla taustalla")

# Ladataan taustakuva
try:
    background = pygame.image.load("images/Meksinkallio2023HimankaTerttuToivonenIMGS2061.jpg")
except pygame.error as e:
    print(f"Virhe: Taustakuvaa ei löytynyt. {e}")
    sys.exit()

# Skaalataan taustakuva näytön kokoon
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Ladataan kuvat joulupukista ja porosta
try:
    santa = pygame.image.load("images/santa2.png")
    reindeer = pygame.image.load("images/reindeer2.png")
except pygame.error as e:
    print(f"Virhe: Kuvia ei löytynyt. {e}")
    sys.exit()

# Skaalataan kuvat
santa = pygame.transform.scale(santa, (200, 200))
santa = pygame.transform.flip(santa, True, False)  # Joulupukki käännetään katsomaan oikealle

reindeer = pygame.transform.scale(reindeer, (150, 150))

# Joulupukin ja poron sijainnit
santa_x, santa_y = 50, HEIGHT - 200
reindeer_x, reindeer_y = +100, HEIGHT - 450

# Kellon asetus animaatiolle
clock = pygame.time.Clock()

# Pelisilmukka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Päivitetään poron sijainti
    reindeer_x -= 3

    # Resetoidaan poron sijainti näytön ulkopuolelle
    if reindeer_x < -150:
        reindeer_x = WIDTH +100
        

    # Piirretään taustakuva
    screen.blit(background, (0, 0))

    # Piirretään joulupukki ja poro
    screen.blit(santa, (santa_x, santa_y))
    screen.blit(reindeer, (reindeer_x, reindeer_y))

    # Näytä "Hyvää Joulua!" -teksti
    font = pygame.font.Font(None, 74)
    text = font.render("Hyvää Joulua!", True, (255, 0, 0))
    screen.blit(text, (WIDTH // 2 - 200, 50))

    # Päivitetään näyttö
    pygame.display.flip()

    # Hidastetaan animaatiota
    clock.tick(60)
