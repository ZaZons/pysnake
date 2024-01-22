# Importar o pygame e o random para podermos usá-las
import pygame
import random


def genComida():
    comida = [
        BLOCO * random.randint(0, GRELHA - 1),
        BLOCO * random.randint(0, GRELHA - 1),
        False,
    ]
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

pontos = 0

# Variavel que nos vai dizer onde está o jogador a todos os momentos, o jogador começa no meio do ecrã
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

wants_to = ""
direction = ""
cobra = [
    [
        pygame.image.load("imagens/cobra.png"),
        screen.get_width() / 2,
        screen.get_height() / 2,
    ]
]

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

    fruta = pygame.image.load("imagens/fruta.png")
    screen.blit(fruta, (comida[0], comida[1]))

    # Update positions of the snake's body segments
    for i in range(pontos, 0, -1):
        cobra[i][1] = cobra[i - 1][1] + BLOCO
        cobra[i][2] = cobra[i - 1][2] + BLOCO

    # Update position of the snake's head
    if direction == "CIMA":
        cobra[0][2] -= 3
    elif direction == "BAIXO":
        cobra[0][2] += 3
    elif direction == "ESQUERDA":
        cobra[0][1] -= 3
    elif direction == "DIREITA":
        cobra[0][1] += 3

    # Draw the snake
    for i in range(pontos + 1):
        screen.blit(cobra[i][0], (cobra[i][1], cobra[i][2]))

    # colisões
    if comida[0] == cobra[0][1] and comida[1] == cobra[0][2]:
        comida[2] = True
        pontos += 1
        cobra.append([pygame.image.load("imagens/cobra.png"), -BLOCO, -BLOCO])

    # input
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and wants_to != "BAIXO":
        wants_to = "CIMA"
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and wants_to != "CIMA":
        wants_to = "BAIXO"
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and wants_to != "DIREITA":
        wants_to = "ESQUERDA"
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and wants_to != "ESQUERDA":
        wants_to = "DIREITA"

    # movimentação
    step = 3
    if wants_to == "CIMA" and cobra[0][1] % BLOCO == 0:
        direction = wants_to
    elif wants_to == "BAIXO" and cobra[0][1] % BLOCO == 0:
        direction = wants_to
    elif wants_to == "ESQUERDA" and cobra[0][2] % BLOCO == 0:
        direction = wants_to
    elif wants_to == "DIREITA" and cobra[0][2] % BLOCO == 0:
        direction = wants_to

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # Decreased the speed for better visibility

pygame.quit()
