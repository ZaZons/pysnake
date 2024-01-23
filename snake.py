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


def set_fruta(fruta, valor):
    print("fruta")


def set_player(nome, player):
    player = nome


def atuamae():
    # Define que o jogo está a decorrer
    running = True

    # Uma comida vai aparecer num local aleatório
    comida = genComida()

    pontos = 0

    # Variavel que nos vai dizer onde está o jogador a todos os momentos, o jogador começa no meio do ecrã
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    wants_to = ""
    direction = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if comida[2]:
            comida = genComida()

        # Preencher o fundo do jogo
        for i in range(0, GRELHA):
            for j in range(0, GRELHA - 1, 2):
                if i % 2 == 0:
                    pygame.draw.rect(
                        screen, (187, 213, 249), (j * BLOCO, BLOCO * i, 30, 30)
                    )
                    pygame.draw.rect(
                        screen, (152, 193, 246), ((j + 1) * BLOCO, BLOCO * i, 30, 30)
                    )
                else:
                    pygame.draw.rect(
                        screen, (152, 193, 246), (j * BLOCO, BLOCO * i, 30, 30)
                    )
                    pygame.draw.rect(
                        screen, (187, 213, 249), ((j + 1) * BLOCO, BLOCO * i, 30, 30)
                    )

        font = pygame.font.SysFont("opensans.ttf", 32)
        text_pontos = font.render("Pontos: " + str(pontos), True, "black")
        text_player = font.render("Player: " + player, True, "green")

        screen.blit(text_pontos, text_pontos.get_rect())
        # screen.blit(text_player, text_player.get_rect())

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
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# Inicia a janela do pygame
pygame.init()
BLOCO = 30
GRELHA = 16
screen = pygame.display.set_mode((BLOCO * GRELHA, BLOCO * GRELHA))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake da mia e da Wakidd")
player = ""

menu = pygame_menu.Menu(
    "Bem vindo", 400, 400, theme=pygame_menu.themes.THEME_BLUE, onclose=atuamae
)
menu.add.text_input("Name :", default="mia", onchange=set_player)
menu.add.selector(
    "Fruta :", [("Morango", 1), ("Laranja", 2), ("Pera", 3)], onchange=set_fruta
)
menu.add.button("Play", menu.close)
menu.add.button("Quit", pygame_menu.events.EXIT)

# Começar o jogo em si
while menu.is_enabled():
    # Se o jogador clicar no X o programa fecha
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    menu.update(events)
    menu.draw(screen)
    pygame.display.update()
