
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Simples com Pygame")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Jogador (quadrado)
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Inimigos (círculos)
enemy_radius = 20
enemy_pos = [random.randint(enemy_radius, WIDTH - enemy_radius),
             random.randint(enemy_radius, HEIGHT - enemy_radius)]
enemy_speed = [random.choice([-3, 3]), random.choice([-3, 3])]

clock = pygame.time.Clock()

def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos
    # Detecta colisão entre quadrado e círculo
    # Aqui, usa a distância entre o centro do círculo e o centro do quadrado
    dx = abs(ex - (px + player_size/2))
    dy = abs(ey - (py + player_size/2))
    if dx > (player_size/2 + enemy_radius):
        return False
    if dy > (player_size/2 + enemy_radius):
        return False
    if dx <= (player_size/2):
        return True
    if dy <= (player_size/2):
        return True
    corner_dist_sq = (dx - player_size/2)**2 + (dy - player_size/2)**2
    return corner_dist_sq <= enemy_radius**2

# Loop principal do jogo
running = True
while running:
    clock.tick(30)  # 30 frames por segundo
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed
    
    # Movimento do inimigo
    enemy_pos[0] += enemy_speed[0]
    enemy_pos[1] += enemy_speed[1]

    # Inverte a direção se bater na parede
    if enemy_pos[0] <= enemy_radius or enemy_pos[0] >= WIDTH - enemy_radius:
        enemy_speed[0] = -enemy_speed[0]
    if enemy_pos[1] <= enemy_radius or enemy_pos[1] >= HEIGHT - enemy_radius:
        enemy_speed[1] = -enemy_speed[1]

    # Detecta colisão
    if detect_collision(player_pos, enemy_pos):
        print("Você perdeu!")
        running = False
    
    # Desenha tudo
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))
    pygame.draw.circle(screen, RED, enemy_pos, enemy_radius)
    pygame.display.flip()

pygame.quit()
sys.exit()
