import pygame
from random import choice
# -----------GAME----------------
sw = 800
sh = 800
backgrounds = []
backgrounds.append(pygame.image.load('images/background1.png'))
backgrounds.append(pygame.image.load('images/background2.png'))
backgrounds.append(pygame.image.load('images/background3.png'))
bg = pygame.transform.scale(choice(backgrounds), (sw, sh))

title = 'Asteroids| Vadim & Myrat'
fps = 40
start_lives = 3
asteroid_spawn_delay = 50
score_per_hit = 1

# -----------Explosion----------------
explosions = []
explosions.append(pygame.image.load('images/expl1.png'))
explosions.append(pygame.image.load('images/expl2.png'))
explosions.append(pygame.image.load('images/expl3.png'))
explosions.append(pygame.image.load('images/expl4.png'))
explosions.append(pygame.image.load('images/expl5.png'))
explosions.append(pygame.image.load('images/expl6.png'))
explosions.append(pygame.image.load('images/expl7.png'))
explosions.append(pygame.image.load('images/expl8.png'))
explosions.append(pygame.image.load('images/expl9.png'))
explosions.append(pygame.image.load('images/expl10.png'))
explosions.append(pygame.image.load('images/expl11.png'))
explosions.append(pygame.image.load('images/expl12.png'))

# -----------Bullet----------------
bullet_distance = 400
rocket_sprite = pygame.image.load('images/rocket.png')
bullet_h = 10
bullet_w = 10
bullet_max_speed = 10

# -----------Player----------------
player_max_speed = 5
player_radial_speed = 5
spaceship_sprite = pygame.image.load('images/ship.png')
spaceship_sprite = pygame.transform.rotate(spaceship_sprite, 90)

spaceship_move_sprite = pygame.image.load('images/ship_thrusted.png')
spaceship_move_sprite = pygame.transform.rotate(spaceship_move_sprite, 90)

# -----------Asteroid----------------
asteroid1_sprite = pygame.image.load('images/asteroid1.png')
asteroid2_sprite = pygame.image.load('images/asteroid2.png')
asteroid3_sprite = pygame.image.load('images/asteroid3.png')
asteroid_sprites = [asteroid1_sprite, asteroid2_sprite, asteroid3_sprite]

asteroid_min_size = 40
asteroid_max_size = 80
asteroid_max_speed = 2
