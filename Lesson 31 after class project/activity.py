import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
caption = pygame.display.set_caption(('My first Game Screen'))

image = pygame.image.load('quiz.jpg').convert_alpha()
image_size = pygame.transform.scale(image, (300, 300))
image_rect = image_size.get_rect(center=(800 // 2, 600 // 2))

grey = (58, 58, 58)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    screen.fill(grey)

    screen.blit(image_size, image_rect)

    pygame.display.flip()