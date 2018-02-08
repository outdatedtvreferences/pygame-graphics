# computer programming 1
# unit 11 - graphics
#
# a scene with layered rain


# imports
import pygame
import random

# initialize game engine
pygame.mixer.pre_init()
pygame.init()

# window
SIZE = (800, 600)
TITLE = "rainy day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# timer
clock = pygame.time.Clock()
refresh_rate = 60

# colors
GREEN = (100, 125, 75)
WHITE = (255, 255, 255)
BLUE = (93, 149, 200)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
YELLOW = (230, 200, 100)
BACK_BLUE = (103, 151, 229)
NIGHT_SKY = (2, 17, 43)
FRONT_BLUE = (176, 196, 232)

# settings
stormy = True

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, DARK_GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARK_GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, DARK_GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, DARK_GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, DARK_GRAY, [x + 20, y + 20, 60, 40])

def draw_small_drop(sr):
    rect = sr[:4]
    pygame.draw.ellipse(screen, BACK_BLUE, rect)

def draw_big_drop(br):
    rect = br[:4]
    pygame.draw.ellipse(screen, FRONT_BLUE, rect)

def draw_huge_drop(hr):
    rect = hr[:4]
    pygame.draw.ellipse(screen, BLUE, rect) 

''' make clouds '''
num_clouds = 100
clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

''' make rain '''
num_small_drops = 500
srain = []

num_big_drops = 50
brain = []

num_huge_drops = 2
hrain = []

for i in range(num_small_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(1, 5)
    stop = random.randrange(400, 700)
    sr = [x, y, r, r, stop]
    srain.append(sr)

for i in range(num_big_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(10, 14)
    stop = random.randrange(600, 700)
    br = [x, y, r, r, stop]
    brain.append(br)

for i in range(num_huge_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(30, 50)
    stop = random.randrange(600, 700)
    hr = [x, y, r, r, stop]
    hrain.append(hr)



# game loop
done = False
lightning = False 

while not done:
    # event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lightning = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                lightning = False

    # game logic
    ''' move clouds '''
    for c in clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    ''' move rain '''
    for sr in srain:
        sr[0] -= 1
        sr[1] += 4

        if sr[1] > sr[4]:
            sr[0] = random.randrange(0, 1000)
            sr[1] = random.randrange(-100, 0)

    for br in brain:
        br[0] -= 2
        br[1] += 8

        if br[1] > br[4]:
            br[0] = random.randrange(0, 1000)
            br[1] = random.randrange(-100, 0)

    for hr in hrain:
        hr[0] -= random.randrange(3, 5)
        hr[1] += random.randrange(10, 14)

        if hr[1] > hr[4]:
            hr[0] = random.randrange(0, 1000)
            hr[1] = random.randrange(-100, 0)
        

    # drawing code
    ''' sky '''
    if lightning:
        screen.fill(YELLOW)
    else:
        screen.fill(NIGHT_SKY) 

    ''' sun '''
    #pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' small rain ''' 
    for sr in srain:
        draw_small_drop(sr)
        

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    ''' big rain '''
    for br in brain:
        draw_big_drop(br)

    ''' huge rain '''
    for hr in hrain:
        draw_huge_drop(hr)


    # update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# close window on quit
pygame.quit()
