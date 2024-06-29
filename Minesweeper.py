# @author: Ian Sanchez Baca
#
#

import pygame
import random # used to randomly place bombs

print("Initializing pygame.")
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = False
EASY = [10, 10] # [the size of the grid, the number of bombs]


def initBombGrid(size, bombs):
    # creating a size x size bomb grid starting with 0
    ## if there is no bomb the tile will be 1
    ## if there is a bomb the tile will be 0
    bombGrid = [[0 for _ in range(size)] for _ in range(size)]

    # creating bombs
    bombsPlaced = 0

    while bombsPlaced < bombs:
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)

        if bombGrid[x][y] == 0:
            bombGrid[x][y] = 1
            bombsPlaced += 1

    print("\nPrinting bombGrid!")
    for i in range(size):
        print(bombGrid[i])

    return bombGrid

def create_number_grid(bomb_grid):
    size = len(bomb_grid)
    number_grid = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            if bomb_grid[i][j] == 1:
                for x in range(max(0, i-1), min(size, i+2)):
                    for y in range(max(0, j-1), min(size, j+2)):
                        if (x, y) != (i, j):
                            number_grid[x][y] += 1
    
    print("\nPrinting numGrid!")
    for i in range(size):
        print(number_grid[i])
    # return number_grid  


temp = initBombGrid(EASY[0], EASY[1])

create_number_grid(temp)


while running:
    # leave this like this in case the user closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # user input

    # update

    # render

print("bye bye!")
pygame.quit()



# def newGame():
