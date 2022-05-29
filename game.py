from pygame import *

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)

       self.size_x = size_x
       self.size_y = size_y

       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite) :
    # Обработка нажатия клавиш для управления
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0: 
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0: 
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

class Ball(GameSprite):
    def init(self):
        self.colors = ['G', 'Y', 'P']
        self.current_color = 0

    def update(self):
        if self.current_color == len(self.colors) - 1 :
            self.current_color = 0
        else :
            self.current_color += 1
        self.image = transform.scale(image.load('PPBALL' + self.colors[self.current_color] + '.png'), (self.size_x, self.size_y))

win_width = 1000
win_height = 500

display.set_caption("PingPong")

window = display.set_mode((win_width, win_height))
window.fill((0,0,0))

player1 = Player('PPING.png', 1, win_height/2 - 100, 40, 100, 4)
player2 = Player('PPING2.png', 958, win_height/2 - 100, 40, 100, 4)

ball = Ball('PPBALLG.png', 500, win_height/2 - 100, 50, 50, 4)
ball.init()

font.init()
font1 = font.Font(None, 30)

speed_x = 2
speed_y = 2

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill((0, 0, 0))

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2) :
        speed_x *= -1
        ball.update()

    if not finish :
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        player1.update_l()
        player1.reset()
        
        player2.update_2()
        player2.reset()
        
        ball.reset()

    display.update()
    time.delay(5)