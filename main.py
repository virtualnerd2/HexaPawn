#3 aways to win. Cause no moves, get to the onther side, kill everything
#https://computd.nl/wp-content/uploads/2020/01/1_qAQ0JIQHlf1BPlzXD7_tZA-1.jpeg

#Possible Turn = [[CURRENT STATE], [WEIGHTS], [STARTING POINT], [ENDING POINT]]

import pygame
import time

Two1 = [ [[1,1,1],[2,0,0],[0,2,2]], [1,1,1], [(0,1),(0,1),(0,2)], [(1,0),(1,1),(1,2)] ]
Two2 = [ [[1,1,1],[0,2,0],[2,0,2]], [1,1], [(0,0),(0,0)], [(1,0),(1,1)] ]

TwoStates = [Two1, Two2] 

Four1 = [ [[1,0,1],[1,2,0],[0,0,2]], [1,1,1,1], [(0,0),(0,2),(0,2),(1,1)], [(1,1),(1,1),(1,2),(2,0)] ]
Four2 = [ [[0,1,1],[2,1,0],[0,0,2]], [1,1,1], [(0,1),(0,2),(1,1)], [(1,0),(1,2),(2,1)] ]
Four3 = [ [[1,0,1],[2,2,0],[0,2,0]], [1,1,1], [(0,0),(0,2),(0,2)], [(1,1),(1,1),(1,2)] ]
Four4 = [ [[1,1,0],[2,0,2],[0,0,2]], [1,1,1], [(0,1),(0,1),(0,1)], [(1,0),(1,1),(1,2)] ]
Four5 = [ [[0,1,1],[0,1,2],[2,0,0]], [1,1,1], [(0,1),(1,1),(1,1)], [(1,2),(2,0),(2,1)] ]
Four6 = [ [[0,1,1],[1,2,2],[2,0,0]], [1,1], [(0,1),(0,2)], [(1,2),(1,1)] ]
Four7 = [ [[1,0,1],[1,0,2],[0,2,0]], [1,1], [(1,0),(1,0)], [(2,0),(2,1)] ]
Four8 = [ [[1,1,0],[2,2,1],[0,0,2]], [1,1], [(0,0),(0,1)], [(1,1),(1,0)] ]
Four9 = [ [[0,1,1],[0,2,0],[0,0,2]], [1,1], [(0,2),(0,2)], [(1,1),(1,2)] ]
Four10 =[ [[0,1,1],[0,2,0],[2,0,0]], [1,1], [(0,2),(0,2)], [(1,1),(1,2)] ]
Four11 = [ [[1,0,1], [2,0,0], [0,0,2]], [1], [(0,2)], [(1,2)] ]

FourStates = [Four1, Four2, Four3, Four4, Four5, Four6, Four7, Four8, Four9, Four10, Four11] 

Six1 = [ [[0,0,1],[1,1,2],[0,0,0]], [1,1], [(1,0),(1,1)], [(2,0),(2,1)] ]
Six2 = [ [[1,0,0],[2,2,2],[0,0,0]], [1], [(0,0)], [(1,1)] ]
Six3 = [ [[0,1,0],[1,2,2],[0,0,0]], [1,1], [(0,1),(1,0)], [(1,2),(2,0)] ]
Six4 = [ [[0,1,0],[2,2,1],[0,0,0]], [1,1], [(0,1),(1,2)], [(1,0),(2,2)] ]
Six5 = [ [[1,0,0],[1,1,2],[0,0,0]], [1,1], [(1,0),(1,1)], [(2,0),(2,1)] ]
Six6 = [ [[0,0,1],[2,1,1],[0,0,0]], [1,1], [(1,1),(1,2)], [(2,1),(2,2)] ]
Six7 = [ [[0,0,1],[1,2,0],[0,0,0]], [1,1,1], [(0,2),(0,2),(1,0)], [(1,1),(1,2),(2,0)] ]
Six8 = [ [[0,1,0],[2,1,0],[0,0,0]], [1,1], [(0,1),(1,1)], [(1,0),(2,1)] ]
Six9 = [ [[0,1,0],[0,1,2],[0,0,0]], [1,1], [(0,1),(1,1)], [(1,2),(2,1)] ]
Six10 = [ [[1,0,0],[1,2,0],[0,0,0]], [1,1], [(0,0),(1,0)], [(1,2),(2,0)] ]
Six11 = [ [[0,0,1],[0,2,1],[0,0,0]], [1,1], [(0,2),(1,2)], [(1,1),(2,2)] ]

SixStates = [Six1, Six2, Six3, Six4, Six5, Six6, Six7, Six8, Six9, Six10, Six11] 

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
greyBackground=(203, 206, 203)

width = 125
height = 125
radius = 60
margin = 0
xDistanceFromEdge = 0
gameBoard=[[None]*3 for _ in range(3)] 
windowSize=[375, 375]

pygame.init()
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Draughts Game")
done = False
clock = pygame.time.Clock()

level = 1
newGame=True

def square_colour(row, col):
    return white if (row + col) % 2 == 0 else black  

def boardGui():
    for boardRow in range(3):
        for boardColumn in range(3):
            xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
            yCoordinate=(margin+height) * boardRow + margin
            currentColour = square_colour(boardRow, boardColumn)
            pygame.draw.rect(screen,currentColour,[xCoordinate,yCoordinate, width, height])

def piecesGameBoard(gameBoard):
    if newGame:
        newGameBoard(gameBoard)
    else:
      drawPieces(gameBoard)

def newGameBoard(gameBoard):
    gameBoard[:] = [[1,1,1],[2,0,2],[2,2,2]]
    drawPieces(gameBoard)

def drawPieces(gameBoard):
    for x in range(3):
        for y in range(3):
            xCoordinate=((margin+width) * x + margin+radius)+xDistanceFromEdge
            yCoordinate=(margin+height) * y + margin+radius
            if gameBoard[x][y]==1:
                pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)
            elif gameBoard[x][y]==2:
                pygame.draw.circle(screen,blue,(xCoordinate,yCoordinate),radius)
            elif gameBoard[x][y]==3:
                pygame.draw.circle(screen,yellow,(xCoordinate,yCoordinate),radius)

def checkMove(column, row):
  if(column == 2):
    return "NOT VALID"

  if(row + 1 < 3 and gameBoard[column+1][row+1] == "2"):
    return "UP"
  elif(gameBoard[column+1][row] == "0"):
    return "RIGHT"
  elif(row - 1 >= 0 and gameBoard[column+1][row-1] == "2"):
    return "DOWN"
  else:
    return "NOT VALID"

def renderImage():
  screen.fill(greyBackground)
  boardGui()
  piecesGameBoard(gameBoard)
  clock.tick(60)
  pygame.display.flip()

selected = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            # Change the x/y screen coordinates to grid coordinates
            column = (pos[0]-xDistanceFromEdge) // (width+margin)
            row = pos[1] // (height+margin)
            if(column < len(gameBoard) and row < len(gameBoard[0])):
              print((column, row)) 

            validMove = checkMove(column, row)
            print(validMove)
            print(gameBoard[column][row])
            if(selected == 0 and gameBoard[column][row] == 1):
              gameBoard[column][row] = 3
              selected = 1
            elif(selected == 1 and gameBoard[column][row] == 3):
              gameBoard[column][row] = 1
              selected = 0


            elif(selected == 1 and validMove != "NOT VALID"):
              selected = 0
              if (validMove == "UP"):
                gameBoard[column-1][row-1] = 0
                gameBoard[column][row] = 1
              elif (validMove == "RIGHT"):
                gameBoard[column-1][row] = 0
                gameBoard[column][row] = 1
              elif (validMove == "DOWN"):
                gameBoard[column-1][row+1] = 0
                gameBoard[column][row] = 1


          

        elif pygame.key.get_pressed()[pygame.K_r] == True:
          newGame = True
          print("Reset")
            
    renderImage()
    newGame = False

pygame.quit()

