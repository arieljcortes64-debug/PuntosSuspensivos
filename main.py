import pygame
import sys
import config as st

pygame.init()
screen = pygame.display.set_mode((st.WINDOW_HEIGHT, st.WINDOW_WIDTH))
pygame.display.set_caption(st.TITLE)
player_surface = pygame.image.load(
    "Source/Sprites/Player/Asset 1player1_1.png"
).convert_alpha()
player_surface = pygame.transform.scale(player_surface, (100, 100))
player_rect = player_surface.get_rect(midbottom=(800, 800))

map_surface = pygame.image.load("Source/Sprites/Map/unnamed_test.jpg")
map_surface = pygame.transform.scale(map_surface, (1920, 1080))
map_rect = map_surface.get_rect(topleft=(0, 0))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    vel_x = 0
    vel_y = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        vel_x = -st.SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        vel_x = st.SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        vel_y = -st.SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        vel_y = +st.SPEED

    player_rect.x += vel_x
    player_rect.y += vel_y
    player_rect.left = max(player_rect.left, 125)
    player_rect.right = min(player_rect.right, 1790)
    player_rect.top = max(player_rect.top, 125)
    player_rect.bottom = min(player_rect.bottom, 980)

    screen.blit(map_surface, map_rect)
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(st.FPS)
