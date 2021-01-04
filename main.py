import pygame
import os


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_click(self, pos):
        if 708 < pos[0] < 1212 and 365 < pos[1] < 515:
            self.game()
        if 540 < pos[0] < 1380 and 565 < pos[1] < 715:
            self.records()

    def game(self):
        global flag
        global posit
        flag = 0
        screen.fill('black')
        all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load(os.path.join('data', 'middleman.jpg'))
        sprite.rect = sprite.image.get_rect()
        all_sprites.add(sprite)
        pygame.draw.line(screen, color, (0, 900), (1920, 900), 3)
        sprite.rect.x = posit[0]
        sprite.rect.y = posit[1]
        all_sprites.draw(screen)
        pygame.display.flip()

    def records(self):
        global flag
        flag = 0
        screen.fill('blue')
        pygame.display.flip()
        pass


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    menu = Menu(1920, 1080)
    screen = pygame.display.set_mode((1920, 1080))
    color = pygame.Color(255, 0, 0)
    hsv = color.hsva
    posit = [200, 700]
    color.hsva = (180, hsv[2], hsv[2] * 0.5, hsv[3])
    pygame.draw.rect(screen, color, (708, 365, 504, 150), 3)
    pygame.draw.rect(screen, color, (540, 565, 840, 150), 3)
    pygame.display.flip()
    running = True
    flag = 1
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag == 1:
                    menu.get_click(event.pos)
            if event.type == pygame.KEYUP:
                if flag == 0:
                    print(posit)
                    if event.key == pygame.K_LEFT:
                        if posit[0] - 10 > 0:
                            posit[0] -= 10
                    elif event.key == pygame.K_RIGHT:
                        posit[0] += 10
                    Menu.game