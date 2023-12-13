import pygame

pygame.init()

width = 800
height = 800

window = pygame.display.set_mode([width, height])
timer = pygame.time.Clock()
fps = 30

#pieces and locations

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),         #coordinates for backline
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]         #coordinates für pawns
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

#loading pieces

black_queen = pygame.image.load('image_pieces/black queen.png')
black_queen = pygame.transform.scale(black_queen, (60, 60))
black_king = pygame.image.load('image_pieces/black king.png')
black_king = pygame.transform.scale(black_king, (60, 60))
black_rook = pygame.image.load('image_pieces/black rook.png')
black_rook = pygame.transform.scale(black_rook, (60, 60))
black_bishop = pygame.image.load('image_pieces/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (60,60))
black_knight = pygame.image.load('image_pieces/black knight.png')
black_knight = pygame.transform.scale(black_knight, (60, 60))
black_pawn = pygame.image.load('image_pieces/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (60, 60))
white_queen = pygame.image.load('image_pieces/white queen.png')
white_queen = pygame.transform.scale(white_queen, (60, 60))
white_king = pygame.image.load('image_pieces/white king.png')
white_king = pygame.transform.scale(white_king, (60, 60))
white_rook = pygame.image.load('image_pieces/white rook.png')
white_rook = pygame.transform.scale(white_rook, (60, 60))
white_bishop = pygame.image.load('image_pieces/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (60, 60))
white_knight = pygame.image.load('image_pieces/white knight.png')
white_knight = pygame.transform.scale(white_knight, (60, 60))
white_pawn = pygame.image.load('image_pieces/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (60, 60))

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']  #to make sure the index and the image are
                                                                    # in the same spot

def drawing_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(window, 'white', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(window, 'white', [(600 + 100) - (column * 200), row * 100, 100, 100])


#gameloop

running = True
while running:
     timer.tick(fps)
     window.fill("black")
     drawing_board()

     for event in pygame.event.get():           #checking if program was quit
         if event.type == pygame.QUIT:
             running = False

     pygame.display.flip()

pygame.quit()






