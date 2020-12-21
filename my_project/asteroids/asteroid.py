import pygame
import random
from config import sh, sw, asteroid_min_size, asteroid_max_size, asteroid_sprites, asteroid_max_speed


# Класс астероида
class Asteroid(object):
    def __init__(self):
        self.image = random.choice(asteroid_sprites)  # Случайно выбирает изображение астероида из списка
        self.size = random.randrange(asteroid_min_size, asteroid_max_size)  # Выбираем случайный размер астероида
        self.image = pygame.transform.scale(self.image,
                                            (self.size, self.size))  # Масштабируем картинку под нужный размер
        self.w = self.size  # Ширина
        self.h = self.size  # Высота
        # Случайная точка появления за пределами экрана
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint  # Присваиваем х и у

        # Выбор вектора направления полета астероида
        if self.x < sw // 2:  # Если точка Х меньше половины ширины экрана, то летим направо
            self.xdir = 1
        else:
            self.xdir = -1

        if self.y < sh // 2:  # Если точка Н меньше половины высоты экрана, то летим вниз
            self.ydir = 1
        else:
            self.ydir = -1

        self.xv = self.xdir * random.randrange(1, asteroid_max_speed)  # Выбираем случайную скорость по Х
        self.yv = self.ydir * random.randrange(1, asteroid_max_speed)  # Выбираем случайную скорость по У

    def draw(self, win):  # Отображение астероида
        win.blit(self.image, (self.x, self.y))
