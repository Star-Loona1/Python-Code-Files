import pygame
pygame.init()
window = pygame.display.set_mode((400, 400))

GREEN = (0, 255, 0)
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()

  window.fill((255, 255, 255))

  pygame.draw.circle(window, GREEN, (300, 300), 50)

  pygame.draw.circle(window, GREEN, (100, 100), 50, 3)

  pygame.display.flip()