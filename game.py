import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Jéssica')

clock = pygame.time.Clock()

snake_block = 10
speed = 10

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 30)


def score_display(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, (0, 0))


def player(snake_block, snake_body):
    for x in snake_body:
        pygame.draw.rect(dis, black, (x[0], x[1], snake_block, snake_block))


def message(msg, color):
    messg = font_style.render(msg, True, color)
    dis.blit(messg, [dis_width / 6, dis_height / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_body = []
    length_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
    food_y = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10

    while not game_over:

        while game_close:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score_display(length_snake - 1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_body.append(snake_head)

        if len(snake_body) > length_snake:
            del snake_body[0]

        for x in snake_body[:-1]:
            if x == snake_head:
                game_close = True
        player(snake_block, snake_body)
        score_display(length_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Yummy!!")
            length_snake += 1
        clock.tick(speed)
    pygame.quit()
    quit()


game_loop()
