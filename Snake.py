import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,128,0)

dis_width = 600         #width of board
dis_height = 400        #height of board

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snakey Snake!')

clock = pygame.time.Clock()

snake_speed = 15    #speed
snake_block = 10    #block size

font_style = pygame.font.SysFont(None, 30)
score_style = pygame.font.SysFont(None, 30)

def your_score(score):
    value = score_style.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    msg = font_style.render(msg,True,color)
    dis.blit(msg, [dis_width/8, dis_height/3])

def messagescore(msg,color):
    msg = font_style.render(msg,True,color)
    dis.blit(msg, [dis_width/20, dis_height/20])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    
    foodgoodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #food that helps you grow in length
    foodgoody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foodbadx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0    #food that if collected will lose 1 point in length
    foodbady = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foodgreatx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  #food that spawns every 10 seconds and increases length of snake and score by 3
    foodgreaty = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        
        while game_close == True:
            dis.fill(white)
            message("You Lost :( Press Q to quit or R to play again",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()
                        
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
        pygame.draw.rect(dis, blue,[foodgoodx, foodgoody, snake_block, snake_block])    #good food block
        pygame.draw.rect(dis, red, [foodbadx, foodbady, snake_block, snake_block])      #bad food block
        pygame.draw.rect(dis, yellow, [foodgreatx, foodgreaty, snake_block, snake_block])   #great food block

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len (snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close == True

        your_score(Length_of_snake - 1)
        our_snake(snake_block, snake_List)
        
        pygame.display.update()

        #good food change in length of snake
        if x1 == foodgoodx and y1 == foodgoody:
            foodgoodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodgoody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        #bad food ends the game
        if x1 == foodbadx and y1 == foodbady:
            foodbadx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodbady = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            game_close = True

        #great food that changes length in snake by adding 3
        if x1 == foodgreatx and y1 == foodgreaty:
            foodgreatx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  
            foodgreaty = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 3

        clock.tick(snake_speed)
        

    pygame.quit()
    quit()

game_loop()
