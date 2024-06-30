# Minesweeper in python

## Introduction... i guess.
I am using pygame because I was too lazy to set up SDL library for c++.

Thats it. Explanation over.

## Documentation

### 06/28/24
Created a screen on pygame and also created images of the blocks.

### 06/30/24
Figured out how to tell if the user clicked the mouse using "pygame.mouse.get_pressed()"

Also got the x and y position with "pygame.mouse.get_pos()"

(0, 100) is the position of the top left square in easy mode.
Crated a revealed grid which will just be 0 if not revealed or 1 if revealed.

Also added a tittle to the screen.




## Gameplay

#### EASY
* 10x10 board
* 10 bombs randomly spread out
* 10 flags.

#### MEDIUM 
* 18x18 board 
* 40 bombs
* 40 flags

