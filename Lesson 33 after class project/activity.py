import pygame
import random
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT, MOVEMENT_SPEED, FONT_SIZE = 600, 400, 5, 72
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_color = pygame.transform.scale(pygame.image.load('attached_assets/anime_shooting_star_1776700405956.jpeg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's play a game")
font = pygame.font.SysFont('New Times Roman', FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
      super().__init__()
      self.image = pygame.Surface([width, height])
      self.co = self.image.fill(pygame.Color('light coral'))
      pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
      self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
      self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
      self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)

all_sprites = pygame.sprite.Group()
sp1 = Sprite(pygame.Color('turquoise'), 20, 30)
sp1.rect.x, sp1.rect.y = random.randint(0, SCREEN_WIDTH - sp1.rect.width), random.randint(0, SCREEN_HEIGHT - sp1.rect.height)
all_sprites.add(sp1)

sp2 = Sprite(pygame.Color('snow'), 20, 30)
sp2.rect.x, sp2.rect.y = random.randint(0, SCREEN_WIDTH - sp2.rect.width), random.randint(0, SCREEN_HEIGHT - sp2.rect.height)
all_sprites.add(sp2)

running, won = True, False
clock = pygame.time.Clock()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
      running = False

  if not won:
    pressed = pygame.key.get_pressed()
    x_change = (pressed[pygame.K_RIGHT] -pressed[pygame.K_LEFT] * MOVEMENT_SPEED)
    y_change = (pressed[pygame.K_DOWN] -pressed[pygame.K_UP] * MOVEMENT_SPEED)
    sp1.move(x_change, y_change)

  if sp1.rect.colliderect(sp2.rect):
    all_sprites.remove(sp2)
    won = True

  display.blit(background_color, (0, 0))
  all_sprites.draw(display)

  if won:
    win_text = font.render('You won!', True, pygame.Color('snow'))
    display.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2, (SCREEN_HEIGHT - win_text.get_height()) // 2))

  pygame.display.flip()
  clock.tick(90)

pygame.quit()
    