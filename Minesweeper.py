# @author: Ian Sanchez Baca
#
#

import pygame
import random # used to randomly place bombs
import time # only using this for debugging

# print("Initializing pygame.")
pygame.init()
pygame.display.set_caption("Minesweeper_LOL")
screen = pygame.display.set_mode((600, 800))
grayBG = pygame.image.load("img\GrayBG.png")
squareBig = pygame.image.load("img\square60x60.png")
running = True
EASY = [10, 10] # [the size of the grid, the number of bombs]

def initRevealedGrid(size):
     revealedGrid = [[0 for _ in range(size)] for _ in range(size)]
     return revealedGrid

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

def returnPos():
    return pygame.mouse.get_pos()


# temp = initBombGrid(EASY[0], EASY[1])

# initNumGrid(temp)

revealGrid = initRevealedGrid(EASY[0])
bombGrid = initBombGrid(EASY[0], EASY[1])
numGrid = initNumGrid(bombGrid)
size = len(bombGrid)

print("Size:", size)

pos = returnPos()


while running:
    # user input
    # leave this like this in case the user closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # LeftClick = pygame.mouse.get_pressed()[0]
        if pygame.mouse.get_pressed()[0]:            
            pos = returnPos()
            # saves the x and y pos in an "array"
            # pos[0] and pos[1]
            
            # example
            print("left button clicked")
            print("OG pos X: ", pos[0], " Y: ", pos[1])
            print("uhh: X: ", pos[0]//60, " Y: ", (pos[1]-100)//60)


    # update
    ## Change the arrays here

    x = pos[0]//60
    y = (pos[1]-100)//60
    # if pygame.mouse.get_pressed()[2]:    
    #     print("uhh2: X: ", x, " Y: ", y)

    

    # render
    screen.fill("cadetblue3")
    # screen.blit(grayBG, (0, 100))
    
    for x in range(0, size): # going for size rows
        for y in range(0, size): # going for size colums
            screen.blit(squareBig, (x * 60, 100+(y*60)))

    pygame.display.flip()

    
    
    # time.sleep(3)

    ###
    # end while


print("bye bye!")
pygame.quit()



# def newGame():
