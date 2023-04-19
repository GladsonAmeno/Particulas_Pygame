import pygame
import random

# DEFINIR CORES
BLACK = (0,0,0)
WHITE = (255,255,255)

#INICIAR O PYGAME
pygame.init()

#DEFINIR O TAMANHO DA TELA
size = (700,500)
screen = pygame.display.set_mode(size)

#TITULO DA TELA
pygame.display.set_caption("Sistema de Particulas")

#DEFINIR A CLASSE PARTICULAS
class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(10, 20)
        self.velocity = [random.randint(-5, 5), random.randint(-5, 5)]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def update(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        if self.pos[0] < 0 or self.pos[0] > size[0]:
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] < 0 or self.pos[0] > size[1]:
            self.velocity[1] = -self.velocity[1]

#CRIANDO LISTA DE PARTICULAS
particles = []

#Main Loop
done = False
clock = pygame.time.Clock()

while not done:
    # --- Main Loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Criando uma nova particula com o clique do mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            particles.append(Particle(list(event.pos)))

    # --- Logica do jogo aqui --- #
    for particle in particles:
        particle.update()

    # --- Codigo de desenho vem aqui --- #
    screen.fill(BLACK)

    for particle in particles:
        particle.draw(screen)

    # --- Atualizar a tela --- #
    pygame.display.flip()

    # --- 60 FPS --- #
    clock.tick(60)

# --- Fechar a janela e sair --- #
pygame.quit()
