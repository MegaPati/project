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
    # text_w = text.get_width()
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
    global positkarti
    flag = 0
    screen.fill('blue')
    all_sprites = pygame.sprite.Group()

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load(os.path.join('data', chelovek))
    sprite.rect = sprite.image.get_rect()

    if positkarti > 0:
        sloy1 = pygame.sprite.Sprite()
        sloy1.image = pygame.image.load(os.path.join('data', 'sloy_1_lev_1_01.gif'))
        sloy1.rect = sprite.image.get_rect()
        sloy1.rect.x = positkarti - 960

        sloy3 = pygame.sprite.Sprite()
        sloy3.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy_01.gif'))
        sloy3.rect = sprite.image.get_rect()
        sloy3.rect.x = positkarti - 960

    if positkarti > -960:
        sloy12 = pygame.sprite.Sprite()
        sloy12.image = pygame.image.load(os.path.join('data', 'sloy_1_lev_1_02.gif'))
        sloy12.rect = sprite.image.get_rect()
        sloy12.rect.x = positkarti

        sloy32 = pygame.sprite.Sprite()
        sloy32.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy_02.gif'))
        sloy32.rect = sprite.image.get_rect()
        sloy32.rect.x = positkarti

    if -1920 < positkarti < 960:
        sloy13 = pygame.sprite.Sprite()
        sloy13.image = pygame.image.load(os.path.join('data', 'sloy_1_lev_1_03.gif'))
        sloy13.rect = sprite.image.get_rect()
        sloy13.rect.x = positkarti + 960

        sloy33 = pygame.sprite.Sprite()
        sloy33.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy_03.gif'))
        sloy33.rect = sprite.image.get_rect()
        sloy33.rect.x = positkarti + 960

    if -2880 < positkarti < 0:
        sloy14 = pygame.sprite.Sprite()
        sloy14.image = pygame.image.load(os.path.join('data', 'sloy_1_lev_1_04.gif'))
        sloy14.rect = sprite.image.get_rect()
        sloy14.rect.x = positkarti + 1920

        sloy34 = pygame.sprite.Sprite()
        sloy34.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy_04.gif'))
        sloy34.rect = sprite.image.get_rect()
        sloy34.rect.x = positkarti + 1920

    if positkarti > 0:
        all_sprites.add(sloy1)

    if positkarti > -960:
        all_sprites.add(sloy12)

    if -1920 < positkarti < 960:
        all_sprites.add(sloy13)

    if -2880 < positkarti < 0:
        all_sprites.add(sloy14)

    all_sprites.add(sprite)

    if positkarti > 0:
        all_sprites.add(sloy3)

    if positkarti > -960:
        all_sprites.add(sloy32)

    if -1920 < positkarti < 960:
        all_sprites.add(sloy33)

    if -2880 < positkarti < 0:
    #    sloy34.image.set_alpha(0)
        all_sprites.add(sloy34)

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
    posit = [200, 760]
    positkarti = 960
    positx = 200
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
                if posit[0] - 7 > 190:
                    if positx > 2880:
                        posit[0] -= 7
                        positx -= 7
                    else:
                        if positx != posit[0]:
                            positkarti += 7
                            positx -= 7
                        else:
                            posit[0] -= 7
                            positx -= 7
                chelovek = 'leftman.png'
            elif pygame.key.get_pressed()[pygame.K_d]:
                if (positx != posit[0] or posit[0] > 960) and positkarti > -1145:
                    positkarti -= 7
                    positx += 7
                else:
                    posit[0] += 7
                    positx += 7
                chelovek = 'rightman.png'
            else:
                chelovek = 'middleman.png'
            game()
