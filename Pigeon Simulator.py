# MEIN PIGEON SIMULATOR IST EIN FUNKTIONSTÜCHTIGES SPIEL ES BENÖTIGT JEDOCH DIE ASSETS/DATEIEN AUS DEN "AUDIO" UND "GRAPHICS" ORDNERN WIE IN LINE 18 LESBAR IST. EINFACH MIT RUNTERLADEN UND ZUSAMMEN NUTZEN ZUM SPIELEN. 
import random

import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pigeon = pygame.image.load("graphics\\pigeon.png").convert_alpha()
        pigeon = pygame.transform.scale(pigeon, (70, 70))
        pigeon = pygame.transform.flip(pigeon, True, False)
        self.image = pigeon
        self.rect = self.image.get_rect(midbottom=(50, 290))
        self.gravity = 0

        #self.background_music = pygame.mixer.Sound("graphics\\audio\\Pigeon Simulator.mp3")
        #self.jump_sound = pygame.mixer.Sound("PyGame assets\\audio\\Jump.mp3")
        #self.jump_sound.set_volume(0.1)
        #if game_active = False: self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 290:
            self.gravity = -18
            #self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 340:
            self.rect.bottom = 340

    def update(self):
        self.player_input()
        self.apply_gravity()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, mob):
        super().__init__()

        if mob == 'fm':
            bat_size = (70, 70)
            bat = pygame.image.load("graphics\\bat.png").convert_alpha()
            bat = pygame.transform.scale(bat, bat_size)
            self.frames = bat
            y_pos = 190

        elif mob == 'ghost':
            ghost_size = (70, 70)
            ghost = pygame.image.load("graphics\\ghost.png").convert_alpha()
            ghost = pygame.transform.scale(ghost, ghost_size)
            ghost = pygame.transform.flip(ghost, True, False)
            self.frames = ghost
            y_pos = 290

        self.image = self.frames
        self.rect = self.image.get_rect(center=(random.randint(900, 1100), y_pos))
        # geist = self.rect2

    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score():
    time = int(pygame.time.get_ticks() / 100) - start_time
    time_surface = test_font.render(f'Score: {time}', False, ("Black"))
    time_rect = time_surface.get_rect(midleft =(15, 70))
    screen.blit(time_surface, time_rect)
    return time

def enemy_walk(enemy_rect_list):
    if enemy_rect_list:
        for enemy_rect in enemy_rect_list:
            enemy_rect.x -= 6

            if enemy_rect.centery == 190: screen.blit(enemy_b, enemy_rect)
            else: screen.blit(enemy_ghost,enemy_rect)

        enemy_rect_list = [enemy for enemy in enemy_rect_list if enemy.x >= -100]

        return enemy_rect_list
    else: return []

def collisions(Player,enemys):
    if enemys:
        for enemy_rect in enemys:
            if main_char_rect.colliderect(enemy_rect): return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: return True


# pygame zum benutzen der funktionen
# exit ist notwendig um das spiel korrekt zu schließen

pygame.init()                                           # Main Func
screen = pygame.display.set_mode((800,400))             # Screen
pygame.display.set_caption("Pigeon Simulator")              # Titel
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 80)
small_font = pygame.font.Font(None, 40)

screen_size = (800, 400)

#GAME ACTIVE
game_active = False
start_time = 0
score = 0

bg_music = (pygame.mixer.Sound("audio\\Music.mp3"))
bg_music.set_volume(0.2)
b_music = bg_music.play(loops = -1)

if game_active: b_music

# self.background_music = pygame.mixer.Sound("graphics\\audio\\Pigeon Simulator.mp3")

player = pygame.sprite.GroupSingle()
player.add(Player())

# TEXT
titel_surface = test_font.render("Pigeon Simulator:", "Comic Sans", (64, 64, 64))     # (text, AA, Color)
titel_rect = titel_surface.get_rect(midleft=(15, 30))

# SCORE
score_surface = test_font.render("Score:", "Comic Sans", (64, 64, 64))
score_rect = score_surface.get_rect(midleft=(15, 70))

# Start_screen
game_over_surface = big_font.render("Pigeon Simulator", "Comic Sans", "Black")
game_over_rect = game_over_surface.get_rect(center=(400, 50))
restart_surface = small_font.render("Drücke W und Leertaste zum spielen", "comic Sans", "Black")
restart_rect = restart_surface.get_rect(center=(400, 100))
# MAP

map_surface = pygame.image.load("graphics\\map.png").convert_alpha()
map_surface = pygame.transform.scale(map_surface,screen_size)

# GROUPS

obstacle_group = pygame.sprite.Group()


# ENEMY GHOST
enemy_size = (70, 70)
enemy_ghost = pygame.image.load("graphics\\ghost.png").convert_alpha()
enemy_ghost = pygame.transform.scale(enemy_ghost, enemy_size)
enemy_ghost = pygame.transform.flip(enemy_ghost, True, False)
# enemy_ghost_rect = enemy_ghost.get_rect(center = (730,290))

# ENEMY BAT
enemy_b_size = (70, 70)
enemy_b = pygame.image.load("graphics\\bat.png").convert_alpha()
enemy_b = pygame.transform.scale(enemy_b, enemy_b_size)
# enemy_b_rect = enemy_b.get_rect(center = (750,190))

# ENEMY
enemy_rect_list =[]


# PLAYER
main_char_size = (70, 70)
main_char_xy = (50, 350)
main_char = pygame.image.load("graphics\\pigeon.png").convert_alpha()
main_char = pygame.transform.scale(main_char, main_char_size)
main_char = pygame.transform.flip(main_char, True, False)
main_char_rect = main_char.get_rect(center=(main_char_xy))

# Big Boi
main_big_boi = pygame.image.load("graphics\\pigeon_gameover.png").convert_alpha()
main_big_boi = pygame.transform.scale(main_big_boi, (350, 350))
main_big_boi_rect = main_big_boi.get_rect(center=(130, 200))

# Gravity
#player_gravity = -0

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# wird benutzt um es durchgehend offen zu haben
# Die while True loop updated das game konstant
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# Sprung
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if main_char_rect.bottom >= 340:
                    player_gravity = -20

            if event.key == pygame.K_w:  # Prüfe den Tastendruck auf "W" außerhalb der vorherigen Bedingung
                if not game_active:  # Wenn das Spiel nicht aktiv ist, starte es neu
                    game_active = True
                    #enemy_ghost.left = 800
                    #enemy_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 100)
                    Player.rect = (50, 290)


            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if event.type == obstacle_timer and game_active:
            obstacle_group.add(Obstacle(choice(['fm', 'ghost', 'ghost'])))


            #if randint(0, 2):
            #    enemy_rect_list.append(enemy_ghost.get_rect(center=(randint(900, 1100), 290)))
            #else:
            #    enemy_rect_list.append(enemy_b.get_rect(center=(randint(900, 1100), 190)))



# Obstacle Ti
        #if event.type == obstacle_timer:



#   Screen.blit() wird verwendet um eingefügte Bilder in das Programm zu importieren nach dem einfügen von
#   blit.("Name_des_Bildes",(x_koordinate,y_koordinate))

#Game Hintergrund
    if game_active:
        screen.blit(map_surface,(0,0))
        screen.blit(titel_surface,titel_rect)
        score = display_score()

        # ENEMY
        # screen.blit(enemy_flipped,enemy_rect)
        # enemy_rect.x -= 5
        # if enemy_rect.right <= 0: enemy_rect.left = 800

        # ENEMY_BAT

        # screen.blit(enemy_b,enemy__b_rect)
        # enemy__b_rect.x -= 0
        # if enemy__b_rect.right <= 0: enemy__b_rect.left = 800

        # PLAYER
        #player_gravity += 1
        #main_char_rect.y += player_gravity
        #if main_char_rect.bottom >= 340 : main_char_rect.bottom = 340
        #screen.blit(main_char, main_char_rect)
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()


        # ENEMY LIST SPAWNS
        #enemy_rect_list = enemy_walk(enemy_rect_list)

    # COLLISION
        #game_active = collisions(main_char_rect, enemy_rect_list)
        # if main_char_rect.colliderect(enemy_ghost_rect):
        #    game_active = False
        # if main_char_rect.colliderect(enemy_b_rect):
        #    game_active = False
        game_active = collision_sprite()

    # GAME OVER SCREEN
    else:
        screen.fill('#66ccff')
        screen.blit(main_big_boi, main_big_boi_rect)
        screen.blit(game_over_surface, game_over_rect)
        screen.blit(restart_surface, restart_rect)
        score_message = test_font.render(f'Deine Punktzahl: {score}', False, "Black")
        score_message_rect = score_message.get_rect(center=(400, 330))
        main_char_rect.center = (main_char_xy)
        player_gravity = 0
        enemy_rect_list.clear()
        # score
        if score == 0: screen.blit(restart_surface, restart_rect)
        else: screen.blit(score_message, score_message_rect)
        Player.rect = (50, 290)

        # screen.blit wurde auf main_char gesetzt und mit .char.rect
        # kann man zeitgleich die x,y kordinaten mit geben
    pygame.display.update()
    clock.tick(60)

    # Mit .key.get_pressed kann man den input von verschiedenen tasten nachgucken (Liste im internet)
    # Die tasten müssen in einer seperaten Line geschrieben werden und als tuple formuliert werden

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]: print("Pressed")

    # if main_char_rect.colliderect(enemy_rect):
    #   print("collision")

        # mouse_pos = pygame.mouse.get_pos()
        # if main_char_rect.collidepoint(mouse_pos): print("Collide")

# NO ANIMATION
