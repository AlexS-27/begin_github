import pygame

pygame.init()

screen = pygame.display_set_mode((800,600))

player = pygame.Rect((300,250,50,50))

run =True
while run:

    screen.fill((0,0,0.))

    pygame.draw.rect(screen,(255,0,0),player)

    key = pygame.key.get_pressed()
    match True:
        case key[pygame.K_a]:
            player.move_ip(-1,0)
        case key[pygame.K_d]:
            player.move_ip(1, 0)
        case key[pygame.K_w]:
            player.move_ip(0, -1)
        case key[pygame.K_s]:
            player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame quit()
