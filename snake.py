# Importar o pygame e o random para podermos usá-las
import pygame
import random

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

    # Desenhar no ecrã a cobra (a vermelho) e a fruta (a verde), com um tamanho de 30
    pygame.draw.rect(screen, "red", (player_pos[0], player_pos[1], 30, 30))
    pygame.draw.rect(screen, "green", (comida[0], comida[1], 30, 30))

    # Detetar se a cobra comeu a fruta
    if player_pos[1] < (comida[1] + 15):
      if ((player_pos[0] > comida[0]
           and player_pos[0] < (comida[0] + 15))
          or ((player_pos[0] + 15) > comida[0]
           and (player_pos[0] + 15) < (player_pos[0] + 15))):
           comida[2] = True

    # Receber input do jogador, se clicar no W a cobra vai para cima, no S para baixo, no A para a esquerda e no B para a direita
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 2
    if keys[pygame.K_s]:
        player_pos.y += 2
    if keys[pygame.K_a]:
        player_pos.x -= 2
    if keys[pygame.K_d]:
        player_pos.x += 2

    # Atualizar o ecrã
    pygame.display.flip()

# Quando o jogo sair do ciclo então o programa fecha
pygame.quit()

