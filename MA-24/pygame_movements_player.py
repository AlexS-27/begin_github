#importing pygame module
import pygame

#initiate pygame and give permission to use pygame's functionality
pygame.init()

#create the display surface object of specific dimension
window = pygame.display.set_mode((1000, 1000))

#add caption in the window
pygame.display.set_caption("Movement Player")

#Initializing the clock. Clocks are used to track and control the frame-rate of a game
clock = pygame.time.Clock() #étape 2

#Creating a variable to check the direction of movement. We will change its value
#whenever the player changes its direction
direction = True

#add player sprite
image = [pygame.image.load('perso.gif'),
         pygame.image.load('perso2.webp')]

#store the initial coordinates of the player in two variables i.e x and y
x=100
y=100

#create variable to store the velocity of player's movement
velocity = 12

#creating the Infinite loop
run = True
while run:

    # filling the bg with white color
    window.fill((255,255,255))

    #display the player sprite at x and y coordinates
    # window.blit(image, (x, y)) --> jusqu'a étape 3 car qu'une image

    """
        #iterate over the list of Event objects that was returned by pygame.event.get() method
        for event in pygame.event.get():

            #closing the window and program if the type of the text is QUIT
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
    """

    """
    Etape 1 : Mouvement des joueurs avec les flêches et velocity
    """
    """
     #checking event key if the type of the event is KEYDOWN i.e. keyboard button is pressed
    if event.type == pygame.KEYDOWN:

        #Incresing the x coordinate if the button pressed is left arrow key
        if event.key == pygame.K_LEFT:
            x -= velocity

        #Increasing the x coordinate if the button pressed is right arrow key
        if event.key == pygame.K_RIGHT:
            x += velocity

        #Increasing the y coordinate if the button pressed is up arrow key
        if event.key == pygame.K_UP:
            y -= velocity

        #Increasing the y coordinate if the button pressed is down arrow key
        if event.key == pygame.K_DOWN:
            y += velocity

    #Draws the surface object to the screen
    pygame.display.update()
    """

    """
    Etape 2 : Moving players in continuous movement 
    """
    """
    #Set the frame rates to 60 fps
    clock.tick(60)

    #Storing the key pressed in a new variable using key.get_pressed() method
    key_pressed_is = pygame.key.get_pressed()

    #changing the coordinates of the player
    if key_pressed_is[pygame.K_LEFT]:
        x -= 8
    if key_pressed_is[pygame.K_RIGHT]:
        x += 8
    if key_pressed_is[pygame.K_UP]:
        y -= 8
    if key_pressed_is[pygame.K_DOWN]:
        y += 8

    #draws the surface object to the screen
    pygame.display.update()
    """

    """
    Etape 3 : Flip players vertically
    """
    """
    clock.tick(60)

    if direction == True:
        window.blit(image, (x, y))
    if  direction == False:
        window.blit(pygame.transform.flip(image, True, False), (x, y))

    # iterate over the list of Event objects that was returned by pygame.event.get() method
    for event in pygame.event.get():

        # closing the window and program if the type of the text is QUIT
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        # Changing the value of the
        # direction variable
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = True
            elif event.key == pygame.K_LEFT:
                direction = False

    #Storing the key pressed in a new variable using key.get_pressed() method
    key_pressed_is = pygame.key.get_pressed()

    #Changing the coordinates of the player
    if key_pressed_is[pygame.K_UP]:
        y -= 5
    if key_pressed_is[pygame.K_DOWN]:
        y += 5
    if key_pressed_is[pygame.K_LEFT]:
        x -= 5
    if key_pressed_is[pygame.K_RIGHT]:
        x += 5

    #Draws the surface object to the screen
    pygame.display.update()
    """

    """
    Etape 4 : Flip players with an other image 
    """

    clock.tick(60)

    if direction == True:
        window.blit(image[0], (x, y))
    if  direction == False:
        window.blit(image[1], (x, y))

    # iterate over the list of Event objects that was returned by pygame.event.get() method
    for event in pygame.event.get():

        # closing the window and program if the type of the text is QUIT
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        # Changing the value of the
        # direction variable
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = True
            elif event.key == pygame.K_LEFT:
                direction = False

    # Storing the key pressed in a new variable using key.get_pressed() method
    key_pressed_is = pygame.key.get_pressed()

    #Changing the coordinates of the player
    if key_pressed_is[pygame.K_UP]:
        y -= 5
    if key_pressed_is[pygame.K_DOWN]:
        y += 5
    if key_pressed_is[pygame.K_LEFT]:
        x -= 5
    if key_pressed_is[pygame.K_RIGHT]:
        x += 5

    #Draws the surface object to the screen
    pygame.display.update()