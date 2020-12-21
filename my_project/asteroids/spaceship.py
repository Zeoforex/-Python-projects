import pygame
from config import sh, sw, spaceship_sprite, spaceship_move_sprite, player_max_speed, player_radial_speed
import math


# Класс игрока
class Player(object):
    def __init__(self):
        self.img = spaceship_sprite  # загружаем из config изображение
        self.distance = 0  # мгновенная дистанция на который перемещается игрок(скорость)
        self.accel = 0  # ускорение
        self.isTorque = False  # нажат ли газ(кнопка вперед) для воспроизведения анимации огня
        self.w = self.img.get_width()  # получаем ширину корабля по изображению
        self.h = self.img.get_height()  # получаем высоту корабля по изображению
        self.x = sw // 2  # получаем центральную координату х
        self.y = sh // 2  # получаем центральную координату у
        self.angle = 0  # текущий угол поворота
        self.rotatedSurf = pygame.transform.rotate(self.img,
                                                   self.angle)  # тело корабля на которое накладывается картинка
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))  # вычисляем угол поворота
        self.sine = math.sin(math.radians(self.angle + 90))  # вычисляем угол поворота
        self.head = (
        self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)  # точка из которой вылетают снаряды

    def draw(self, win):  # отображение
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):  # поворот налево
        self.angle += player_radial_speed  # скорость поворота берез из config.py
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)  # поворациваем поверхность корабля
        self.rotatedRect = self.rotatedSurf.get_rect()  # генерируем прямоугольник повернутый
        self.rotatedRect.center = (self.x, self.y)  # центр
        self.cosine = math.cos(math.radians(self.angle + 90))  # вычисление угла (координаты)
        self.sine = math.sin(math.radians(self.angle + 90))  # вычисление угла (координаты)
        self.head = (
        self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)  # точка из которой вылетают снаряды

    def turnRight(self):  # аналогично turnLeft
        self.angle -= player_radial_speed
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def moveForward(self):  # Движение вперед
        if self.isTorque:  # если нажата клавишу вперед, то включаем изображение с огнем
            self.img = spaceship_move_sprite
        else:
            self.img = spaceship_sprite

        self.distance += self.accel  # прибавляем ускорение
        if self.distance >= player_max_speed:  # если достигли макс скорости, то нормализуем значение
            self.distance = self.distance / abs(self.distance) * player_max_speed
        if self.accel == 0:  # если нет ускорения, то замедляемся
            self.distance *= 0.92

        self.x += self.cosine * self.distance  # перемещение по Х
        self.y -= self.sine * self.distance  # перемещение по У
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)  # поворачиваем корабль
        self.rotatedRect = self.rotatedSurf.get_rect()  # создаем поверзность
        self.rotatedRect.center = (self.x, self.y)  # находим центральную координату
        self.cosine = math.cos(math.radians(self.angle + 90))  # считаем угол
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)  # точка появления снарядов

    def updateLocation(self):  # тотроидальное перемещение
        if self.x > sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = sw
        elif self.y < -50:
            self.y = sh
        elif self.y > sh + 50:
            self.y = 0

    def respawn(self):  # появление в центре
        self.x = sw / 2
        self.y = sh / 2
