import pygame
import random

pygame.init()  # инициализируем экран в начале кода

white = (255, 255, 255)  # цвет нужен для интро и самой игры
black = (0, 0, 0)  # нужен нам для очков наших
gray = (240, 240, 240)  # нужен для фона при проигрыше
red = (213, 50, 80)  # нужен для цвета текста при проигрыше
green = (0, 150, 0)  # закрашиваю им цвет текста рекорда

dis_width = 600  # задаем параметры нашего экрана
dis_height = 400  # задаем высоту

dis = pygame.display.set_mode((dis_width, dis_height))  # для создания экрана с нашими значениями делаем
pygame.display.set_caption('Змейка')  # можно вывести заголовок

clock = pygame.time.Clock()

snake_block = 10  # размер блока еды и змейки
snake_speed = 25  # скорость нашей змейки
max_score = 0  # изначально у нас будет самым минимальным значением
start = False

font_style = pygame.font.SysFont("bahnschrift", 15)  # отвечает за наш размер букв для старта игры
score_font = pygame.font.SysFont("comicsansms", 21)  # отвечает за наш текст по очкам

# функция для наших очков в игре
def your_score(score):
    value = score_font.render("Очков: " + str(score), True, black)  # наши очки
    dis.blit(value, [5, 0])  # Отрисовка выполняется с помощью метода blit

# функция для максимума очков

def max_score1(score, max_score):
    if score > max_score:
        max_score = score
    return max_score


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])  # рисуем нашу змейку

# функция для показа нашего сообщения
def message(msg, color, x,  y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])


def intro():
    """Показ интро-картинки"""
    dis.fill(white)  # заполняем поле белым цветом
    message("Змейка", (255, 179, 0), dis_width/2-25, dis_height/4)
    intro = pygame.image.load("snake1/snake_intro.png")
    intro = pygame.transform.scale(intro, (170, 170))
    intro_rect = intro.get_rect()
    intro_rect.center = (dis_width/2, dis_height/1.4)
    message("Для начала нажмите ПРОБЕЛ...", black, dis_width/2-100, dis_height/5)
    dis.blit(intro, intro_rect)
    pygame.display.flip()


def load_sprites():
    """Загрузка картинки еды"""

    apple = pygame.image.load("snake1/mushroom.jpg")
    apple = pygame.transform.scale(apple, (snake_block+1, snake_block+1))
    apple_rect = apple.get_rect()

    return apple, apple_rect


def gameloop():
    game_over = False  # изначально будем false, но потом изменяем это значение
    game_close = False  # здесь тоже изначально false, но потом мы изменяем
    global max_score  # максимальный рекорд

    x1 = dis_width / 2  # вводим координаты
    y1 = dis_height / 2  # вводим y также

    x1_change = 0  # Для сохранения изменений координат x создал две новых переменные
    y1_change = 0  # Для сохранения изменений координат y создал две новых переменные

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    intro()
    global start

    while not start:  # пока игра не стартует из-за определенных правил
        for event in pygame.event.get():  # pygame.event.get()- отображает все действия игры
            if event.type == pygame.KEYDOWN:  # связь с клавиатурой
                if event.key == pygame.K_SPACE:  # нажимаем пробел и игра запускается
                    start = True

    while not game_over:  # работаем до окончания игры

        while game_close:
            dis.fill(gray)  # заполнение поля серым
            your_score(length_of_snake - 1)
            message("Нажмите ПРОБЕЛ чтобы играть заново или Q чтобы выйти", red, dis_width/16,
                    dis_height/2.5)
            message(f"Ваш рекорд: {max_score}", green, dis_width/2.5, dis_height/2.15)
            pygame.display.update()  # изменения на экране нашем

            for event in pygame.event.get():  # pygame.event.get()- отображает все действия игры
                if event.type == pygame.KEYDOWN:  # используем keydown чтобы передвигать змейку
                    if event.key == pygame.K_q:  # нажимаем Q и выходим с игры
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameloop()

        for event in pygame.event.get():  # pygame.event.get()- отображает все действия игры
            if event.type == pygame.QUIT:  # нужно чтоб экран закрылся так как если нажмем на крестик он не закроется
                game_over = True  # игра закончена поэтому меня на True
            if event.type == pygame.KEYDOWN:  # используем keydown чтобы передвигать змейку
                if event.key == pygame.K_LEFT:  # двигаемся влево
                    x1_change = -snake_block  # то двигаемся по x влево
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  # двигаемся вправо
                    x1_change = snake_block  # когда в право то оставляем
                    y1_change = 0
                elif event.key == pygame.K_UP:  # двигаемся вверх
                    y1_change = -snake_block  # меняется y координата
                    x1_change = 0
                elif event.key == pygame.K_DOWN:  # двигаемся вниз
                    y1_change = snake_block  # меняется y координата
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # условие если игрок касается границы
            game_close = True  # то проигрывает соответственно

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        food, food_rect = load_sprites()  # загружаем картинки на место еды
        food_rect.x = foodx  # Меняем у объекта еды прямоугольника параметры координат
        food_rect.y = foody  # Меняем у объекта еды прямоугольника параметры координат
        dis.blit(food, food_rect)  # Отображаем еду

        snake_head = list()
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)  # подсчет очков
        if (length_of_snake - 1) > max_score:
            max_score = (length_of_snake - 1)  # проверка и запись рекорда

        pygame.display.update()  # фиксируем изменения наши и применяем их

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            # Рандомно генерим координаты x y для еды
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  #
            # Рандомно генерим координаты x y для еды
            length_of_snake += 1

        clock.tick(snake_speed)  # на каждую секунду должно пройти сток скок у змейки скорость

    pygame.quit()  # закрываем инициализацию в конце
    quit()  # и заканчиваем нашу программу


gameloop()
