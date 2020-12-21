import pygame
from config import explosions


# Класс взрыва
class Explosion(pygame.sprite.Sprite):
    def __init__(self, asteroid):
        super(Explosion, self).__init__()
        self.x = asteroid.x  # Получаем координату Х астероида который должен взорваться
        self.y = asteroid.y  # Получаем координату У астероида который должен взорваться
        self.size = asteroid.size  # Получаем размер астероида
        self.images = explosions  # Загружаем из config.py анимацию взрыва
        self.index = 0  # начальный кадр анимации
        self.image = self.images[self.index]  # Устанавливаем начальный кадр
        self.rect = pygame.Rect(asteroid.x, asteroid.y, asteroid.size,
                                asteroid.size)  # создаем прямоугольник по размеру астероида

    def draw(self, win):  # отрисовка взрыва
        self.index += 1  # меняем кадры
        if self.index >= len(self.images):  # если анимацию закончилась, то удаляем объект
            self.kill()
        else:  # если текущий кадр не последний, то оттображаем новый кадр
            self.image = self.images[self.index]
            self.image = pygame.transform.scale(self.image,
                                                (self.size, self.size))  # масштабируем изображение по размеру астероида
            win.blit(self.image, (self.x, self.y))
