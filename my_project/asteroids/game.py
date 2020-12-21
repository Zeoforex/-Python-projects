import pygame
from config import *
from asteroid import Asteroid
from bullet import Bullet
from spaceship import Player
from explosion import Explosion

pygame.init()

pygame.display.set_caption(title)  # устанавливаем название
win = pygame.display.set_mode((sw, sh))  # окно
fps_counter = pygame.time.Clock()  # счетчик кадров

gameover = False  # проиграли ли мы

score = 0  # текущие очки
highScore = 0  # рекорд
lives = start_lives


def redrawGameWindow():  # обновление окна
    win.blit(bg, (0, 0))  # задний фон обновляем
    font = pygame.font.SysFont('robo', 30)  # шрифт
    livesText = font.render('Lives left: ' + str(lives), 1, (255, 255, 255))  # отображение жизней
    playAgainText = font.render("Press 'return' to Play Again", 1, (255, 255, 255))  # текст начать сначала
    scoreText = font.render('Score: ' + str(score), 1, (255, 255, 255))  # отображение очков
    highScoreText = font.render('Record: ' + str(highScore), 1, (255, 255, 255))  # отображение рекорда

    player.draw(win)  # отрисовываем игрока
    for a in asteroids:  # отрисовываем все астероиды
        a.draw(win)
    for b in playerBullets:  # отрисовываем все снаряды
        b.draw(win)
    for e in explosions:  # отрисовываем все взрывы
        e.draw(win)

    if gameover:  # если проиграли, то выводим текст
        win.blit(playAgainText, (sw // 2 - playAgainText.get_width() // 2, sh // 2 - playAgainText.get_height() // 2))

    win.blit(scoreText, (sw - scoreText.get_width() - 25, 25))  # обновляем очки
    win.blit(livesText, (25, 25))  # обновляем жизни
    win.blit(highScoreText, (sw - highScoreText.get_width() - 25, 35 + scoreText.get_height()))  # обновлячем рекорд
    pygame.display.update()  # запуск перерисовки жкрана


player = Player()  # объект игрока
playerBullets = []  # список снарядов на сцене
asteroids = []  # список астероидов на сцене
explosions = []  # список взрывов на сцене
count = 0  # счетчик времени

run = True
while run:
    fps_counter.tick(fps)  # привязываемся к ФПС

    count += 1
    if not gameover:
        if count % asteroid_spawn_delay == 0:  # каждые n тиков добавляем новый астероид
            asteroids.append(Asteroid())

        player.updateLocation()  # тороидальное перемещение
        for b in playerBullets:  # обновляем снаряды
            b.move()  # передвигаем снаряд
            if b.checkOffScreen() or b.checkDistance():  # если вышел за экран или пролетел максимальное расстоянме
                playerBullets.pop(playerBullets.index(b))  # то удаляем его

        for a in asteroids:  # проверяем астероиды
            a.x += a.xv  # двигаем астероид по Х
            a.y += a.yv  # двигаем астероид по У
            # Проверяем столкновение игрока и астероида
            if (a.x >= player.x - player.w // 2 and a.x <= player.x + player.w // 2) or (
                    a.x + a.w <= player.x + player.w // 2 and a.x + a.w >= player.x - player.w // 2):
                if (a.y >= player.y - player.h // 2 and a.y <= player.y + player.h // 2) or (
                        a.y + a.h >= player.y - player.h // 2 and a.y + a.h <= player.y + player.h // 2):
                    lives -= 1  # если столкнулись то отнимаем жизнь
                    asteroids.pop(asteroids.index(a))  # удаляем астероид
                    explosions.append(Explosion(a))  # добавляем взрыв

                    asteroids.clear()  # очищаем поле
                    player.respawn()  # возвращем игрока в центр
                    break

            for b in playerBullets:  # проверяем пули
                # проверяем столкновение пули и астероида
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:
                        # если есть столкновение
                        score += score_per_hit  # то прибавлячем очко
                        asteroids.pop(asteroids.index(a))  # удаляем астероид
                        playerBullets.pop(playerBullets.index(b))  # удаляем пулю
                        explosions.append(Explosion(a))  # добавляем взрыв
                        break

        if lives <= 0:  # если закончились жизни то включаем gameover
            gameover = True

        keys = pygame.key.get_pressed()  # получаем список нажатых клавиш
        if keys[pygame.K_LEFT]:  # кнопка влево
            player.turnLeft()
        if keys[pygame.K_RIGHT]:  # кнопка вправо
            player.turnRight()
        if keys[pygame.K_UP]:  # кнопка вверх
            player.accel = 0.2  # добавляем ускорения
            player.isTorque = True  # включаем анимацию огня
            player.moveForward()  # передвигаем корабль
        else:  # если внока не нажата
            player.accel = 0  # ускорение ноль чтоб корабль тормозил
            player.isTorque = False  # выключаем огонь
            player.moveForward()  # передвигаем

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:  # если нажали пробел
            if event.key == pygame.K_SPACE:
                if not gameover:  # если игра идет
                    playerBullets.append(Bullet(player))  # выстрел

            if event.key == pygame.K_RETURN:  # нажимаем return для продолжения игры
                if gameover:
                    gameover = False  # выключаем gameover
                    lives = start_lives  # обновляем жизни
                    asteroids.clear()  # очищаем поле
                    player.distance = 0  # убираем скорость у корабля
                    player.respawn()  # перемещаем в центр

                    if score > highScore:  # если побили рекорд
                        highScore = score  # обновляем
                    score = 0  # обнуляем очки

    redrawGameWindow()  # перерисовываем окно
pygame.quit()
