import pygame
import os
import sqlite3


def print_results():
    pth = os.getcwd() + "/results.sqlite3"
    cur = sqlite3.connect(pth).cursor()
    results = cur.execute("""SELECT * FROM result""")
    font = pygame.font.Font(None, 50)
    screen.blit(font.render("ТОП-5 лучших игроков", True, (0, 0, 0)), (1920 // 2 + 10, 1080 // 2))
    i = 0
    j = 0
    text_h = 0
    res2 = []
    for res1 in results:
        res2.append([res1[0], res1[1]])
    res2 = sorted(res2, reverse=True, key=lambda x: (int(x[1]), x[0]))
    for res1 in res2[:5]:
        i += 30
        j += 1
        text = font.render((res1[0] + " -- " + str(res1[1])), True, (200, 0, 0))
        text_x = 1920 // 2 - text.get_width() - 20
        text_y = 1080 // 2 - text.get_height()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y + i))
    pygame.draw.line(screen, "black", (1920 // 2, 1080 // 2),
                     (1920 // 2, 1080 // 2 + text_h * j), 3)


def load_questions():
    pth = os.getcwd() + "/quesions.sqlite3"
    cur = sqlite3.connect(pth).cursor()
    results = cur.execute("""SELECT * FROM question""")
    s = []
    for res2 in results:
        s.append([res2[1], res2[-1]])
    return s


def get_click(pos):
    global flag2
    if 708 < pos[0] < 1212 and 365 < pos[1] < 515:
        flag2 = 0
        screen.fill('blue')
        game()
    if 540 < pos[0] < 1380 and 565 < pos[1] < 715:
        records()


class Question(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites_questions, question):
        super().__init__(sprites_questions)
        self.image = pygame.Surface((2 * 10, 2 * 10), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("white"), (1, 1), 1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.x = x
        self.rect.y = y
        self.question = question[0]
        self.right = question[1]
        self.answer = -1

    def update_status(self, answer):
        if answer == -1:
            self.image = pygame.image.load(os.path.join('data', 'good_luck.png'))
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = 700
        if answer == 0:
            pass  # wrong
        else:
            pass  # right


def game():
    global flag
    global posit
    global flag2
    global positkarti
    flag = 0
    screen.fill('blue')
    all_sprites = pygame.sprite.Group()
    sprites_questions = pygame.sprite.Group()
    print(positkarti, posit[0])
    questions = load_questions()

    good_luck = Question(positkarti - 960 + 750, 700, sprites_questions, ["GoodLuck!", 1])
    if (posit[0] > good_luck.rect.x - 100) and (posit[0] < good_luck.rect.x + 50):
        good_luck.update_status(-1)

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load(os.path.join('data', chelovek))
    sprite.rect = sprite.image.get_rect()

    if positkarti > 0:
        sloy1 = pygame.sprite.Sprite()
        sloy1.image = pygame.image.load(os.path.join('data', 'sloy_1_lev_1_01.gif'))
        sloy1.rect = sprite.image.get_rect()
        sloy1.rect.x = positkarti - 960

        que0 = Question(positkarti - 960 + 1200, 700, sprites_questions, questions[0])
        if 700 < positkarti < 800:
            que0.update_status(que0.answer)
        que1 = Question(positkarti - 960 + 1600, 700, sprites_questions, questions[1])
        if 300 < positkarti < 400:
            que1.update_status(que1.answer)

        sloy3 = pygame.sprite.Sprite()
        sloy3.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy_01.gif'))
        sloy3.rect = sprite.image.get_rect()
        sloy3.rect.x = positkarti - 960

    if positkarti > -960:
        sloy12 = pygame.sprite.Sprite()
        sloy12.image = pygame.image.load(os.path.join('data', 'sloy_1_lev_1_02.gif'))
        sloy12.rect = sprite.image.get_rect()
        sloy12.rect.x = positkarti

        que2 = Question(positkarti - 960 + 2000, 700, sprites_questions, questions[2])
        if -100 < positkarti < 0:
            que2.update_status(que2.answer)
        que3 = Question(positkarti - 960 + 2400, 700, sprites_questions, questions[3])
        if -500 < positkarti < -400:
            que3.update_status(que3.answer)

        sloy32 = pygame.sprite.Sprite()
        sloy32.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy_02.gif'))
        sloy32.rect = sprite.image.get_rect()
        sloy32.rect.x = positkarti
        if 900 < posit[0] and positkarti > 0:
            sloy32.rect.y = -10000

    if -1920 < positkarti < 960:
        sloy13 = pygame.sprite.Sprite()
        sloy13.image = pygame.image.load(os.path.join('data', 'sloy_1_lev_1_03.gif'))
        sloy13.rect = sprite.image.get_rect()
        sloy13.rect.x = positkarti + 960

        que4 = Question(positkarti - 960 + 2800, 700, sprites_questions, questions[2])
        if -900 < positkarti < -800:
            que4.update_status(que4.answer)
        que5 = Question(positkarti - 960 + 3180, 700, sprites_questions, questions[3])
        if (positkarti == -958) and (1150 < posit[0] < 1250):
            que5.update_status(que5.answer)

        sloy33 = pygame.sprite.Sprite()
        sloy33.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy_03.gif'))
        sloy33.rect = sprite.image.get_rect()
        sloy33.rect.x = positkarti + 960
        if -930 < positkarti < 0:
            sloy33.rect.y = -10000

    if -2880 < positkarti < 0:
        sloy14 = pygame.sprite.Sprite()
        sloy14.image = pygame.image.load(os.path.join('data', 'sloy_1_lev_1_04.gif'))
        sloy14.rect = sprite.image.get_rect()
        sloy14.rect.x = positkarti + 1920

        sloy34 = pygame.sprite.Sprite()
        sloy34.image = pygame.image.load(os.path.join('data', 'verkhniy_sloy_04.gif'))
        sloy34.rect = sprite.image.get_rect()
        sloy34.rect.x = positkarti + 1920
        if -1920 < positkarti < -930:
            sloy34.rect.y = -10000

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
        if side == 0:
            sloy3.image.set_alpha(126)
        all_sprites.add(sloy3)

    if positkarti > -960:
        if side == 0:
            sloy32.image.set_alpha(126)
        all_sprites.add(sloy32)

    if -1920 < positkarti < 960:
        if side == 0:
            sloy33.image.set_alpha(126)
        all_sprites.add(sloy33)

    if -2880 < positkarti < 0:
        if side == 0:
            sloy34.image.set_alpha(126)
        all_sprites.add(sloy34)

    sprite.rect.x = posit[0]
    sprite.rect.y = posit[1]
    all_sprites.draw(screen)
    sprites_questions.draw(screen)
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
    side = 1
    objects1 = 0
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
            if pygame.key.get_pressed()[pygame.K_w]:
                side = 1
            elif pygame.key.get_pressed()[pygame.K_s]:
                side = 0
            if pygame.key.get_pressed()[pygame.K_a]:

                if objects1 == 0:
                    if (450 < positx < 650) and (525 < posit[1] < 760):
                        posit[1] += 7

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

                if objects1 == 0:
                    if ((450 < positx < 650) and (posit[1] > 625)) or ((3350 < positx < 3800) and (posit[1] > 275)):
                        posit[1] -= 8

                if positx + 110 < 3800:
                    if (positx != posit[0] or posit[0] > 960) and positkarti > -955:
                        positkarti -= 7
                        positx += 7
                    else:
                        posit[0] += 7
                        positx += 7
                chelovek = 'rightman.png'
            else:
                chelovek = 'middleman.png'
            game()
