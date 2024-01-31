import sys, pygame
from src.logger import ColoredLogger
from src.settings import get_setting

logger = ColoredLogger(name="game")
logger.debug("Pygame is initializng")

pygame.init()

WINDOW_SIZE = pygame.Vector2(
    get_setting("window.size")[0], get_setting("window.size")[1]
)
BLACK = pygame.Color(0, 0, 0)

pygame.display.set_caption("TEMPEST")
window_surface = pygame.display.set_mode((WINDOW_SIZE.x, WINDOW_SIZE.y))

background = pygame.Surface((WINDOW_SIZE.x, WINDOW_SIZE.y))
background.fill(BLACK)

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()