# Importar o pygame e o random para podermos usá-las
import pygame
import random
import pygame_menu


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

meio = screen.get_width() / 2, screen.get_height() / 2

wants_to = ""
direction = ""


menu = pygame_menu.Menu(
    "Bem vindo",
    400,
    400,
    theme=pygame_menu.themes.THEME_BLUE,
)


# Começar o jogo em si
while running:
    # Se o jogador clicar no X o programa fecha
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo do jogo
    screen.fill("RED")

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    if comida[2]:
        comida = genComida()

    fruta = pygame.image.load("imagens/fruta.png")
    cobra = pygame.image.load("imagens/cobra.png")
    screen.blit(fruta, (comida[0], comida[1]))
    screen.blit(cobra, (player_pos[0], player_pos[1]))

    # colisões
    if comida[0] == player_pos[0]:
        if comida[1] == player_pos[1]:
            comida[2] = True
            pontos += 1

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
    if wants_to == "CIMA" and player_pos[0] % BLOCO == 0:
        direction = wants_to
    elif wants_to == "BAIXO" and player_pos[0] % BLOCO == 0:
        direction = wants_to

    if wants_to == "ESQUERDA" and player_pos[1] % BLOCO == 0:
        direction = wants_to
    elif wants_to == "DIREITA" and player_pos[1] % BLOCO == 0:
        direction = wants_to

    if direction == "CIMA" and player_pos[1] > 0:
        player_pos[1] -= step
    elif direction == "BAIXO" and player_pos[1] < screen.get_height() - BLOCO:
        player_pos[1] += step
    elif direction == "ESQUERDA" and player_pos[0] > 0:
        player_pos[0] -= step
    elif direction == "DIREITA" and player_pos[0] < screen.get_width() - BLOCO:
        player_pos[0] += step

    # flip() the display to put your work on screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()
