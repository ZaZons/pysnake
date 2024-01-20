# Importar o pygame e o random para podermos usá-las
import pygame
import random


def genComida():
    comida = [random.randint(30, screen.get_width() - 30), random.randint(30, screen.get_height() - 30), False]
    print(comida[0], comida[1])

    return comida

# Inicia a janela do pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))

# Define que o jogo está a decorrer
running = True

# Uma comida vai aparecer num local aleatório
comida = [random.randint(30, screen.get_width() - 30), random.randint(30, screen.get_height() - 30), False]

# Variavel que nos vai dizer onde está o jogador a todos os momentos, o jogador começa no meio do ecrã
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Começar o jogo em si
while running:
    # Se o jogador clicar no X o programa fecha
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo do jogo
    screen.fill("black")

    if comida[2]:
        comida = genComida()

    pygame.draw.rect(screen, "red", (player_pos[0], player_pos[1], 30, 30))
    pygame.draw.rect(screen, "green", (comida[0], comida[1], 30, 30))
    pygame.display.flip()

    # if player_pos[0] + 15 == comida[0] + 15:
    #     if player_pos[1] == comida[1]:
    #         comida[2] = True

    if player_pos[1] < (comida[1] + 15):
 
      if ((player_pos[0] > comida[0]
           and player_pos[0] < (comida[0] + 15))
          or ((player_pos[0] + 15) > comida[0]
           and (player_pos[0] + 15) < (player_pos[0] + 15))):
           comida[2] = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 2
    if keys[pygame.K_s]:
        player_pos.y += 2
    if keys[pygame.K_a]:
        player_pos.x -= 2
    if keys[pygame.K_d]:
        player_pos.x += 2

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()

