# Minesweeper.py
# @author: Ian Sanchez Baca
# 
#

import pygame
import random # used to randomly place bombs
import time # only using this for debugging

# print("Initializing pygame.")
pygame.init()
screen = pygame.display.set_mode((600, 800))
grayBG = pygame.image.load("img\GrayBG.png")
squareBig = pygame.image.load("img\square60x60.png")
running = True
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

def initNumGrid(bomb_grid):
    size = len(bomb_grid)
    numGrid = [[0 for _ in range(size)] for _ in range(size)]
    
    # looping through the whole bombGrid
    for i in range(size): 
        for j in range(size):
             # checking if the current bombGrid position has a bomb   
            if bomb_grid[i][j] == 1:            
                for x in range(max(0, i-1), min(size, i+2)): 
                    for y in range(max(0, j-1), min(size, j+2)):
                        # not really sure what min/max are doing
                        # they sort of help so that it doesnt go out of bounds
                        if (x, y) != (i, j):
                            numGrid[x][y] += 1
    
    print("\nPrinting numGrid!")
    for i in range(size):
        print(numGrid[i])
    
    return numGrid  


# temp = initBombGrid(EASY[0], EASY[1])

# initNumGrid(temp)

bombGrid = initBombGrid(EASY[0], EASY[1])
numGrid = initNumGrid(bombGrid)
size = len(bombGrid)

print("Size:", size)

# for i in range(0, size):
#     print(i)

while running:
    # leave this like this in case the user closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # user input

    # update

    # render
    screen.fill("cadetblue3")
    # screen.blit(grayBG, (0, 100))
    
    for i in range(0, size):
        for j in range(0, size):
            screen.blit(squareBig, (i * 60, 100+(j*60)))

    pygame.display.flip()

    
    
    # time.sleep(3)

    ###
    # end while


print("bye bye!")
pygame.quit()



# def newGame():
