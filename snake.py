# Importar o pygame, o pygame_menu e o random para podermos usá-las
import pygame
import pygame_menu
import random


# Cria uma comida nova, com um x e um y aleatório na grelha
# Se a comida for comida o 3º valor passa de False para True
def genComida():
    comida = [
        BLOCO * random.randint(0, GRELHA - 1),
        BLOCO * random.randint(1, GRELHA - 1),
        False,
    ]

    return comida


# Para quanndo a cobra morre
def morre():
    font = pygame.font.SysFont("opensans.ttf", 100)
    text_morreste = font.render("Morreste", True, "black", "white")

    morreste_rect = text_morreste.get_rect()
    morreste_rect.x = screen.get_width() / 2 - morreste_rect.width / 2
    morreste_rect.y = screen.get_height() / 2 - morreste_rect.height / 2

    screen.blit(text_morreste, morreste_rect)

    return False


# Mostrar as pontuações
def pontuacao():
    aqui = True
    while aqui:
        # Limpa a janela e criar a fonte para escrever as pontuações
        screen.fill("white")
        font = pygame.font.SysFont("opensans.ttf", 30)

        # Se houver pontuações escreve-as
        if len(pontuacoes) > 0:
            # Organizar a lista de pontuações descendentemente
            for i in range(0, len(pontuacoes)):
                for j in range(0, len(pontuacoes) - i - 1):
                    if pontuacoes[j][1] < pontuacoes[j + 1][1]:
                        temp = pontuacoes[j]
                        pontuacoes[j] = pontuacoes[j + 1]
                        pontuacoes[j + 1] = temp

            # Escrever as pontuações por ordem e deixar um espaço
            for i in range(0, len(pontuacoes)):
                texto = (
                    "#"
                    + str(i + 1)
                    + ": "
                    + pontuacoes[i][0]
                    + " ("
                    + str(pontuacoes[i][1])
                    + " pontos)"
                )
                text = font.render(texto, True, "black")
                text_rect = text.get_rect()
                text_rect.x = screen.get_width() / 2 - text_rect.width / 2
                text_rect.y = i * 20
                screen.blit(text, text_rect)

        # Se não existirem pontuações então apresenta uma mensagem ao jogador
        else:
            text = font.render("Sem pontuações ainda, joguem um pouco!!", True, "black")
            screen.blit(text, text.get_rect())

        # Atualiza a janela
        pygame.display.flip()

        # Para fechar o jogo ou voltar para o menu inicial
        while True:
            # Espera que alguma coisa aconteça
            event = pygame.event.wait()

            # Fecha o jogo se carregar no X
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame_menu.events.QUIT

            # Volta para o menu principal se carregarmos numa tecla qualquer
            if event.type == pygame.locals.KEYDOWN:
                aqui = False
                break


# Começa o jogo
def jogar():
    # Define que o jogo está a decorrer (a cobra está viva)
    running = True

    # Uma comida vai aparecer num local aleatório
    comida = genComida()

    # Conta os pontos
    pontos = 0

    # Variavel que nos vai dizer onde está o jogador a todos os momentos, o jogador começa no meio do ecrã
    player_pos = pygame.Vector2(
        screen.get_width() / 2, (screen.get_height() + BLOCO) / 2
    )

    # Variáveis de direção
    wants_to = ""
    direction = ""

    # Executa enquanto a cobra está viva
    while running:
        # Fecha o jogo se carregarmos no X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Se a comida for comida então cria uma nova
        if comida[2]:
            comida = genComida()

        # Preencher o fundo do jogo
        screen.fill("white")
        # Desenha a grelha do jogo
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

        # Escrever os pontos e o nome do jogador
        font = pygame.font.SysFont("opensans.ttf", 40)
        text_pontos = font.render("Pontos: " + str(pontos), True, "black")
        text_player = font.render("Player: " + player_input.get_value(), True, "black")
        text_player_rect = text_player.get_rect()
        text_player_rect.x = screen.get_width() - text_player_rect.width

        screen.blit(text_pontos, text_pontos.get_rect())
        screen.blit(text_player, text_player_rect)

        # Carregar as imagens
        imagem_comida = pygame.image.load(
            "imagens/comida/" + comida_input.get_value()[0][0] + ".png"
        )
        cobra = pygame.image.load("imagens/cobra.png")
        screen.blit(imagem_comida, (comida[0], comida[1]))
        screen.blit(cobra, (player_pos[0], player_pos[1]))

        # Se a posição do jogador for igual à da comida então a comida é comida e o jogador ganha 1 ponto
        if comida[0] == player_pos[0]:
            if comida[1] == player_pos[1]:
                comida[2] = True
                pontos += 1

        # Se o jogador usar as teclas a cobra vai querer ir na direção escolhida
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and wants_to != "BAIXO":
            wants_to = "CIMA"
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and wants_to != "CIMA":
            wants_to = "BAIXO"
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and wants_to != "DIREITA":
            wants_to = "ESQUERDA"
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and wants_to != "ESQUERDA":
            wants_to = "DIREITA"

        # A cobra apenas se movimenta na direção escolhida se estiver num bloco da grelha
        if wants_to == "CIMA" and player_pos[0] % BLOCO == 0:
            direction = wants_to
        elif wants_to == "BAIXO" and player_pos[0] % BLOCO == 0:
            direction = wants_to

        if wants_to == "ESQUERDA" and player_pos[1] % BLOCO == 0:
            direction = wants_to
        elif wants_to == "DIREITA" and player_pos[1] % BLOCO == 0:
            direction = wants_to

        # Movimentação da cobra
        step = 3
        if direction == "CIMA":
            player_pos[1] -= step
        elif direction == "BAIXO":
            player_pos[1] += step
        elif direction == "ESQUERDA":
            player_pos[0] -= step
        elif direction == "DIREITA":
            player_pos[0] += step

        # Se a cobra tocar nas bordas então morre e a pontuação é adicionada à lista, com o nome do jogador e os seus pontos
        if (
            player_pos[1] < BLOCO
            or player_pos[1] > screen.get_height() - BLOCO
            or player_pos[0] < 0
            or player_pos[0] > screen.get_width() - BLOCO
        ):
            pontuacoes.append((player_input.get_value(), pontos))
            running = morre()

        # Atualiza a imagem, 60 vezes por segundo
        pygame.display.flip()
        clock.tick(60)

    # Quando o jogo acabar, se o jogador clicar no X o jogo fecha, mas se só carregar numa tecla do teclado volta para o menu inicial
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame_menu.events.EXIT
            pygame.quit()

        if event.type == pygame.locals.KEYDOWN:
            break


# Inicia a janela do pygame e define o tamanho dos blocos, o número de blocos da grelha e a resolução da janela
pygame.init()
BLOCO = 30
GRELHA = 16
screen = pygame.display.set_mode((BLOCO * GRELHA, BLOCO * (GRELHA + 1)))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake da mia e da Wakid")

# Cria a lista das pontuações
pontuacoes = []

# Cria o menu e os botões
menu = pygame_menu.Menu(
    "Bem vindo",
    400,
    400,
    theme=pygame_menu.themes.THEME_BLUE,
)

# Nome do jogador
player_input = menu.add.text_input("Nome: ", default="mia")

# Seleção da comida
comida_input = menu.add.selector(
    "Comida: ", [("Morango", 0), ("Laranja", 1), ("Pera", 2), ("Chocolate", 3)]
)
menu.add.button("Pontuação", pontuacao)
menu.add.button("Jogar", jogar)
menu.add.button("Sair", pygame_menu.events.EXIT)

# Abrir o menu
while menu.is_enabled():
    # Preencher o fundo a rosa
    screen.fill((255, 223, 255))

    events = pygame.event.get()

    # Registar os eventos do menu
    menu.update(events)
    menu.draw(screen)
    pygame.display.update()
