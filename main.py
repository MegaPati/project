import pygame
import os
import sqlite3


def print_results():
    pth = os.getcwd() + "/results.sqlite3"
    cur = sqlite3.connect(pth).cursor()
    results = cur.execute("""SELECT * FROM result""")
    font = pygame.font.Font(None, 50)
    screen.blit(font.render("Dodiki", True, (0, 0, 0)), (1920 // 2 + 10, 1080 // 2))
    i = 0
    j = 0
    text_h = 0
    for res1 in results:
        i += 30
        j += 1
        text = font.render((res1[0] + " -- " + str(res1[1])), True, (100, 255, 100))
        text_x = 1920 // 2 - text.get_width()
        text_y = 1080 // 2 - text.get_height()
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y + i))
    pygame.draw.line(screen, "black", (1920 // 2, 1080 // 2),
                     (1920 // 2, 1080 // 2 + text_h * j), 3)


def get_click(pos):
    global flag2
    if 708 < pos[0] < 1212 and 365 < pos[1] < 515:
        flag2 = 0
        screen.fill('blue')
        game()
    if 540 < pos[0] < 1380 and 565 < pos[1] < 715:
        records()


def game():
    global flag
    global posit
    global flag2
    flag = 0
    all_sprites = pygame.sprite.Group()
    if flag2 == 0:
        laysofschool = pygame.sprite.Group()
        sloy1 = pygame.sprite.Sprite()
        sloy1.image = pygame.image.load(os.path.join('data', 'sloy_1.png'))
        sloy1.rect = sloy1.image.get_rect()

        sloy2 = pygame.sprite.Sprite()
        sloy2.image = pygame.image.load(os.path.join('data', 'sredniy_sloy.png'))
        sloy2.rect = sloy2.image.get_rect()

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load(os.path.join('data', chelovek))
    sprite.rect = sprite.image.get_rect()

    if flag2 == 0:
        sloy3 = pygame.sprite.Sprite()
        sloy3.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy.png'))
        sloy3.rect = sloy3.image.get_rect()
        flag2 = 1
        laysofschool.add(sloy1)
        laysofschool.add(sloy2)
        laysofschool.add(sloy3)
        laysofschool.draw(screen)
    #  pygame.draw.line(screen, color, (0, 900), (1920, 900), 3)
    all_sprites.add(sprite)
    sprite.rect.x = posit[0]
    sprite.rect.y = posit[1]
    all_sprites.draw(screen)
    pygame.display.flip()


def records():
    global flag
    screen.fill('black')
    ress = pygame.sprite.Group()
    schooll = pygame.sprite.Sprite()
    schooll.image = pygame.image.load(os.path.join('data', 'school.jpg'))
    schooll.rect = schooll.image.get_rect()
    ress.add(schooll)
    ress.draw(screen)
    flag = 2
    print_results()
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1920, 1080))
    color = pygame.Color(255, 0, 0)
    hsv = color.hsva
    posit = [200, 700]
    chelovek = 'middleman.png'
    color.hsva = (180, hsv[2], hsv[2] * 0, hsv[3])
    pygame.draw.rect(screen, color, (708, 365, 504, 150), 3)
    pygame.draw.rect(screen, color, (540, 565, 840, 150), 3)

    schools = pygame.sprite.Group()

    school = pygame.sprite.Sprite()
    school.image = pygame.image.load(os.path.join('data', 'school.jpg'))
    school.rect = school.image.get_rect()

    play = pygame.sprite.Sprite()
    play.image = pygame.image.load(os.path.join('data', 'играть.png'))
    play.rect = school.image.get_rect()
    play.rect.x = 708
    play.rect.y = 365

    res = pygame.sprite.Sprite()
    res.image = pygame.image.load(os.path.join('data', 'результаты.png'))
    res.rect = school.image.get_rect()
    res.rect.x = 540
    res.rect.y = 565

    schools.add(school)
    schools.add(play)
    schools.add(res)
    schools.draw(screen)

    pygame.display.flip()
    running = True
    flag = 1
    flag2 = 1
    while running:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag == 1:
                    get_click(event.pos)
        if flag == 0:
            if pygame.key.get_pressed()[pygame.K_a]:
                posit[0] -= 4
                chelovek = 'leftman.png'
            elif pygame.key.get_pressed()[pygame.K_d]:
                posit[0] += 4
                chelovek = 'rightman.png'
            else:
                chelovek = 'middleman.png'
            game()
