import pygame

pygame.init()

width = 800
height = 800

window = pygame.display.set_mode([width,height])
timer = pygame.time.Clock()
fps = 30

#gameloop

running = True
while running:
     timer.tick(fps)
     window.fill('white')

     for event in pygame.event.get():           #checking if program was quit
         if event.type == pygame.QUIT:
             running = False

     pygame.display.flip()

pygame.quit()





