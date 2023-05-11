import sys

import pygame as p
import time
import math


class Cat(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 60
        self.y = HEIGHT / 2
        self.vel = 5
        self.width = 100
        self.height = 50

        # IMAGES

        self.cat1 = p.image.load('Cat1.jpg')
        self.cat2 = p.image.load('Cat2.jpg')
        self.cat1 = p.transform.scale(self.cat1, (self.width, self.height))
        self.cat2 = p.transform.scale(self.cat2, (self.width, self.height))

        self.image = self.cat1
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)

    def update(self):
        self.movement()
        self.correction()
        self.checkCollision()
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            self.x -= self.vel
            self.image = self.cat2

        elif keys[p.K_RIGHT]:
            self.x += self.vel
            self.image = self.cat1

        if keys[p.K_UP]:
            self.y -= self.vel

        elif keys[p.K_DOWN]:
            self.y += self.vel


    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2

    def checkCollision(self):
        car_check = p.sprite.spritecollide(self, car_group, False, p.sprite.collide_mask)
        for car in car_check:
            distance = ((car.x - self.x) ** 2 + (car.y - self.y) ** 2) ** 0.5
            if (distance < 90):
                explosion.explode(self.x, self.y)


class Car(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()

        self.y = HEIGHT / 2
        self.width = 100
        self.height = 150

        if number == 1:
            self.x = 190
            self.image = p.image.load('blue.png')
            self.vel = 1
        if number == 2:
            self.x = 450
            self.image = p.image.load('red.png')
            self.vel = -0.5
            self.radius = 155
            self.degree = 0
        if number == 3:
            self.x = 320
            self.image = p.image.load('red.png')
            self.vel = 2
        if number == 4:
            self.x = 220
            self.image = p.image.load('blue.png')
            self.vel = 1
            self.radius = 55
            self.degree = 0
        if number == 5:
            self.image = p.image.load('blue.png')
            self.velx = 2
            self.vely = 2
            self.x = 100
            self.y = self.height / 2 + 20
        if number == 6:
            self.image = p.image.load('red.png')
            self.velx = 2
            self.vely = 2
            self.x = 420
            self.y = self.height / 2 + 20
        if number == 7:
            self.image = p.image.load('red.png')
            self.velx = 1
            self.vely = 1
            self.x = 420
            self.y = self.height / 2 + 20

        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)
        self.movementType = 0

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        if self.movementType == 0:
            self.moveUpDown()
        elif self.movementType == 1:
            self.moveLeftRight()
        elif self.movementType == 2:
            self.moveCos()
        elif self.movementType == 3:
            self.dvd()

    def moveUpDown(self):
        self.y += self.vel
        # BOTTOM SCREEN CHECK
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1
        # BOTTOM SCREEN CHECK
        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
            self.vel *= -1

    def moveLeftRight(self):
        self.x += self.vel

        # LEFT SCREEN CHECK
        if self.x - self.width / 2 < 0:
            self.vel *= -1
            self.x += self.vel

        # RIGHT SCREEN CHECK
        if self.x + self.width / 2 > WIDTH:
            self.vel *= -1
            self.x += self.vel

    def moveCos(self):
        self.degree += self.vel
        if self.degree == 360:
            self.degree == 0
        self.x = math.cos(math.radians(self.degree)) * self.radius + WIDTH / 2
        self.y = math.sin(math.radians(self.degree)) * self.radius + HEIGHT / 2

    def dvd(self):

        self.x = self.x + self.velx
        self.y = self.y + self.vely

        if self.x + self.width / 2 >= WIDTH:
            self.velx *= -1
            self.x = WIDTH - self.width / 2
        elif self.x - self.width / 2 <= 0:
            self.velx *= -1
            self.x = self.width / 2
        if self.y + self.height / 2 >= HEIGHT:
            self.vely *= -1
            self.y = HEIGHT - self.height / 2
        elif self.y - self.height / 2 <= 0:
            self.vely *= -1
            self.y = self.height / 2


class Screen(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global SCORE

        self.img1 = p.image.load('Scene' + str(SCORE) + '.jpg')
        # self.img1 = p.image.load('Scene0.jpg')
        self.img2 = p.image.load('YouWin.jpg')
        self.img3 = p.image.load('YouLose.jpg')

        self.img1 = p.transform.scale(self.img1, (WIDTH, HEIGHT))
        self.img2 = p.transform.scale(self.img2, (WIDTH, HEIGHT))
        self.img3 = p.transform.scale(self.img3, (WIDTH, HEIGHT))

        self.image = self.img1
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)


class Flag(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        self.number = number

        if self.number == 1:
            self.image = p.image.load('GreenFlag.jpg')
            self.visible = False
            self.x = 50

        else:
            self.image = p.image.load('WhiteFlag.jpg')
            self.visible = True
            self.x = 580

        self.y = HEIGHT / 2
        self.image = p.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)

    def update(self):
        if self.visible:
            self.collision()
            self.rect.center = (self.x, self.y)

    def collision(self):
        global SCORE, cat, POINT

        flag_hit = p.sprite.spritecollide(self, cat_group, False, p.sprite.collide_mask)
        if flag_hit:
            self.visible = False

            if self.number == 1:
                white_flag.visible = True
                if POINT < 5:
                    POINT += 1
                    print("point =", POINT)
                    print("score =", SCORE)
                    speedup()
                    cat.vel += 1

                if SCORE <= 3 and POINT >= 5:
                    SwitchLevel()
                    resetspeed()
                    POINT = 0
                    print("score =", SCORE)
                    if SCORE == 4:
                        print("END")
                        cat_group.empty()
                        DeleteOtherItems()
                        EndScreen(1)
            else:
                green_flag.visible = True


class Explosion(object):
    def __init__(self):
        self.costume = 1
        self.width = 140
        self.height = 140
        self.image = p.image.load('Explosion' + str(self.costume) + '.jpg')
        self.image = p.transform.scale(self.image, (self.width, self.height))

    def explode(self, x, y):
        x = x - self.width / 2
        y = y - self.height / 2
        DeleteCat()

        while self.costume < 9:
            self.image = p.image.load('Explosion' + str(self.costume) + '.jpg')
            self.image = p.transform.scale(self.image, (self.width, self.height))
            win.blit(self.image, (x, y))
            p.display.update()

            self.costume += 1
            time.sleep(0.1)

        DeleteOtherItems()
        EndScreen(0)


def ScoreDisplay():
    global gameOn
    score_font = p.font.SysFont('comicsans', 80, True)
    if gameOn:
        score_text = score_font.render('Level ' + str(SCORE) + ' : ' + str(POINT) + ' / 5', True, (0, 0, 0))
        win.blit(score_text, (30, 10))


def checkFlags():
    for flag in flags:
        if not flag.visible:
            flag.kill()

        else:
            if not flag.alive():
                flag_group.add(flag)


def speedupSLOW():
    if slow_car.vel < 0:
        slow_car.vel -= 0.5
    else:
        slow_car.vel += 0.5


def speedupFAST():
    if fast_car.vel < 0:
        fast_car.vel -= 0.5
    else:
        fast_car.vel += 0.5


def speedupMID():
    if mid_car.vel < 0:
        mid_car.vel -= 1
    else:
        mid_car.vel += 1


def speedupMIDDER():
    if midder_car.vel < 0:
        midder_car.vel -= 1
    else:
        midder_car.vel += 1


def speedupdvd():
    if slow_car.velx < 0:
        slow_car.velx -= 1
    else:
        slow_car.velx += 1

    if slow_car.vely < 0:
        slow_car.vely -= 1
    else:
        slow_car.vely += 1


def speedup():
    global SCORE
    if SCORE == 0:
        speedupSLOW()
        speedupFAST()
    if SCORE == 1:
        speedupFAST()
        speedupSLOW()
        speedupMID()
        # speedupMIDDER()
    if SCORE == 2:
        speedupSLOW()
        speedupFAST()
    if SCORE == 3:
        speedupdvd()


def resetspeed():
    global SCORE
    if SCORE == 1 or SCORE == 2:
        slow_car.vel = -4
        fast_car.vel = 5
        print('slow reset to: ' + str(slow_car.vel))
        print('fast reset to: ' + str(fast_car.vel))
    if SCORE == 3:
        slow_car.velx = 0
        slow_car.vely = 0


def SwitchLevel():
    global SCORE
    if SCORE == 0:
        print("1")
    if SCORE == 1:
        print("2")

    SCORE += 1


def DeleteCat():
    global cat

    cat.kill()
    screen_group.draw(win)
    car_group.draw(win)
    flag_group.draw(win)

    screen_group.update()
    car_group.update()
    flag_group.update()

    p.display.update()


def Deletethisitem():
    car_group.empty()


def DeleteOtherItems():
    car_group.empty()
    flag_group.empty()
    flags.clear()


def EndScreen(n):
    global gameOn

    gameOn = False

    if n == 0:  # màn hình thua
        bg.image = bg.img3


    elif n == 1:  # màn hình thắng
        bg.image = bg.img2


def checkForKeyPress():
    global gameOn
    if not gameOn:
        keys = p.key.get_pressed()
        if keys[p.K_ESCAPE]:
            exit()
        if keys[p.K_SPACE]:
            setgame()


def setgame():
    global gameOn, PREV_SCORE, run, screen_group, win, car_group, cat_group, flag_group, clock, SCORE, flags
    global explosion, green_flag, white_flag, slow_car, fast_car, mid_car, midder_car, cat, bg, POINT
    gameOn = True
    PREV_SCORE = -1
    SCORE = 0
    POINT = 0
    while run:
        if PREV_SCORE != SCORE:
            if SCORE == 0:
                print("sure")
                p.init()

                win = p.display.set_mode((WIDTH, HEIGHT))
                p.display.set_caption('Crossy Road')
                clock = p.time.Clock()

                bg = Screen()
                screen_group = p.sprite.Group()
                screen_group.add(bg)

                cat = Cat()
                cat_group = p.sprite.Group()
                cat_group.add(cat)

                slow_car = Car(1)
                fast_car = Car(2)
                car_group = p.sprite.Group()
                car_group.add(slow_car, fast_car)

                green_flag = Flag(1)
                white_flag = Flag(2)
                flag_group = p.sprite.Group()
                flag_group.add(green_flag, white_flag)
                flags = [green_flag, white_flag]

                explosion = Explosion()
            if SCORE == 1:
                cat_group.empty()
                DeleteOtherItems()

                print("yes sir")
                print("dap an is ", SCORE)
                p.init()

                win = p.display.set_mode((WIDTH, HEIGHT))
                p.display.set_caption('Crossy Road')
                clock = p.time.Clock()

                bg = Screen()
                screen_group = p.sprite.Group()
                screen_group.add(bg)

                cat = Cat()
                cat_group = p.sprite.Group()
                cat_group.add(cat)

                slow_car = Car(1)
                fast_car = Car(2)
                mid_car = Car(3)
                # midder_car = Car(4)
                car_group = p.sprite.Group()
                # car_group.add(slow_car, fast_car, mid_car, midder_car)
                car_group.add(slow_car, fast_car, mid_car)

                green_flag = Flag(1)
                white_flag = Flag(2)
                flag_group = p.sprite.Group()
                flag_group.add(green_flag, white_flag)
                flags = [green_flag, white_flag]

                explosion = Explosion()
            if SCORE == 2:
                cat_group.empty()
                DeleteOtherItems()

                print("hell yeah")
                print("dap an is ", SCORE)
                p.init()

                win = p.display.set_mode((WIDTH, HEIGHT))
                p.display.set_caption('Crossy Road')
                clock = p.time.Clock()

                bg = Screen()
                screen_group = p.sprite.Group()
                screen_group.add(bg)

                cat = Cat()
                cat_group = p.sprite.Group()
                cat_group.add(cat)

                slow_car = Car(6)
                fast_car = Car(2)
                midder_car = Car(4)

                slow_car.movementType = 1
                fast_car.movementType = 2
                midder_car.movementType = 2
                car_group = p.sprite.Group()
                car_group.add(slow_car, fast_car, midder_car)

                green_flag = Flag(1)
                white_flag = Flag(2)
                flag_group = p.sprite.Group()
                flag_group.add(green_flag, white_flag)
                flags = [green_flag, white_flag]

                explosion = Explosion()

            if SCORE == 3:
                # cat_group.empty()
                # DeleteOtherItems()

                print("yes sir")
                print("is not adkhsads ", SCORE)
                p.init()

                win = p.display.set_mode((WIDTH, HEIGHT))
                p.display.set_caption('Crossy Road')
                clock = p.time.Clock()

                bg = Screen()
                screen_group = p.sprite.Group()
                screen_group.add(bg)

                cat = Cat()
                cat_group = p.sprite.Group()
                cat_group.add(cat)

                slow_car = Car(5)
                fast_car = Car(6)
                slow_car.movementType = 3
                fast_car.movementType = 3
                car_group = p.sprite.Group()
                car_group.add(slow_car,fast_car)

                green_flag = Flag(1)
                white_flag = Flag(2)
                flag_group = p.sprite.Group()
                flag_group.add(green_flag, white_flag)
                flags = [green_flag, white_flag]

                explosion = Explosion()

            PREV_SCORE = SCORE
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        screen_group.draw(win)

        ScoreDisplay()
        checkFlags()

        car_group.draw(win)
        cat_group.draw(win)
        flag_group.draw(win)

        car_group.update()
        cat_group.update()
        flag_group.update()

        screen_group.update()

        p.display.update()
        clock.tick(60)
        checkForKeyPress()
    p.quit()


# SET UP
WIDTH = 640
HEIGHT = 500
PREV_SCORE = -1
SCORE= 0
POINT = 0

gameOn = True
run = True

setgame()
