import pygame
import time
import random

pygame.init()

dis_width = 900
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game')

white = (255, 255, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)
blue = (0, 193, 193)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 128, 0)

snake_block = 30

clock = pygame.time.Clock()
snake_speed = 5

font_style = pygame.font.SysFont("bahnschrift", 45)
score_font = pygame.font.SysFont("comicsansms", 50)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    foodx = float(foodx)
    foody = float(foody)

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press C-Play or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
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

        #if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #    game_close = True

        if x1 < 0:
            x1 = dis_width
        if x1 > dis_width:
            x1 = -30

        if y1 < 0:
            y1 = dis_height
        if y1 > dis_height:
            y1 = -30

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1


        print(x1, "==", foodx, "     ", y1, "==", foody)

        clock.tick(snake_speed)

    message("You Lost", red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()


gameLoop()
