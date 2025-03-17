import pygame
import math
import csv

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 12
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hitbox_w = self.width + 5
        self.hitbox_h = self.height + 5
        self.update_hitbox()

    def update_hitbox(self):
        self.hitbox_player = pygame.Rect(
            self.x +(player_w-self.hitbox_w)//2,
            self.y +(player_h - self.hitbox_h)//2,
            self.hitbox_w,
            self.hitbox_h
        )

    def draw(self, surface):

        pygame.draw.rect(surface, 'red', self.rect)
        #pygame.draw.rect(surface, 'black', self.hitbox_player,2)

    def move(self, dx, dy):
        #garde l'ancienne position avant le déplacement
        old_x = self.x
        old_y = self.y

        #déplacement
        self.x += dx
        self.y += dy

        #Màj du joeur
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.update_hitbox()

        #vérif des limites
        if self.rect.left < limite_x[0] or self.rect.right > limite_x[1]:
            self.x = old_x
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.rect.top < limite_y[0] or self.rect.bottom > limite_y[1]:
            self.y = old_y
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class Enemy():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.velocity = velocity

        self.hitbox_w = width + 5
        self.hitbox_h = height + 5
        self.update_hitbox()

    def update_hitbox(self):
        #met à jour la hitbox
        self.hitbox_enemy = pygame.Rect (
        self.rect.x + (self.width - self.hitbox_w) // 2,
        self.rect.y + (self.height - self.hitbox_h) // 2,
        self.hitbox_w,
        self.hitbox_h
    )

    def draw(self, window):

        pygame.draw.rect(window, 'green', self.rect)
        pygame.draw.rect(window, 'black', self.hitbox_enemy, 2)

    def move (self, dx, dy):
        #on garde l'ancienne position
        old_ex, old_ey = self.x, self.y

        self.rect.x += dx * velocity
        self.rect.y += dy * velocity

        #MàJ de l'ennemie
        #self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.rect.left < limite_x[0] or self.rect.right > limite_x[1]:
            self.rect.x = old_ex
            #self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.rect.top < limite_y[0] or self.rect.bottom > limite_y[1]:
            self.rect.y = old_ey
            #self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.update_hitbox()

    def move_towards_player(self, player, ):
        #calculer la direction vers le joueur
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y

        #calculer la distance entre l'ennemi et le joueur
        dist = math.hypot(dx, dy)

        # Enemy AI: Move towards the player
        if dist != 0:
            dx /= dist
            dy /= dist

            #déplacer l'ennemi
            self.rect.x += dx * (self.velocity -2)
            self.rect.y += dy * (self.velocity -2)

            self.update_hitbox()

class HealthBar():

    def __init__(self, x, y, width, height, max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(window, 'red', (700, 0, 300, 40))
        pygame.draw.rect(window, 'green', (700, 0, int(300 * ratio), 40))

class Collide_damage():
    def __init__(self, x, y, max_damage):
        self.x = x
        self.y = y
        self.damage = max_damage
        self.max_damage = max_damage

    def colide(self, player1, enemy):
        collide = pygame.Rect.colliderect(enemy.rect, player1.rect)

        #if collide:



pygame.init()

window_width = 1000
window_height = int(window_width*0.8)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Essaie de la Pygame")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define game variable
Gravity = 0.75
Rows = 16
Cols = 150
tile_size = window_height // Rows
tile_types = 21
level = 1


limite_x = (60, 940)
limite_y = (60, 940)

#store the initial coordinates of the player in two variables i.e x and y
x, y = 100, 100
velocity = 12
player_w, player_h = 50, 50

ex, ey = 720, 720
enemy_w, enemy_h = 50, 50
enemy_speed = 2

player1 = Player(x, y, player_w, player_h)
enemy = Enemy(x, y, enemy_w, enemy_h)

health_bar = HealthBar(250,200,300,40,100)
run = True
clock = pygame.time.Clock()

#create empty tile list
world_data = []
for row in range(Rows):
    r = [-1] * Cols
    world_data.append(r)

#load in level data and create world
with open(f'level{level}_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in enumerate(reader):
        for tile in enumerate(row):
            world_data[x][y] = int(tile)

print(world_data)


while run:
    pygame.time.delay(30)
    window.fill((255,255,255))

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player1.move(-player1.velocity, 0)
    if key[pygame.K_RIGHT]:
        player1.move(player1.velocity, 0)
    if key[pygame.K_UP]:
        player1.move(0, -player1.velocity)
    if key[pygame.K_DOWN]:
        player1.move(0, player1.velocity)

    if player1.hitbox_player.colliderect(enemy.hitbox_enemy):
        print("collision")

    #draw health bar
    health_bar.hp = 50
    health_bar.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    # Enemy AI: Move towards the player
    enemy.move_towards_player(player1)

    #pygame.draw.rect(window, (255,0,0), player)
    player1.draw(window)
    enemy.draw(window)

    pygame.display.flip()

    pygame.display.update()

pygame.quit()