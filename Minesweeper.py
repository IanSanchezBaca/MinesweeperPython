# Minesweeper.py
# @author: Ian Sanchez Baca
# @desc: Using python library pygame to create a minesweeper game
#

import pygame
import random # used to randomly place bombs
import time # only using this for debugging

### Initalization of pygame
pygame.init()
pygame.display.set_caption("Minesweeper_LOL")
screen = pygame.display.set_mode((600, 800))
grayBG = pygame.image.load("img\GrayBG.png")
squareHidden = pygame.image.load("img\square60x60.png")
squareShown = pygame.image.load("img\Revealed60x60.png")
bombImg = pygame.image.load("img\\bomb.png")
running = True
EASY = [10, 10] # [the size of the grid, the number of bombs]

### Functions
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

    # print("\nPrinting bombGrid!")
    # for i in range(size):
    #     print(bombGrid[i])

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

def returnPos(): # this is only becuase I don't know how to create local variables without making it equal to something
    return pygame.mouse.get_pos()




### Local variables
revealGrid = initRevealedGrid(EASY[0])
bombGrid = initBombGrid(EASY[0], EASY[1])
numGrid = initNumGrid(bombGrid)
size = len(bombGrid)
pos = returnPos()
update = False
buttonReleased = True
blud = {
    1: pygame.image.load("img\\Numbers\\one.png"),
    2: pygame.image.load("img\\Numbers\\two.png"),
    3: pygame.image.load("img\\Numbers\\three.png"),
    4: pygame.image.load("img\\Numbers\\four.png"),
    5: pygame.image.load("img\\Numbers\\five.png"),
    6: pygame.image.load("img\\Numbers\\six.png"),
    7: pygame.image.load("img\\Numbers\\seven.png"),
    8: pygame.image.load("img\\Numbers\\eight.png")
}

# for x in range(0, size): # going for size rows
#     for y in range(0, size): # going for size colums
#         if bombGrid[x][y]:
#             print ("bomb at ", x, y)


def printMap():
     for x in range(0, size): # going for size rows
        for y in range(0, size): # going for size colums
            # It was "breaking" when I didn't have the x and y like this.
            if not revealGrid[y][x]: 
                screen.blit(squareHidden, (x * 60, 100+(y*60)))
            else:
                if bombGrid[y][x]:
                    screen.blit(bombImg, (x * 60, 100+(y*60)))
                elif numGrid[y][x]:
                    screen.blit(blud[numGrid[y][x]], (x * 60, 100+(y*60)))

                else:
                    screen.blit(squareShown, (x * 60, 100+(y*60)))




while running:
    # user input
    # leave this like this in case the user closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #  and buttonReleased:            
        if event.type == pygame.MOUSEBUTTONDOWN and buttonReleased == True:
            if pygame.mouse.get_pressed()[0]:
                pos = returnPos()
                # saves the x and y pos in an "array"
                # pos[0] and pos[1]

                update = True
                buttonReleased = False
            
                # example
                print("left button clicked")
                # print("OG pos X: ", pos[0], " Y: ", pos[1])
                print("clicked: X: ", pos[0]//60, " Y: ", (pos[1]-100)//60)
        
        # elif pygame.mouse.get_pressed()[2]:
        #     print("Right button clicked!")

        if event.type == pygame.MOUSEBUTTONUP and buttonReleased == False:
            buttonReleased = True

        


    # update
    ## Change the arrays here
    # if pygame.mouse.get_pressed()[2]:    
    #     print("uhh2: X: ", x, " Y: ", y)
    
    if update:
        x = pos[0]//60
        y = (pos[1]-100)//60
        
        if  (0 <= x <= 9) and (0 <= y <= 9):
            revealGrid[y][x] = 1
        else:
            print("out of bounds!")
        update = False


        
    

    

    # render
    screen.fill("cadetblue3")
    printMap()
    
   
    pygame.display.flip()


    #############
    ### end while


print("End.")
pygame.quit()



# def newGame():
