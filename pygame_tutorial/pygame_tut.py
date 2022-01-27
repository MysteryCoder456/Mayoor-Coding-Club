import pygame

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()

    win.fill(pygame.Color("black"))

    # First number: x position or horizontal position
    # Second number: y position or vertical position
    # Third number: width
    # Fourth number: height
    pygame.draw.rect(win, pygame.Color("red"), (10, 10, 50, 100))
    pygame.draw.rect(win, pygame.Color("green"), (200, 300, 200, 50))

    pygame.display.flip()
