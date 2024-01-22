# Importar o pygame e o random para podermos usá-las
import pygame
import random


def genComida():
    comida = [
        BLOCO * random.randint(0, GRELHA),
        BLOCO * random.randint(0, GRELHA),
        False,
    ]
    print(comida[0], comida[1])

    return comida


# Inicia a janela do pygame
pygame.init()
BLOCO = 30
GRELHA = 16
screen = pygame.display.set_mode((BLOCO * GRELHA, BLOCO * GRELHA))
clock = pygame.time.Clock()

# Define que o jogo está a decorrer
running = True

# Uma comida vai aparecer num local aleatório
comida = genComida()

# Variavel que nos vai dizer onde está o jogador a todos os momentos, o jogador começa no meio do ecrã
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

wants_to = ""
direction = ""
last_direction = ["", ""]

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

    pygame.draw.rect(screen, "red", (player_pos[0], player_pos[1], BLOCO, BLOCO))
    pygame.draw.rect(screen, "green", (comida[0], comida[1], BLOCO, BLOCO))
    pygame.display.flip()

    # colisões
    if comida[0] < player_pos[0] < (comida[0] + BLOCO):
        if comida[1] < player_pos[1] < (comida[1] + BLOCO):
            comida[2] = True

    # input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP] and direction != "BAIXO":
        wants_to = "CIMA"
    if keys[pygame.K_s] or keys[pygame.K_DOWN] and direction != "CIMA":
        wants_to = "BAIXO"
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and direction != "DIREITA":
        wants_to = "ESQUERDA"
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and direction != "ESQUERDA":
        wants_to = "DIREITA"

    # movimentação
    print(wants_to)
    step = 5
    if wants_to == "CIMA" and player_pos.y > 0:
        if player_pos.x % BLOCO == 0:
            direction = wants_to
    elif wants_to == "BAIXO" and player_pos.y < screen.get_height() - BLOCO:
        if player_pos.y % BLOCO == 0:
            direction = wants_to

    if wants_to == "ESQUERDA" and player_pos.x > 0:
        if player_pos.y % BLOCO == 0:
            direction = wants_to
    elif wants_to == "DIREITA" and player_pos.x < screen.get_width() - BLOCO:
        if player_pos.y % BLOCO == 0:
            direction = wants_to

    if direction == "CIMA":
        player_pos.y -= step
    elif direction == "BAIXO":
        player_pos.y += step
    elif direction == "ESQUERDA":
        player_pos.x -= step
    elif direction == "DIREITA":
        player_pos.x += step

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
