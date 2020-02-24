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

dis_width = 600
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snakey Snake!')

clock = pygame.time.Clock()

snake_speed = 10
snake_block = 20

font_style = pygame.font.SysFont(None, 30)

def message(msg,color):
    msg = font_style.render(msg,True,color)
    dis.blit(msg, [dis_width/8, dis_height/3])

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0
    y1_change = 0
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

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
        pygame.draw.rect(dis, blue,[foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1,y1,snake_block,snake_block])
        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
