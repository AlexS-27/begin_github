import pygame

pygame.init()

window = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Essaie de la Pygame")

limite_x = (60, 940)
limite_y = (60, 940)

#store the initial coordinates of the player in two variables i.e x and y
x, y = 100, 100
velocity = 12

player = pygame.Rect((x ,y ,50,50))

run = True
while run:
    pygame.time.delay(30)
    window.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    old_x, old_y = player.x, player.y

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.x -= velocity
    if key[pygame.K_RIGHT]:
        player.x += velocity
    if key[pygame.K_UP]:
        player.y -= velocity
    if key[pygame.K_DOWN]:
        player.y += velocity

    if player.left < limite_x[0] or player.right > limite_x[1]:
        player.x = old_x
    if player.top < limite_y[0] or player.bottom > limite_y[1]:
        player.y = old_y

    pygame.draw.rect(window, (255,0,0), player)

    pygame.display.update()

pygame.quit()