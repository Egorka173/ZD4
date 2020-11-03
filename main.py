import pygame
import sys

W, H = 800, 600
w, h = 50, 50
x = (W - w) // 2
y = H // 2 - h * 2
red = (250, 0, 0)
navy = (5, 0, 50)

pygame.init()
pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((W, H))

background = pygame.Surface(screen.get_size())
background.fill(navy)

# Отобразить текст
font = pygame.font.Font(None, 96)
text = font.render("Всем привет", 1, (250, 250, 250), None)
text_pos = text.get_rect(center=(W // 2, H // 2))

font2 = pygame.font.Font(None, 48)
text2 = font2.render("задание на урок", 1, (250, 250, 0), None)
text_pos2 = text2.get_rect(center=(W // 2, H // 2 + font.get_height()))

background.blit(text, text_pos)
background.blit(text2, text_pos)

screen.blit(background, (0, 0))
pygame.draw.rect(screen, red, (x, y, w, h,))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

screen.blit(background, (0, 0))
pygame.draw.rect(screen, red, (x, y, w, h,)) 

x += 1
if x > W:
    x = -w

    pygame.display.update()
    pygame.time.wait(5)