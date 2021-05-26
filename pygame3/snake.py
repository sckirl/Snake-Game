import pygame
import sys
import random
from time import sleep
pygame.init()

# display config
win_x = 500
win_y = 500
win = pygame.display.set_mode((win_x,  win_y))
pygame.display.set_caption("Snake game")

# global config
clock = pygame.time.Clock()
start = False
right = False
left = False
up = False
down = False
x = 250
y = 250
food_x = 300
food_y = 300
point = 0

# player class
class player(object):
    def __init__(self, x1, y1, width, height):
        self.x = x1
        self.y = y1
        self.width = width
        self.height = height
        self.point = 0
        self.die = False
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.font = pygame.font.SysFont('comicsans', 50, False, False)
        self.font2 = pygame.font.SysFont('comicsans', 30, False, False)
        self.point = self.font.render(str(point), True, (255, 255, 255))
        self.text = self.font2.render("Press any key to restart", True, (255, 255, 255))

    def game_over(self):
        win.fill((0, 0, 0))
        win.blit(self.point, (250, 250))
        win.blit(self.text, (150, 300))
        print("score", point)
        sys.exit()

    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), self.rect)

# thing to interact with (the food)
class projectile(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.hit = False

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), self.rect)

# drawing all objects into display
def reDraw():
    win.fill((0, 0, 0))

    food.draw()
    snake.draw()
    if snake.die:
        snake.game_over()

    pygame.display.update()


# main loop
while 1:
    # fill the classes
    snake = player(x, y, 20, 20)
    food = projectile(food_x, food_y, 10, 10)

    clock.tick(10)

    # getting user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            start = True
            if start:
                if event.key == pygame.K_LEFT:
                    left = True
                    right = False
                    up = False
                    down = False
                elif event.key == pygame.K_RIGHT:
                    left = False
                    right = True
                    up = False
                    down = False
                elif event.key == pygame.K_UP:
                    left = False
                    right = False
                    up = True
                    down = False
                elif event.key == pygame.K_DOWN:
                    left = False
                    right = False
                    up = False
                    down = True

    if not start:   # idle movements
        x += 20
    elif right: # repeating movements from user input
        x += 20
    elif left:
        x -= 20
    elif up:
        y -= 20
    elif down:
        y += 20

    # collision detection
    if snake.rect.colliderect(food.rect):
        food_x = random.randrange(1, 500)
        food_y = random.randrange(1, 500)
        point += 1

    elif snake.x + snake.width >= win_x or snake.x <= 0:
        snake.die = True
    elif snake.y - snake.height >= win_y or snake.y + snake.height <= 0:
        snake.die = True

    reDraw()