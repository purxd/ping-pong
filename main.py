from pygame import *


# базовый класс для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, image_file, x, y, speed, size_x, size_y):
        super().__init__()  
        self.image = transform.scale(image.load(image_file), (size_x, size_y))  
        self.speed = speed  
        self.rect = (self.image.get_rect())  
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# класс для игрока
class Player(GameSprite):  
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 150:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < height - 150:
            self.rect.y += self.speed


# размеры окна
width = 600
height = 500

# создание окна
window = display.set_mode((width, height))
display.set_caption("Ping Pong")
back = (200, 255, 255)  # цвет заливки для фона
window.fill(back)  # заливка фона

# внутриигровые часы и ФПС
clock = time.Clock()
FPS = 60

# шрифт и надписи
font.init()
font1 = font.SysFont("Arial", 36)
lose1 = font1.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font1.render("PLAYER 2 LOSE!", True, (180, 0, 0))

""" Создание спрайтов """
# левая ракетка (Игрок №1)
racket1 = Player("racketka.png", 30, 200, 4, 50, 150)
# правая ракетка (Игрок №2)
racket2 = Player("racketka.png", 520, 200, 4, 50, 150)
# мяч
ball = GameSprite("ball.png", 200, 200, 4, 50, 50)

ball_x = 3
ball_y = 3

# переменная окончания игры
finish = False  # когда True, то спрайты перестают работать
game = True  # завершается при нажатии кнопки закрыть окно
