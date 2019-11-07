import pygame
from typing import List


class Visualizer:


    #===Static Variables===
    WINDOW = (500,500)
    BLACK = (0,0,0)
    GREY = (100,100,100)
    WHITE = (255,255,255)
    RED = (210, 35, 45)
    YELLOW = (255, 225, 50)
    DIMENSION = 10# Dimension of game board
    SIZE = 50 # Dimension of a grid tile

    P1 = "X"
    P2 = "O"
    KP1 = "KX"
    KP2 = "KO"
    EMPTY = " "

    #===Instance Variables===
    screen: pygame.Surface

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW, pygame.HWSURFACE |
                                              pygame.DOUBLEBUF)
        
    def getInput(self):
        keypressed = pygame.event.get()
        return keypressed

    def quit(self):
        pygame.quit()

    """
    Create a checker board onto the screen from a 2D list of characters, with
    piece strings defined in the static variables above.
    By Ronald
    """
    def create_board(self, board_list) -> None:
        background = pygame.Surface(self.WINDOW)
        for row in range(len(board_list)):
            for column in range(len(board_list[row])):
                rect = pygame.Rect(column*self.SIZE, row*self.SIZE, self.SIZE,
                                   self.SIZE)
                
                """alternate drawing white and grey tiles every column,
                switch order every row"""
                if(((column%2)+(row%2))%2 == 0):
                    pygame.draw.rect(background, self.WHITE, rect)
                else:
                    pygame.draw.rect(background, self.GREY, rect)
                    
                """Draw man/king if there is one on this tile"""
                if(board_list[row][column] == self.P1):
                    pygame.draw.ellipse(background, self.BLACK, rect)
                elif(board_list[row][column] == self.P2):
                    pygame.draw.ellipse(background, self.RED, rect)
                elif(board_list[row][column] == self.KP1):
                    pygame.draw.ellipse(background, self.BLACK, rect)
                    pygame.draw.ellipse(background, self.YELLOW,
                                        rect.inflate(-self.SIZE//2, -self.SIZE//2))
                elif(board_list[row][column] == self.KP2):
                    pygame.draw.ellipse(background, self.RED, rect)
                    pygame.draw.ellipse(background, self.YELLOW,
                                        rect.inflate(-self.SIZE//2, -self.SIZE//2))
                    
        self.screen.blit(background, (0,0))
        pygame.display.update()

    """
    Create a DIMENSION*DIMENSION grid onto the screen with alternating
    white and grey tiles, with tiles of dimension SIZE*SIZE.(without any men)
    By Ronald
    """
    def create_initial_grid(self) -> None:
        background = pygame.Surface(self.WINDOW)
        for row in range(self.DIMENSION):
            for column in range(self.DIMENSION):
                rect = pygame.Rect(column*self.SIZE, row*self.SIZE, self.SIZE,
                                   self.SIZE)

                """alternate white and grey tiles every column,
                switch order every row"""
                if(((column%2)+(row%2))%2 == 0):
                    pygame.draw.rect(background, self.WHITE, rect)
                else:
                    pygame.draw.rect(background, self.GREY, rect)
                    
        self.screen.blit(background, (0,0))
        pygame.display.update()
        

if __name__ == "__main__":
    
    visualizer = Visualizer()
    board = [[" ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
             ["X", " ", "X", " ", "X", " ", "X", " ", "X", " "],
             [" ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
             ["KX", " ", "X", " ", "X", " ", "X", " ", "X", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", "O", " ", "O", " ", "O", " ", "O", " ", "O"],
             ["O", " ", "O", " ", "O", " ", "O", " ", "O", " "],
             [" ", "O", " ", "O", " ", "O", " ", "O", " ", "O"],
             ["KO", " ", "O", " ", "O", " ", "O", " ", "O", " "]]
    visualizer.create_board(board)
    
    is_running = True
    while(is_running):
        events = visualizer.getInput()
        if events:
            for event in events:
                if event.type == 6:
                    if event.dict['button'] == 1:
                        print('left' + str(event.dict['pos']))
                    elif event.dict['button'] == 3:
                        print('right' + str(event.dict['pos']))

        for event in events:
            if event.type == pygame.QUIT:
                visualizer.quit()
                is_running = False
