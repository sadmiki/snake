import pygame as py
import time
import random


py.init()
dis_width, dis_height = 600, 600
snake_color = py.Color('Green')
food_color = py.Color('Red')
score_color = py.Color('Orange')
background_color = py.Color('Black')
speed = 6
max_speed = 15
size = 30
score = 0
direction = [0, -1]

game_over = False

random.seed()
food_x, food_y = random.randrange(0, dis_width - size, size), random.randrange(0, dis_height - size, size)
x, y = dis_width // 2, dis_height // 2

py.display.set_caption('__S_n_a_k_e__')

font_style = py.font.SysFont(None, 60)
score_font = py.font.SysFont("comicsansms", 40)

dis = py.display.set_mode((dis_width, dis_height))
clock = py.time.Clock()
snake = [(x - size, y - size), (x, y)]


def draw_game_score(score, color):
    value = score_font.render("Score: " + str(score), True, color)
    dis.blit(value, [0, 0])


def draw_snake():
    for element in snake:
        py.draw.rect(dis, snake_color, [element[0], element[1], size - 2, size - 2])


def draw_food():
    py.draw.rect(dis, food_color, [food_x, food_y, size, size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width // 2 - 100, dis_height // 2 - 100])


while not game_over:

    clock.tick(speed)
    for event in py.event.get():
        if event.type == py.QUIT:
            game_over = True

    key = py.key.get_pressed()
    if key[py.K_LEFT] and direction != [1, 0]:
        direction[0] = -1
        direction[1] = 0
    elif key[py.K_RIGHT] and direction != [-1, 0]:
        direction[0] = 1
        direction[1] = 0
    elif key[py.K_UP] and direction != [0, 1]:
        direction[0] = 0
        direction[1] = -1
    elif key[py.K_DOWN] and direction != [0, -1]:
        direction[0] = 0
        direction[1] = 1

    x += direction[0] * size
    y += direction[1] * size

    if (x, y) in snake:
        game_over = True

    snake.append((x, y))

    if x < 0 or y + size > dis_height or x + size > dis_width or y < 0:
        game_over = True

    if snake[-1][0] == food_x and snake[-1][1] == food_y:
        food_x = random.randrange(size, dis_width - size, size)
        food_y = random.randrange(size, dis_height - size, size)
        speed = min(speed + 1, max_speed)
        score += 1
    else:
        del snake[0]

    dis.fill(background_color)
    draw_snake()
    draw_food()
    draw_game_score(score, score_color)
    py.display.update()

message("Game over!!", py.Color('Red'))
py.display.update()
time.sleep(1)
py.quit()
