# pygame template
# hi!!!!!!! :))))))

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

sky_r = 149
sky_g = 232
sky_b = 240
cloud_x1 = 110
cloud_x2 = 270
cloud_x3 = 400
cloud_x4 = 560
cloud_x5 = 85
cloud_x6 = 255
cloud_x7 = 480
cloud_x8 = 330
sun_y = 90
moon_y = 800
sun_dir = True
moon_dir = True

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
   
    if sky_r >= 7:
        sky_r -= 1
    if sky_g >= 22:
        sky_g -= 1
    if sky_b >= 46:
        sky_b -= 1

    cloud_x1 += 3
    cloud_x2 += 3.48
    cloud_x3 += 3.6
    cloud_x4 += 2.6
    cloud_x5 += 3.2
    cloud_x6 += 2.45
    cloud_x7 += 3.6
    cloud_x8 += 2.728
    
    if cloud_x1 > WIDTH + 25:
        cloud_x1 = -100

    if cloud_x2 > WIDTH + 30:
        cloud_x2 = -100

    if cloud_x3 > WIDTH + 30:
        cloud_x3 = -100

    if cloud_x4 > WIDTH + 30:
        cloud_x4 = -100

    if cloud_x5 > WIDTH + 30:
        cloud_x5 = -100
        
    if cloud_x6 > WIDTH + 25:
        cloud_x6 = -100
        
    if cloud_x7 > WIDTH + 30:
        cloud_x7 = -100
    
    if cloud_x8 > WIDTH + 25:
        cloud_x8 = -100

    if sun_dir:
        sun_y += 2.5

    if sun_y >= 850:
        sun_y = 850
        sun_dir = False

    if sun_dir == False:
        sun_y -= 2.5
        if sun_y >= 850:
            sun_y = 850
            sun_dir = True

    if sun_y <= 90:
        sun_y = 90
        sun_dir = True

    if moon_dir:
        moon_y -= 2.5

    if moon_y >= 850:
        moon_y = 850
        moon_dir = True
        
    if moon_y <= 90:
        moon_y = 90
        moon_dir = False
        
    if moon_dir == False:
        moon_y += 2.5
        if moon_y >= 850:
            moon_y = 850
            moon_up = True

    if moon_y <= 300:
        sky_r = max(7, sky_r - 1)
        sky_g = max(22, sky_g - 1)
        sky_b = max(46, sky_b - 1)
    
    if sun_y < 300:
        sky_r = min(149, sky_r + 5)
        sky_g = min(232, sky_g + 5)
        sky_b = min(240, sky_b + 5)

    if moon_y <= 300:
        white = (199, 195, 195)
    
    if sun_y < 300:
        white = (255, 255, 255)

    if moon_y <= 300:
        green = (33, 138, 37)

    if sun_y < 300:
        green = (37, 219, 24)

    if moon_y <= 300:
        red = (166, 5, 5)
    
    if sun_y < 300:
        red = (255, 0, 0)

    if moon_y <= 300:
        beige = (168, 161, 91)
    
    if sun_y < 300:
        beige = (227, 218, 134) 

    if moon_y <= 300:
        star_x1 = 30
    
    if sun_y < 300:
        star_x1 = 700

    if moon_y <= 300:
        star_x2 = 10

    if sun_y < 300:
        star_x2 = 700

    if moon_y <= 300:
        star_x3 = 205

    if sun_y < 300:
        star_x3 = 700

    if moon_y <= 300:
        star_x4 = 355

    if sun_y < 300:
        star_x4 = 700

    if moon_y <= 300:
        star_x5 = 265

    if sun_y < 300:
        star_x5 = 700
    
    if moon_y <= 300:
        star_x6 = 410

    if sun_y < 300:
        star_x6 = 700

    if moon_y <= 300:
        star_x7 = 455

    if sun_y < 300:
        star_x7 = 700

    if moon_y <= 300:
        star_x8 = 535

    if sun_y < 300:
        star_x8 = 700

    if moon_y <= 300:
        star_x9 = 510

    if sun_y < 300:
        star_x9 = 700

    if moon_y <= 300:
        star_x10 = 620
    
    if sun_y < 300:
        star_x10 = 700

    if moon_y <= 300:
        star_x11 = 125
    
    if sun_y < 300:
        star_x11 = 700
    
    # DRAWING
    screen.fill((sky_r, sky_g, sky_b))  # always the first drawing command

    # Moon
    pygame.draw.circle(screen, (255, 255, 255), (120, moon_y), 60)

    # Sun
    pygame.draw.circle(screen, (247, 232, 10), (120, sun_y), 60)

    # Stars
    pygame.draw.circle(screen, (255, 255, 255), (star_x1, 50), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x2, 230), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x3, 70), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x4, 120), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x5, 215), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x6, 30), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x7, 230), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x8, 140), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x9, 45), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x10, 100), 2)
    pygame.draw.circle(screen, (255, 255, 255), (star_x11, 150), 2)

    # Clouds
    pygame.draw.circle(screen, white, (cloud_x1, 110), 25)
    pygame.draw.circle(screen, white, (cloud_x1 + 30, 120), 25)
    pygame.draw.circle(screen, white, (cloud_x1 + 20, 140), 25)

    pygame.draw.circle(screen, white, (cloud_x2, 50), 30)
    pygame.draw.circle(screen, white, (cloud_x2 + 50, 45), 30)
    pygame.draw.circle(screen, white, (cloud_x2 + 30, 35), 30)

    pygame.draw.circle(screen, white, (cloud_x3 + 55, 125), 25)
    pygame.draw.circle(screen, white, (cloud_x3 + 50, 145), 25)
    pygame.draw.circle(screen, white, (cloud_x3 + 45, 130), 25)

    pygame.draw.circle(screen, white, (cloud_x4 + 70, 50), 30)
    pygame.draw.circle(screen, white, (cloud_x4 + 60, 65), 30)
    pygame.draw.circle(screen, white, (cloud_x4 + 40, 55), 30)

    pygame.draw.circle(screen, white, (cloud_x5, 240), 30)
    pygame.draw.circle(screen, white, (cloud_x5 + 60, 235), 30)
    pygame.draw.circle(screen, white, (cloud_x5 + 50, 230), 30)

    pygame.draw.circle(screen, white, (cloud_x6, 215), 25)
    pygame.draw.circle(screen, white, (cloud_x6 + 30, 210), 25)
    pygame.draw.circle(screen, white, (cloud_x6 + 20, 220), 25)

    pygame.draw.circle(screen, white, (cloud_x7, 210), 30)
    pygame.draw.circle(screen, white, (cloud_x7 + 50, 200), 30)
    pygame.draw.circle(screen, white, (cloud_x7 + 40, 215), 30)

    pygame.draw.circle(screen, white, (cloud_x8, 45), 25)
    pygame.draw.circle(screen, white, (cloud_x8 + 40, 40), 25)
    pygame.draw.circle(screen, white, (cloud_x8 + 35, 50), 25)
    
    # Golf course
    pygame.draw.rect(screen, green, (0, 385, 640, 100)) # grass
    pygame.draw.ellipse(screen, (33, 138, 37), (145, 385, 350, 20)) # green
    pygame.draw.ellipse(screen, white, (300, 385, 40, 10)) # hole
    pygame.draw.rect(screen, red, (320, 220, 80, 50)) # flag
    pygame.draw.rect(screen, white, (317.5, 220, 5, 170)) # flagstick
    pygame.draw.ellipse(screen, beige, (440, 425, 300, 100)) # bunker
    pygame.draw.rect(screen, (59, 30, 30), (580, 285, 50, 100)) # tree trunk
    pygame.draw.circle(screen, green, (630, 250), 40) # tree leaves 1
    pygame.draw.circle(screen, green, (580, 280), 40) # tree leaves 2
    pygame.draw.circle(screen, green, (580, 235), 40) # tree leaves 3

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
