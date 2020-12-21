import pygame
from config import sw, sh, bullet_distance, rocket_sprite, bullet_h, bullet_w, bullet_max_speed
from math import sqrt


# Класс снаряда
class Bullet(object):
    def __init__(self, player):
        self.image = rocket_sprite  # Изображение
        self.image = pygame.transform.scale(self.image, (bullet_w, bullet_h))  # Масштабируем
        self.point = player.head  # Точка появления снаряда
        self.x, self.y = self.point  # Присваиваем координаты х у
        self.w = bullet_w  # Ширина снаряда
        self.h = bullet_h  # Длина снаряда
        self.c = player.cosine  # Косинус
        self.s = player.sine  # Синус
        self.xv = self.c * bullet_max_speed  # Вычисляем скорость движения по x
        self.yv = self.s * bullet_max_speed  # Вычисляем скорость движения по у
        self.spawn_x, self.spawn_y = self.point  # Записываем точку появления снаряда для дальнейшего вычисления дистанции

    def move(self):  # Движение снаряда
        self.x += self.xv
        self.y -= self.yv

    def draw(self, win):  # Отображение снаряда
        win.blit(self.image, (self.x, self.y))

    def checkOffScreen(self):  # Провера на вылет за пределы экрана
        if self.x < -50 or self.x > sw or self.y > sh or self.y < -50:  # Если снаряд за пределами экрана
            return True

    def checkDistance(self):  # Проверка на максимальную дистанцию полета снаряда
        if sqrt((self.spawn_x - self.x) ** 2 + (self.spawn_y - self.y) ** 2) > bullet_distance:
            return True
