import pygame
import sys
from random import randrange

pygame.init()
# display config
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

class player(object):
    def __init__(self):
        self.width, self.height = 20, 20
        self.x, self.y = None, None
        self.body, self.hit = [(randrange(1, 500, 20), randrange(1, 500, 20))], []
        self.point = 0
        self.font = pygame.font.SysFont('futura', 30, False, False)
        self.restart = True

    def draw(self):
        for (x, y) in self.body:
            pygame.draw.rect(win, (255, 255, 255), (x, y, self.width, self.height))

    def win_limit(self):
        if self.body[0][0] >= 500: self.body[0] = ((self.body[0][0] % 500) - 20, self.y)
        elif self.body[0][0] <= 0: self.body[0] = ((self.body[0][0] + 500) + 20, self.y)
        elif self.body[0][1] >= 500: self.body[0] = (self.x, self.body[0][1] % 500 - 20)
        elif self.body[0][1] <= 0: self.body[0] = (self.x, (self.body[0][1] + 500) + 20)

    def die(self):
        pygame.time.delay(1000)
        self.point = 0
        self.body.clear()
        self.body = [(randrange(1, 500, 20), randrange(1, 500, 20))]

class Food(object):
    def __init__(self, x=None, y=None):
        self.x, self.y = x, y
        self.width, self.height = 20, 20

    def new_position(self):
        self.x, self.y = randrange(1, 500, 20), randrange(1, 500, 20)

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

snake = player()
food = Food()
food.new_position()
move = (20, 0)

def redraw():
    win.fill((0, 0, 0))  # filling all of the previous movements

    food.draw()
    snake.draw()
    win.blit(snake.font.render('Points: ' + str(snake.point), True, (255, 255, 255)), (400, 0))

    pygame.display.update()

while 1:  # mainloop
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN: # processing user input
            snake.restart = True
            if snake.restart:
                if event.key == pygame.K_UP: move = (0, -20)
                elif event.key == pygame.K_DOWN: move = (0, 20)
                elif event.key == pygame.K_LEFT: move = (-20, 0)
                elif event.key == pygame.K_RIGHT: move = (20, 0)

    snake.body[0] = (snake.body[0][0] + move[0], snake.body[0][1] + move[1])  # getting movements
    snake.body.insert(0, snake.body[0])  # constantly add more body
    snake.x, snake.y = snake.body[0][0], snake.body[0][1]

    if snake.body[0] == (food.x, food.y):
        food.new_position()
        if len(snake.body) >= 5:
            snake.point += 1
    else:
        if len(snake.body) >= 5:
            snake.body.pop()  # constantly deleting body, so its not visible

    snake.hit = snake.body[2:]  # separating the head and the body
    for i in range(len(snake.hit)):
        if snake.body[0] == snake.hit[i]:
            snake.die()

    snake.win_limit()

    redraw()