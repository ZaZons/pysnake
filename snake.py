# Importar o pygame e o random para podermos usá-las
import pygame
import random
import pygame_menu


def genComida():
    comida = [
        BLOCO * random.randint(0, GRELHA - 1),
        BLOCO * random.randint(1, GRELHA - 1),
        False,
    ]

    return comida


def morre():
    font = pygame.font.SysFont("opensans.ttf", 100)
    text_morreste = font.render("Morreste", True, "black", "white")

    morreste_rect = text_morreste.get_rect()
    morreste_rect.x = screen.get_width() / 2 - morreste_rect.width / 2
    morreste_rect.y = screen.get_height() / 2 - morreste_rect.height / 2

    screen.blit(text_morreste, morreste_rect)

    return False


def pontuacao():
    aqui = True
    while aqui:
        screen.fill("white")
        font = pygame.font.SysFont("opensans.ttf", 30)
        if len(leaderboard) > 0:
            for i in range(0, len(leaderboard)):
                for j in range(0, len(leaderboard) - i - 1):
                    if leaderboard[j][1] < leaderboard[j + 1][1]:
                        temp = leaderboard[j]
                        leaderboard[j] = leaderboard[j + 1]
                        leaderboard[j + 1] = temp

            for i in range(0, len(leaderboard)):
                texto = (
                    "#"
                    + str(i + 1)
                    + ": "
                    + leaderboard[i][0]
                    + " ("
                    + str(leaderboard[i][1])
                    + " pontos)"
                )
                text = font.render(texto, True, "black")
                text_rect = text.get_rect()
                text_rect.x = screen.get_width() / 2 - text_rect.width / 2
                text_rect.y = i * 20
                screen.blit(text, text_rect)

        else:
            text = font.render("Sem pontuações ainda, joguem um pouco!!", True, "black")
            screen.blit(text, text.get_rect())

        pygame.display.flip()

        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame_menu.events.QUIT

            if event.type == pygame.locals.KEYDOWN:
                aqui = False
                break


def jogar():
    # Define que o jogo está a decorrer
    running = True
    # Uma comida vai aparecer num local aleatório
    comida = genComida()

    pontos = 0

    # Variavel que nos vai dizer onde está o jogador a todos os momentos, o jogador começa no meio do ecrã
    player_pos = pygame.Vector2(
        screen.get_width() / 2, (screen.get_height() + BLOCO) / 2
    )

    wants_to = ""
    direction = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if comida[2]:
            comida = genComida()

        # Preencher o fundo do jogo
        screen.fill("white")
        for i in range(1, GRELHA + 1):
            for j in range(0, GRELHA, 2):
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

        font = pygame.font.SysFont("opensans.ttf", 40)
        text_pontos = font.render("Pontos: " + str(pontos), True, "black")
        text_player = font.render("Player: " + player_input.get_value(), True, "black")
        text_player_rect = text_player.get_rect()
        text_player_rect.x = screen.get_width() - text_player_rect.width

        screen.blit(text_pontos, text_pontos.get_rect())
        screen.blit(text_player, text_player_rect)

        imagem_comida = pygame.image.load(
            "imagens/comida/" + comida_input.get_value()[0][0] + ".png"
        )
        cobra = pygame.image.load("imagens/cobra.png")
        screen.blit(imagem_comida, (comida[0], comida[1]))
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

        if direction == "CIMA":
            player_pos[1] -= step
        elif direction == "BAIXO":
            player_pos[1] += step
        elif direction == "ESQUERDA":
            player_pos[0] -= step
        elif direction == "DIREITA":
            player_pos[0] += step

        # morte
        if (
            player_pos[1] < BLOCO
            or player_pos[1] > screen.get_height() - BLOCO
            or player_pos[0] < 0
            or player_pos[0] > screen.get_width() - BLOCO
        ):
            leaderboard.append((player_input.get_value(), pontos))
            running = morre()

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame_menu.events.EXIT

        if event.type == pygame.locals.KEYDOWN:
            break


# Inicia a janela do pygame
pygame.init()
BLOCO = 30
GRELHA = 16
screen = pygame.display.set_mode((BLOCO * GRELHA, BLOCO * (GRELHA + 1)))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake da mia e da Wakid")
leaderboard = []
menu = pygame_menu.Menu(
    "Bem vindo",
    400,
    400,
    theme=pygame_menu.themes.THEME_BLUE,
)
player_input = menu.add.text_input("Nome: ", default="mia")
comida_input = menu.add.selector(
    "Comida: ", [("Morango", 0), ("Laranja", 1), ("Pera", 2), ("Chocolate", 3)]
)
menu.add.button("Pontuação", pontuacao)
menu.add.button("Jogar", jogar)
menu.add.button("Sair", pygame_menu.events.EXIT)

# Começar o jogo em si
while menu.is_enabled():
    screen.fill((255, 223, 255))
    # Se o jogador clicar no X o programa fecha
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    menu.update(events)
    menu.draw(screen)
    pygame.display.update()
