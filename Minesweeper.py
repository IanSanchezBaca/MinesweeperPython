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
GGImg = pygame.image.load("img\\deathScreen.jpg")
flagImg = pygame.image.load("img\\Flag.png")
flagIcon = pygame.image.load("img\\flagIcon.png")
winImg = pygame.image.load("img\\youWin.png")
smallWinImag = pygame.transform.scale(winImg, (500, 300))
running = True
gameOver = False
fps = pygame.time.Clock()
fps.tick(30)
EASY = [10, 10] # [the size of the grid, the number of bombs]

testing = False

### Functions
def doRevealBombs(size):
    for x in range(size):
        for y in range(size):
            if bombGrid[x][y]:
                revealGrid[x][y] = 1

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

def initNumGrid(bomb_grid): # this grid shows how many bombs are around it
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
    
    # print("\nPrinting numGrid!")
    # for i in range(size):
    #     print(numGrid[i])
    
    return numGrid  

def initFlagGrid(size):
    flagGrid = [[0 for _ in range(size)] for _ in range(size)]
    return flagGrid

def returnPos(): # this is only becuase I don't know how to create local variables without making it equal to something
    return pygame.mouse.get_pos()




### Local variables
## bools
update = False
buttonReleased = True
leave = False
leftClick = False
rightClick = False
lose = False
win = False

## grids
revealGrid = initRevealedGrid(EASY[0])
bombGrid = initBombGrid(EASY[0], EASY[1])
numGrid = initNumGrid(bombGrid)
flagGrid = initFlagGrid(EASY[0])

## numbers and counters
size = len(bombGrid)
pos = returnPos()
flags = EASY[1] # num of flags
counter = 0
winCon = 90

blud = {
    0: pygame.image.load("img\\Numbers\\zero.png"),
    1: pygame.image.load("img\\Numbers\\one.png"),
    2: pygame.image.load("img\\Numbers\\two.png"),
    3: pygame.image.load("img\\Numbers\\three.png"),
    4: pygame.image.load("img\\Numbers\\four.png"),
    5: pygame.image.load("img\\Numbers\\five.png"),
    6: pygame.image.load("img\\Numbers\\six.png"),
    7: pygame.image.load("img\\Numbers\\seven.png"),
    8: pygame.image.load("img\\Numbers\\eight.png"),
    9: pygame.image.load("img\\Numbers\\nine.png"),
    10: pygame.image.load("img\\Numbers\\ten.png")
}

# for x in range(0, size): # going for size rows
#     for y in range(0, size): # going for size colums
#         if bombGrid[x][y]:
#             print ("bomb at ", x, y)

def doRevealRecursive(y,x):
    if revealGrid[y][x]: # if its already revealed return
        return    
    if flagGrid[y][x]: # if theres a flag on it return
        return
    if bombGrid[y][x]: # if its a bomb dont reveal and return
        return

    revealGrid[y][x] = 1 # reveal it if its acceptable
    global counter 
    counter += 1

    if numGrid[y][x]: # if its a number dont reveal others
        return
    
    else:
        if y != 0:
            doRevealRecursive(y-1, x) # up
        if y != 9:
            doRevealRecursive(y+1, x) # down
        if x != 0:
            doRevealRecursive(y, x-1) # left
        if x != 9:
            doRevealRecursive(y, x+1) # right
        if x != 0 and y != 0:
            doRevealRecursive(y-1, x-1) # up-left
        if x != 9 and y != 9:
            doRevealRecursive(y+1, x+1) # down-right
        if x != 9 and y != 0:
            doRevealRecursive(y-1, x+1) # up-right
        if x != 0 and y != 9:
            doRevealRecursive(y+1, x-1) # down-left
    
        

def printMap(): # prints the grid and shid
     for x in range(0, size): # going for size rows
        for y in range(0, size): # going for size colums
            # It was "breaking" when I didn't have the x and y like this.
            if flagGrid[y][x] and not revealGrid[y][x]:
                screen.blit(flagImg, (x * 60, 100+(y*60)))
            elif not revealGrid[y][x]: 
                screen.blit(squareHidden, (x * 60, 100+(y*60))) # you need to do ".blit" to actually print the image to the screen
            else:
                if bombGrid[y][x]:
                    screen.blit(bombImg, (x * 60, 100+(y*60)))
                elif numGrid[y][x]:
                    screen.blit(blud[numGrid[y][x]], (x * 60, 100+(y*60)))

                else:
                    screen.blit(squareShown, (x * 60, 100+(y*60)))

def printFlags(): # prints the number of flags available
    screen.blit(flagIcon, (0,0))
    screen.blit(blud[flags], (60,0))

### Game Loop
while running:
    ### user input
    # leave this like this in case the user closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            leave = True
            break

        #  and buttonReleased:            
        if event.type == pygame.MOUSEBUTTONDOWN and buttonReleased == True:
            if pygame.mouse.get_pressed()[0]:
                pos = returnPos()
                # saves the x and y pos in an "array"
                # pos[0] and pos[1]

                leftClick = True
                update = True
                buttonReleased = False
            
                # # example
                # print("left button clicked")
                # # print("OG pos X: ", pos[0], " Y: ", pos[1])
                # print("clicked: X: ", pos[0]//60, " Y: ", (pos[1]-100)//60)
            
            elif pygame.mouse.get_pressed()[2]:
                pos = returnPos()
                update = True
                buttonReleased = False
                rightClick = True
                
        
        # elif pygame.mouse.get_pressed()[2]:
        #     print("Right button clicked!")

        if event.type == pygame.MOUSEBUTTONUP and buttonReleased == False:
            buttonReleased = True

    if leave:
        break 


    ### update
    ## Change the arrays here
    # if pygame.mouse.get_pressed()[2]:    
    #     print("uhh2: X: ", x, " Y: ", y)
    
    if update:
        x = pos[0]//60
        y = (pos[1]-100)//60
        
        if  (0 <= x <= 9) and (0 <= y <= 9):
            if leftClick:
                if not flagGrid[y][x] and not bombGrid[y][x]:
                    doRevealRecursive(y, x)
                    # revealGrid[y][x] = 1
                    # counter += 1
                leftClick = False

                if bombGrid[y][x] and not flagGrid[y][x]:
                    doRevealBombs(EASY[0])
                    running = False
                    lose = True
                ### end if
            ### end if
            
            elif rightClick:
                if not flagGrid[y][x] and flags and not revealGrid[y][x]:
                    flagGrid[y][x] = 1
                    flags -= 1
                elif flagGrid[y][x]:
                    flagGrid[y][x] = 0
                    flags += 1

                rightClick = False
                # print("flags: ", flags)
            ### end elif
            
            
        # else:
        #     print("out of bounds!")
        
        if testing:
            counter = 90

        if counter == winCon:
            win = True
            running = False

        update = False


        
    

    

    ### render
    screen.fill("cadetblue3")
    printMap()
    printFlags()
    
   
    pygame.display.flip()

    
    if not running:
        if lose: ### displaying the "You died image"
            for i in range(255):
                GGImg.set_alpha(i)
                screen.blit(GGImg, (44, 244))
                pygame.display.flip()
        elif win:
            print("You win!") # temp
            for i in range(255):
                smallWinImag.set_alpha(i)
                screen.blit(smallWinImag, (44, 244))
                pygame.display.flip()
            # should display the win image

    # game closes after screen is clicked when gameover screen is up
    if not running:
        while not gameOver:
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    gameOver = True
                if event.type == pygame.QUIT:
                    gameOver = True


    #############
    ### end while



# print("End.")
pygame.quit()




