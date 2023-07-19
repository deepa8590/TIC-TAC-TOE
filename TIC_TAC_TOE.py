import pygame
import sys
import numpy as np

pygame.init()  # initialises pygame model

COUNT1=0

WIDTH = 600  # WIDTH and HEIGHT are constants ,so they are represented in capital letters
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE=WIDTH//BOARD_ROWS
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
CUT_CORNER_CROSS_SPACE = 55

# rgb:red blue  green
RED = (255, 0, 0)
BG_COLOR = (30, 150, 175)
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# creating a screen board
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('WELCOME TO TIC TAC TOE :)\nPress r to RESET')  # setting title
screen.fill(BG_COLOR)

#console  board
board = np.zeros((BOARD_ROWS, BOARD_COLS))  # takes tuple as argument
# print(board)     #got as list

# Drawing 2 horiaontal and 2 vertical lines


def draw_4_lines():
    # 1st horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # starting , ending cordinates as tuple
    # 2nd horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # 1st vertical line
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2nd vertical line
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def draw_circle_or_cross():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:  # means player 1 and by default he /she choose circle
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col*200+100), int(row*200+100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
               
                pygame.draw.line(screen, CROSS_COLOR, (col*200+CUT_CORNER_CROSS_SPACE, row * 200+200 -CUT_CORNER_CROSS_SPACE), (col * 200+200-CUT_CORNER_CROSS_SPACE, row*200+CUT_CORNER_CROSS_SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col*200+CUT_CORNER_CROSS_SPACE, row * 200+CUT_CORNER_CROSS_SPACE),(col * 200+200-CUT_CORNER_CROSS_SPACE, row*200+200-CUT_CORNER_CROSS_SPACE), CROSS_WIDTH)


def mark_the_square(row, col, player):
    board[row][col] = player

# returns true if square is available


def SPACE_check(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

# true if board is full


def full_board_check():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def win_check(player):
    # vertical win check
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True
            #

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal_line(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal_line(player)
		return True

	return False    #no win

def draw_vertical_winning_line(col,player):
    posX = col * 200 + 100  # Xpostion does not gonna change
    
    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row,player):
    posY = row * 200 + 100  # Xpostion does not gonna change
    
    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line( screen, color, (15,posY), (WIDTH-15,posY), LINE_WIDTH )
def draw_asc_diagonal_line(player):
    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line( screen, color, (15, HEIGHT-15), (WIDTH - 15, 15),15 )    
def draw_desc_diagonal_line(player):
    if player == 1:
        color = CIRCLE_COLOR

    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15 )    



def restart():
	screen.fill( BG_COLOR )
	draw_4_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0


draw_4_lines()

player = 1
game_over=False
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # quit the application

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # this checks if we are clicking the screen
            # linking screen board to console board,we need to acces x and y coordinates when we click the screen
            # event.pos[0] represent x coordinate
            # event.pos[1] represent y coordinate
            X_Cordinate = event.pos[0]
            Y_Cordinate = event.pos[1]

            # each small square is of 200 length
            clicked_row = int(Y_Cordinate // 200)
            clicked_col = int(X_Cordinate // 200)

            if SPACE_check(clicked_row, clicked_col):
                if player == 1 :
                    mark_the_square(clicked_row, clicked_col, 1)
                    #check win right after a player mark the square
                    if win_check(player):
                        print("CONGRATULATIONS player{} Wins the game".format(player))
                        print("Player1 Score: 1\nPlayer2 Score: 0")
                        game_over=True
                    elif (full_board_check()==True)  :
                        print("OOPS! IT's A TIE,NO One wins the game\n")
                        print("Player1 Score: 0\nPlayer2 Score: 0")
                    player = 2
                elif player == 2 and (full_board_check()==False):
                    mark_the_square(clicked_row, clicked_col, 2)
                    if win_check(player):
                        print("CONGRATULATIONS player{} Wins the game".format(player))
                        print("Player1 Score: 0\nPlayer2 Score: 1")
                        game_over=True
                    elif (full_board_check()==True)  :
                        print("OOPS! IT's A TIE ,NO One wins the game")  
                        print("Player1 Score: 0\nPlayer2 Score: 0")  
                    player = 1

                draw_circle_or_cross()
                #print(board)

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()  # inorder to update the screen
