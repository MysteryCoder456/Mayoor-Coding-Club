import pygame

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")

x = 250  # horizontal pos
y = 450  # vertical pos
speed = 3  # speed of movement

enemy_x = 50
enemy_y = 50
enemy_speed = 4


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    elif keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed

    enemy_x += enemy_speed

    # Bounce the enemy from left and right
    if enemy_x > 500 - 40 or enemy_x < 0:
        enemy_speed *= -1
        enemy_y += 60

    # Prevent player from going off screen
    if x < 0:
        x = 0
    elif x >= 500 - 50:
        x = 500 - 50

    if y < 0:
        y = 0
    elif y >= 500 - 50:
        y = 500 - 50

    win.fill(pygame.Color("black"))

    # First number: x position or horizontal position
    # Second number: y position or vertical position
    # Third number: width
    # Fourth number: height
    pygame.draw.rect(win, pygame.Color("red"), (x, y, 50, 50))
    pygame.draw.rect(win, pygame.Color("blue"), (enemy_x, enemy_y, 40, 40))

    pygame.display.flip()
