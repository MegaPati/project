import pygame
import os
import sys


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill((0, 0, 0))
    running = True
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load(os.path.join('data', 'arrow.png'))
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    pos = (0, 0)
    while running:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
        sprite.rect.x = pos[0]
        sprite.rect.y = pos[1]
        screen.fill((0, 0, 0))
        if pos[0] != 0 and pos[1] != 0:  
            all_sprites.draw(screen)
        pygame.display.flip()
        
