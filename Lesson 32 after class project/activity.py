import pygame
pygame.init()
display = pygame.display.set_mode((640, 480))
pygame.display.set_caption('My first game screen')

RED = (255, 255, 255)
text = pygame.font.Font(None, 36).render('I am a text', True, pygame.Color('black'))
text_rect = text.get_rect(center=(640 // 2, 320))
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      
  display.fill((255, 255, 255))
  
  pygame.draw.rect(display, (128, 0, 128), pygame.Rect(220, 190, 195, 100))

  pygame.draw.circle(display, (255, 0, 0), (100, 100), 30, 3)

  pygame.draw.circle(display, (95, 158, 160), (350, 120), 50)

  pygame.draw.rect(display, (0, 0, 128), pygame.Rect(350, 400, 100, 50), 5)

  display.blit(text, text_rect)

  pygame.display.flip()