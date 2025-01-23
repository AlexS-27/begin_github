import pygame
pygame.init()

#setup pygame
screen = pygame.display.set_mode((800,600))
player = pygame.Rect((300,250,50,50))
#clock = pygame.time.Clock()
run =True

#Loading the image
bg_image = pygame.image.load('bg_im.jpeg')
bg_image2 = pygame.image.load('ballonf.png')

#scaling the image to fit the game window
#bg_image = pygame.transform.scale(bg_image, (800,600)) --> image fixe

#Image initial position
x1=0
#x2= bg_image.get_width() --> 2 images qui défile
x2=0

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0,0,0.))
    pygame.draw.rect(screen,(255,0,0),player)

    #moving the bg
    x1 -= 1
    x2 -= 1

    #resetting the image when it leaves screen
    #if x1 == -1 *bg_image.get_width():
        #x1 = bg_image.get_width() --> image qui bouge si on quitte la position 0 de l'écran
    #if x2 == -1 *bg_image2.get_width():
        #x2 = bg_image2.get_width() --> 2ème image qui défile avec la première
    if x1 == -1 *bg_image.get_width(): #Même effet que précèdement avec les 2 images suaf que c'était un effet de profondeur qui était recherché ptr essayer avec des image plus "proche"
        x1 = 0
    if x2 == -1 *bg_image2.get_width():
        x2 = 0

    # Drawing image at position (0,0) --> essaie d'importation d'une image à la place du carré
    #screen.blit(bg_image,(0,0))
    #pygame.display.update()

    #Drawing images at positions (x1, 0) and (x2,0)
    screen.blit(bg_image,(x1,0))
    screen.blit(bg_image2,(x2,0))
    pygame.display.update()

    #background = pygame.Surface(screen.get_size()) --> essaie d'implantation d'une image pour bg
    #background = background.convert()
    #background.fill((0,0,255))

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1,0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    pygame.display.update()

pygame.quit()