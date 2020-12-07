import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
gray = (240, 240, 240)
red = (213, 50, 80)
green = (0, 150, 0)
lime = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
max_score = 0
start = False

font_style = pygame.font.SysFont("bahnschrift", 21)
score_font = pygame.font.SysFont("comicsansms", 21)


def Your_score(score):
    value = score_font.render("Очков: " + str(score), True, black)
    dis.blit(value, [5, 0])


def Max_score(score, max_score):
    if score > max_score:
        max_score = score
    return max_score


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color, x,  y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])


def intro():
    """Show the intro screen."""
    dis.fill(white)
    message("Змейка", (255, 179, 0), dis_width/2-25, dis_height/4)
    intro = pygame.image.load("snake1/snake_intro.png")
    intro = pygame.transform.scale(intro, (170, 170))
    intro_rect = intro.get_rect()
    intro_rect.center = (dis_width/2, dis_height/1.4)
    message("Для начала нажмите ПРОБЕЛ...", black, dis_width/2-100, dis_height/5)
    dis.blit(intro, intro_rect)
    pygame.display.flip()

# def start_music():
#     """Start the music"""
#
#     # We define the first song
#     filename = "03 Chibi Ninja.mp3"
#     volume = 5
#
#     # We load the sound
#     pygame.mixer.music.load(filename) #music player
#     pygame.mixer.music.set_volume(volume)
#     pygame.mixer.music.play(-1)
#
#     # We load the sound effects
#     eat_sound = pygame.mixer.Sound("apple-crunch.wav")
#     boom_sound = pygame.mixer.Sound("boom.wav")
#     return eat_sound, boom_sound

def gameLoop():
    game_over = False
    game_close = False
    global max_score

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    intro()
    global start

    while not start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True

    while not game_over:

        while game_close == True:
            dis.fill(gray)
            Your_score(Length_of_snake - 1)
            message("Вы проиграли! Нажмите ПРОБЕЛ чтобы начать заново или Q чтобы выйти", red, dis_width/16, dis_height/2.5)
            message(f"Ваш рекорд: {max_score}", green, dis_width/2.5, dis_height/2.15)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        # food = pygame.image.load("snake1/mushroom.jpg")
        # food = pygame.transform.scale(food, (snake_block, snake_block))
        # food_rect = food.get_rect()
        # pygame.draw.rect(dis, red, food_rect)

        pygame.draw.rect(dis, lime, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        if (Length_of_snake - 1) > max_score:
            max_score = (Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()