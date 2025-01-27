"""
etape 1 : creating a platform

etape 2 : moving platform

etape 3 : adding player sprite and collision (+gravity)
"""
#Importing the pygame module
import pygame

#initiate pygame and give permission to use pygame's functionality
pygame.init()

#create a display surface object of specific dimension
window = pygame.display.set_mode((600, 600))

#creating a new clock object to track the amount of time
clock = pygame.time.Clock()

platform_vel = 5

#startig coordinate of the platform
x = 100
y = 150

#starting coordinates for player sprite
player_x = 180
player_y = 0

#creating a new variable for gravity
gravity = 8

#creating a new rect for player
player_rect = pygame.Rect(player_x, player_y, 50, 50)

#creating a rect with width and height
"""
rect = [pygame.Rect(x, y, 200, 50), pygame.Rect(x, 300, 200, 50)]

essaie de multiplateforme
"""
rect = pygame.Rect(x, y, 200, 50)

#creating a boolean variable that we will use to run the while loop
run = True

#cretaing an infinite loop to run our game
while run:

    #setting the framerate to 30fps
    clock.tick(30)

    #multipying platform_vel with -1. if its x coordinate is less than 100 or greater than or equal to 300
    #etape 2
    if rect.left >= 300 or rect.left < 100 :
        platform_vel *= -1

    #Checking if player is colliding with platform or not using the colliderect() method.
    #It will return a boolean value
    collide = pygame.Rect.colliderect(rect, player_rect)

    #If player is colliding with platform then setting coordinate of player bottom equal to
    #top platform and adding the platform velocity
    if collide:
        player_rect.bottom = rect.top
        player_rect.left += platform_vel

    #adding platform_vel to x coordinate of our rect (etape 2)
    rect.left += platform_vel

    #adding gravity
    player_rect.top += gravity

    #drawing the rect on the screen using the draw.rect() method
    pygame.draw.rect(window, (255, 0, 0), rect)

    pygame.draw.rect(window, (0, 255, 0), player_rect)

    #updating the display surface
    pygame.display.update()

    #filling the window with white color
    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()