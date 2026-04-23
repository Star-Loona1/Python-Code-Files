import pygame
import random
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 600

background_image = pygame.image.load('HD-wallpaper-cloudy-sky-aesthetic-butterflies-clouds-pink-stars.jpg')

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

red = pygame.Color('red')
blue = pygame.Color('blue')
snow = pygame.Color('snow')
khaki = pygame.Color('khaki')
purple = pygame.Color('purple')
powderblue = pygame.Color('powderblue')
palegreen = pygame.Color('palegreen')
mediumaquamarine = pygame.Color('mediumaquamarine')
l1 = [red, blue, snow, khaki, purple, powderblue, palegreen, mediumaquamarine]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite bounce')

class Sprite(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

  def update(self):
    self.rect.move_ip(self.velocity)
    boundary_hit = False
    if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
      self.velocity[0] = -self.velocity[0]
      boundary_hit = True

    elif self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
      self.velocity[1] = -self.velocity[1]
      boundary_hit = True

    if boundary_hit:
      pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
      
  def change_sprite_color(self):
    self.image.fill(random.choice(l1))

all_sprites = pygame.sprite.Group()

sp1 = Sprite(red, 20, 30)
sp1.rect.x = random.randint(0, 680)
sp1.rect.y = random.randint(0, 570)
all_sprites.add(sp1)

sp2 = Sprite(purple, 20, 30)
sp2.rect.x = random.randint(0, 680)
sp2.rect.y = random.randint(0, 570)
all_sprites.add(sp2)

exit = False
clock = pygame.time.Clock()

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = True

    elif event.type == SPRITE_COLOR_CHANGE_EVENT:
      sp1.change_sprite_color()
      sp2.change_sprite_color()

  screen.blit(background_image, (0, 0))
  all_sprites.update()
  all_sprites.draw(screen)

  pygame.display.flip()
  clock.tick(240)

pygame.quit()
