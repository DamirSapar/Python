#Exercise 1
import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
#Coin number counter initialization
NUMBER_OF_COINS=0
#Bonus counter initialization
BONUS=0
#To store the last value NUMBER_OF_COINS
last_coin_count=0
 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("/Users/damirsapar/Downloads/PygameTutorial_3_0/AnimatedStreet.png")
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/damirsapar/Downloads/PygameTutorial_3_0/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 #Initialization of class for coins
class Bonus(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        #Loading coin image
        self.image = pygame.image.load("/Users/damirsapar/Downloads/gold.coin.png")
        #Coin size changes
        self.image = pygame.transform.scale(self.image,(20,20))
        #Transformation into a rectangle
        self.rect = self.image.get_rect()
        #Random coin appearance
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 

      def move(self):
        self.rect.move_ip(0,SPEED)
        #Condition for reappearance and randomness
        if (self.rect.top > 600):
            #Move to the beginning
            self.rect.top = 0
            #The random appearance
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/damirsapar/Downloads/PygameTutorial_3_0/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                        
P1 = Player()
E1 = Enemy()
#Coin initialization
coin=Bonus()
 
enemies = pygame.sprite.Group()
enemies.add(E1)
#Adding to sprite group
gold_coin = pygame.sprite.Group()
gold_coin.add(coin)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin)
 

while True:
       
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    #Show counter in upper ridht corner
    bonus = font_small.render(str(BONUS),True,BLACK)
    DISPLAYSURF.blit(bonus,(370,10))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    
 
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

#Condition when player and coin collide
    collected_coin = pygame.sprite.spritecollideany(P1, gold_coin) 
    if collected_coin:
        pygame.mixer.Sound('/Users/damirsapar/Downloads/a2d4fd123353974.mp3').play()
        BONUS += random.randint(1,5)
        NUMBER_OF_COINS += 1

#Increase speed when picking up every third coin and also if you haven't increased it on this coin
        if NUMBER_OF_COINS%3 == 0 and NUMBER_OF_COINS!=last_coin_count:
            SPEED += 0.5
#Remembering the last increased value
            last_coin_count = NUMBER_OF_COINS

#Moving the coin back
        collected_coin.rect.top = 0
        collected_coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Condition for the coin not to appear on top of the enemy(car)
    if pygame.sprite.spritecollideany(E1, gold_coin):
        coin.rect.top = 0
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('/Users/damirsapar/Downloads/PygameTutorial_3_0/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)



#Execises 2
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Function to generate a random food position
def generate_food(snake_body):
    while True:
        food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
        if food not in snake_body:
            return food

# Main variables
snake = [(100, 100)]
direction = (GRID_SIZE, 0)  # Initial direction to the right
food = generate_food(snake)
#food creation time 
spawn_time=pygame.time.get_ticks()
speed = 10
score = 0
number=0
level = 1

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
#current time
    current_time=pygame.time.get_ticks()
# Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)
    
# Update snake position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

#if 10 seconds pass, the food appears in a new place
    if current_time-spawn_time>=10000:
        food=generate_food(snake)
#new food creation time
        spawn_time=pygame.time.get_ticks()

# Check for collisions with walls or itself
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake):
        running = False
    else:
        snake.insert(0, new_head)
        
# Check if the snake eats the food
        if new_head == food:
            score += random.randint(1,3)
            number+=1
            food = generate_food(snake)
#new food creation time 
            spawn_time=pygame.time.get_ticks()
            
# Level up
            if number % 3 == 0:
                level += 1
                speed += 2
        else:
            snake.pop()
    
# Draw food and snake
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
    
 # Display score and level
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()



#Exercise 3
import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

#Initialization of size,color,shape   
    radius = 15
    mode = 'blue'
    shape = 'circle'  
    points = []
    
    while True:
        pressed = pygame.key.get_pressed()
#Checkinf if ctrl is pressed
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

#Different exit methods       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_s:
                    shape = 'square'
                elif event.key == pygame.K_t:
                    shape = 'triangle'
                elif event.key == pygame.K_i:
                    shape = 'equilateral triangle'
                elif event.key == pygame.K_o:
                    shape = 'rhombus'
                elif event.key == pygame.K_v:
                    shape = 'rectangle'
                elif event.key == pygame.K_e:
                    shape = 'eraser'

#Changes in mouse size and movement                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 1)
                elif event.button == 3: 
                    radius = max(1, radius - 1)
                
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, shape, mode, radius))
                points = points[-256:]
        
        screen.fill((0, 0, 0))
        
        for pos, s, color, size in points:
            drawShape(screen, pos, s, color, size)
        
        pygame.display.flip()
        clock.tick(60)

#Drawing figures
def drawShape(screen, position, shape, color_mode, size):
    colors = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}
    color = colors.get(color_mode, (255, 255, 255))
    
    if shape == 'circle':
        pygame.draw.circle(screen, color, position, size)
    elif shape == 'rectangle':
        pygame.draw.rect(screen, color, (position[0] - size, position[1] - size, size * 2, size * 2))
    elif shape == 'square':
        pygame.draw.rect(screen, color, (position[0] - size, position[1] - size, size * 2, size * 2))
    elif shape == 'triangle':
        pygame.draw.polygon(screen, color, [
            (position[0] - size, position[1] - size),
            (position[0], position[1] - size),
            (position[0] - size, position[1])
        ])
    elif shape == 'equilateral triangle':
        height = math.sqrt(3) / 2 * size
        pygame.draw.polygon(screen, color, [
            (position[0] - size, position[1] - height),
            (position[0] + size, position[1] - height),
            (position[0], position[1] + size)
        ])
    elif shape == 'rhombus':
        pygame.draw.polygon(screen, color, [
            (position[0] - size, position[1] - size),
            (position[0] - size, position[1]),
            (position[0], position[1] + size),
            (position[0] + size, position[1])
        ])
    elif shape == 'eraser':
        pygame.draw.circle(screen, (0, 0, 0), position, size)

main()
