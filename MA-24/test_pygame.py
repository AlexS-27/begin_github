import pygame

pygame.init()

screen = pygame.display_set_mode((800,600))

player = pygame.Rect((300,250,50,50))

run =True
while run:

    screen.fill((0,0,0.))

    pygame.draw.rect(screen,(255,0,0),player)

    key = pygame.key