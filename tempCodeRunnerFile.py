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

