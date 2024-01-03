# Spaceion is a 2d vertical scrolling game where it tests the
# users reaction time and gamer instincts. The game takes place in space
# and the primary objective of the game is to reach planet Earth while
# dodging various obstacles and utilizing power-ups to your advantage. 
# Made by Vishal Thilak

import simplegui, math, random, time

# CONSTANTS===========================================================================================================================================

FRAME_WIDTH = 1000 
FRAME_HEIGHT = 1000

PLAYER_SPEED = 13
PLAYER_SIDE_SPEED = 20
PLAYER_HEALTH = 5
PLAYER_STILL_SIZE = [99, 122]
PLAYER_COLS = 4
PLAYER_ROWS = 2
PLAYER_IMG_SIZE = [398/PLAYER_COLS, 308/PLAYER_ROWS]
PLAYER_MOVING_SIZE = [101, 156]
PLAYER_SIZE = [175, 175]
PLAYER_CENTER  = [PLAYER_SIZE[0]/2, PLAYER_SIZE[1]/2]

MAX_HEIGHT = 550
STARTING_POSITION = [500, 600]
GRAVITY = 6 # Acting only on player

# Scroll speeds when boosting and not boosting
BOOST_SPEED = 28
NORMAL_SPEED = 15

LASER_SIZE = [50, 50]
LASER_SPEED = [0, -10]

LIGHTNING_SIZE = [75, 75]
LIGHTNING_VEL = (0, 0)

BULLET_CASE_SIZE = [100, 100]
BULLET_POUCH_POS = [895, 32]
BULLET_POUCH_SIZE = [80, 90]

ASTEROID_SIZE = [100, 100]

BLACKHOLE_SIZE = (120, 120)
BLACKHOLE_VEL = (0, 0)

EARTH_SIZE = [950, 950]
EARTH_POS = [500, -300]
EARTH_COLS = 16
EARTH_ROWS = 16

EXP_ROWS = 5
EXP_COLS = 5

ROCK_SIZE = [500, 500]
ROCK_POS = [500, 0]
ROCK_VEL = [0, -20]

# Point where things are kicked up a notch
FINAL_MARK = 5000

# Final scroll speed
FINAL_SPEED = 40

# Button sizes for rectangular buttons
RECT_BUTTON_WID = 300
RECT_BUTTON_HEI = 100

# Button sizes for square button
SQUARE_BUTTON_WID = 100 
SQUARE_BUTTON_HEI = 100

# IMAGES ===============================================================================================================

PLAYER_IMG = simplegui.load_image("https://opengameart.org/sites/default/files/spaceship.pod_.1.blue__0.png")
ASTEROID_IMG = simplegui.load_image("https://cdn2.iconfinder.com/data/icons/space-cartoon/512/sim4313-512.png")
METEORITE_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142956993854840933/meteor-26464.png")
LASER_IMG = simplegui.load_image("https://res.cloudinary.com/mirukusheku/image/upload/v1495140035/Red_laser-ConvertImage_votu8o.png")
BLACKHOLE_IMG = simplegui.load_image("https://icons.iconarchive.com/icons/zairaam/bumpy-planets/256/blackhole-icon.png")
BKGD = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1143231749766266900/stary.png")
LIGHTNING_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1143239400331948053/lightning.png") 
PLATFORM_IMG = simplegui.load_image("data:image/jpeg;base64,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")
HEART_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1143229679017414736/hearts.png")
PLANET_SPRITE = simplegui.load_image("https://i.stack.imgur.com/HmyRu.png")
EXP_IMG = simplegui.load_image("https://static.packt-cdn.com/products/9781785880957/graphics/B05066_08_01.png")
PLAYER_SPRITE = simplegui.load_image("https://www.pngkit.com/png/full/241-2414314_rocket-ship-sprite-sheet.png")
PLAYER_STILL = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142972060210053150/shipstill.png") 
PLAYER_MOVING = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142972626420113549/shipmove.png") 
EARTH_SPRITE = simplegui.load_image("https://s3.us-east-2.amazonaws.com/singular-assets/Global/Earth1024x1024_256Frames.png")
BULLET_POUCH = simplegui.load_image("https://steamuserimages-a.akamaihd.net/ugc/789741591334706643/378A4229E47D60D0A41FEE565300F2A49D71ABC6/")
BULLET_CASE_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1143240936550309928/bulletcase.png")
PLAY_BUTTON_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142959379063259136/image.png")
MENU_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142959907579101324/1094289_2.png")
MOON_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142973342924681306/pngimg.com_-_moon_PNG20.png") 
GAME_OVER_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142960469540360254/Untitled_1.png")
PLAY_AGAIN_BUTTON = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142967718803415160/Rounded_Rectangle.png")
HOME_BUTTON = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142961909881127012/335-3354019_white-home-button-icon-png-for-kids-white.png")
WIN_SCREEN_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142962276937257010/Very_Black_screen.jpg")
CONTROLS_BUTTON = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142962465953566750/15.5x23_Yellow_1024x1024_4.png")
CONTROLS_SCREEN_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142962678109851718/Untitled_3.png")
TIPS_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142963073074876526/Untitled_5.png")
TIPS_BUTTON = simplegui.load_image("https://cdn.discordapp.com/attachments/931333327695282249/1142963355049545818/15.5x23_Yellow_1024x1024_5.png")

# DICTIONARIES=========================================================================================================================================

IMG_SIZES = {#Player image
              BKGD:[1000, 2000],
              PLAYER_IMG:[422, 372],
              ASTEROID_IMG:[512, 512],
              LIGHTNING_IMG:[100, 100],
              METEORITE_IMG:[1000, 1000],
              LASER_IMG:[200, 600],
              BLACKHOLE_IMG:[256, 256],
              BULLET_CASE_IMG:[486,260],
              HEART_IMG:[490,117],
              EXP_IMG:[[500/EXP_COLS/2,500/EXP_ROWS/2],
              [500/EXP_COLS,500/EXP_ROWS]],
              EARTH_SPRITE:[1024/EARTH_COLS, 1024/EARTH_ROWS],
              BULLET_POUCH: [640, 480],
              PLAY_BUTTON_IMG:[300, 100],
              MOON_IMG:[1000, 997],
              GAME_OVER_IMG:[1000, 1000],
              PLAY_AGAIN_BUTTON:[523, 295],
              HOME_BUTTON:[2044, 1811],
              CONTROLS_BUTTON:[300, 100],
              TIPS_BUTTON:[300, 100]}

# SOUNDS=============================================================================================================================================

EXP_SOUND = simplegui.load_sound("https://cdn.discordapp.com/attachments/931333327695282249/1143223610811617380/explosion_02.wav")
FINAL_SOUND = simplegui.load_sound("https://cdn.discordapp.com/attachments/931333327695282249/1143226197422129163/Cat_Transcendence_-_The_prophecy_is_true_128_kbps-AudioTrimmer.com.mp3")
SHOOT_SOUND = simplegui.load_sound("https://cdn.discordapp.com/attachments/931333327695282249/1143224264686838001/alien_shoot.wav")
MENU_SOUND = simplegui.load_sound("https://cdn.discordapp.com/attachments/931333327695282249/1143225370661896232/Arcade-Fantasy-AudioTrimmer.com_2-AudioTrimmer.com_1.mp3")
GAME_MUSIC = simplegui.load_sound("https://cdn.discordapp.com/attachments/931333327695282249/1143225661234884820/music_zapsplat_game_music_action_mild_agressive_bass_synth_breakbeat_027.mp3")
GAME_OVER_SOUND = simplegui.load_sound("https://cdn.discordapp.com/attachments/931333327695282249/1143224652374745088/9convert.com_-_Videogame_Death_Sound_Effect_HD_No_Copyright.mp3")
VICTORY_SOUND = simplegui.load_sound("https://cdn.discordapp.com/attachments/931333327695282249/1143224914522939493/Ta_Da.mp3")

# GLOBAL VARIABLES===================================================================================================================================

# Initialize an empty list to hold obstacles when created
asteroid_list = []
laser_list = []
blackhole_list = []
lightning_list = []
bullet_case_list = []

# Scroller
background_pos = [IMG_SIZES[BKGD][0]/2,0]
screen_scroll = False

# Time
t = 0

# Boolean if player has collided into laser
# Used because the laser has a set duration
has_collided = False

# Boolean for whether or not game is in the playing mode
playing = False

# Game states
MENU = 0
GAME = 1
GAME_OVER = 2
WIN = 4
CONTROLS = 5
TIPS = 6
screen = MENU # default screen state

# Default spawn rates which get altered in the finale
asteroid_spaw_rate = 100 
blackhole_spawn_rate = 250

# Player bullet count
player_bullets = 10

# HELPER FUNCTIONS================================================================================================= 

def new_game():
    global player, health, moon, earth, game_over_sound, victory_sound
    player = Character(PLAYER_SPRITE, PLAYER_SIZE, 
                       STARTING_POSITION.copy(), 
                       PLAYER_HEALTH, 
                       NORMAL_SPEED)
    health = Health_bar(HEART_IMG)
    
    # Only comes in the final part of game
    moon = Obstacles(MOON_IMG, [400, 400], ROCK_POS.copy(), ROCK_VEL) 
    earth = Planet(EARTH_SPRITE, EARTH_SIZE, EARTH_POS.copy())
    
    # Sounds
    game_over_sound = True
    victory_sound = True
    
    # clears lists
    asteroid_list.clear() 
    laser_list.clear() 
    blackhole_list.clear() 
    lightning_list.clear() 
    bullet_case_list.clear()

    screen = GAME

# To detect if obstacles go offscreen
def offscreen(pos):
    off = False
    if pos[0] < -50 or pos[0] > 1050:
        off = True
    if pos[1] < -500 or pos[1] > 1250:
        off = True
    return off    

# Uses pythagorean theorem to calculate distance between 
# pos1 and pos2 
def distance(pos1, pos2):
    a = pos1[0] - pos2[0]
    b = pos1[1] - pos2[1]
    dist = math.sqrt(a**2 + b **2)
    return dist

# Generates random velocities and positions for moving obstacles
def randomstats():
    if random.randrange(1, 3) == 1:
        x = random.randrange(0, 50)
    else:
        x = random.randrange(950, 1000)
    
    y = random.randrange(0, 50)
    position = [x, y]
    x_vel = random.randrange(12, 15)
    if 0 <= position[0] <= 50:
        x_vel *= 1
    else:
        x_vel *= -1
    
    y_vel = random.randrange(3, 5)
    y_vel *= random.choice([-1, 1])
    velocity = [x_vel, y_vel]
    return position,velocity

# Generate random positions for non-moving obstacles
def randompos():
    pos_x = random.randrange(0, 1000)
    pos_y = random.randrange(-50, 0)
    position = [pos_x, pos_y]
    return position

# Performs a triangular collision check with obstacles and items
# Takes in a desired hitbox as the obstacle images aren't all the same
def collided(player, other_obj, hitbox):
    collision = False

    # First hitbox from top to bottom 
    top = player.pos[1] - PLAYER_SIZE[1]/2 - other_obj.size[1]/hitbox 
    bottom = player.pos[1] + PLAYER_SIZE[1]/4 + other_obj.size[1]/hitbox 
    left = player.pos[0] - PLAYER_SIZE[0]/2 - other_obj.size[0]/hitbox 
    right = player.pos[0] + PLAYER_SIZE[0]/2 + other_obj.size[0]/hitbox 

    if left < other_obj.pos[0] < right and top < other_obj.pos[1] < bottom:
        collision = True
       
    return collision

# Spawns all the buttons for the game
def spawn_button():
    global start_button, play_again_button, home_button, controls_button, tips_button
    start_button = Button(PLAY_BUTTON_IMG, [500, 675], RECT_BUTTON_WID, RECT_BUTTON_HEI)
    play_again_button = Button(PLAY_AGAIN_BUTTON, [125, 900], 125, 125)
    home_button = Button(HOME_BUTTON, [900, 900], SQUARE_BUTTON_WID, SQUARE_BUTTON_HEI)
    controls_button = Button(CONTROLS_BUTTON, [500, 800], RECT_BUTTON_WID, RECT_BUTTON_HEI)
    tips_button = Button(TIPS_BUTTON, [500, 925], RECT_BUTTON_WID, RECT_BUTTON_HEI)

# CLASSES==================================================================================================================
                        
class Character:
    
    def __init__(self, image, size, position, health, scroll_speed):
        self.img = image
        self.size = size
        self.pos = position
        self.vel = [0, 0]
        self.BOOST_SPEED = 10
        self.boost_timer = 0
        self.health = health
        self.animated1 = False # For moving sideways
        self.animated2 = False # For moving forward
        self.time = 0
        self.disp = 0
        self.scroll_speed = scroll_speed
        self.bullets = player_bullets
        
    def draw(self, canvas):
        # When moving left or right do turning animation
        if self.animated1:
            column = math.floor(self.time%PLAYER_COLS)
            row = 1
            # Note for the third column, couldn't divide the
            # player's width by 2 as its slightly offset which is why
            # it is divided by 2.1
            if column == 3:
                tile_center = [PLAYER_IMG_SIZE[0]/2.1 + column*PLAYER_IMG_SIZE[0],    
                       PLAYER_IMG_SIZE[1]/2 + row*PLAYER_IMG_SIZE[1]]
                
            else:
                tile_center = [PLAYER_IMG_SIZE[0]/2 + column*PLAYER_IMG_SIZE[0],    
                       PLAYER_IMG_SIZE[1]/2 + row*PLAYER_IMG_SIZE[1]]
            
            canvas.draw_image(self.img,
                          tile_center,   
                          PLAYER_IMG_SIZE,
                          self.pos,
                          PLAYER_SIZE)
        # When moving forward do moving animation     
        elif self.animated2:
            width, height = PLAYER_MOVING_SIZE
            canvas.draw_image(PLAYER_MOVING, 
                          (width/2, height/2), 
                          (width, height), 
                          self.pos, 
                          [175, 190])
        # When not moving use stationary animation    
        else:
            width, height = PLAYER_STILL_SIZE
            canvas.draw_image(PLAYER_STILL, 
                          (width/2, height/2), 
                          (width, height), 
                          self.pos, 
                          self.size)
            
    def update(self):
        global screen_scroll
        self.pos[0] += self.vel[0] 
        self.pos[1] += self.vel[1] + GRAVITY
       
        if self.pos[1] < MAX_HEIGHT:
            self.pos[1] = MAX_HEIGHT
            screen_scroll = True
        else:
            screen_scroll = False
        # Allows player to wrap around screen in the horizontal direction   
        self.pos[0] = self.pos[0] % FRAME_WIDTH
        if self.animated1:
            # Slower time increment to get slower animation
            self.time += 0.3
            
    def shoot(self):
        position = [self.pos[0], self.pos[1] - PLAYER_SIZE[1]/2]
        new_laser = Laser(LASER_IMG, position, LASER_SIZE, LASER_SPEED, 
                          (LASER_SIZE[0]/2,
                           LASER_SIZE[1]/2))
        laser_list.append(new_laser)
        
    # Allows player to temporarily change scroll_speed with an item
    def boost(self, vel):
        self.scroll_speed = vel

class Health_bar:
    
    def __init__(self, image):
        self.img = image
        self.size = [200, 50]
        self.pos = [108, 60]
        self.player_health = 5
        
    def draw(self, canvas):
        width, height = IMG_SIZES[self.img]
        canvas.draw_image(self.img, 
                          (width/2, height/2), 
                          (width, height), 
                          self.pos, 
                          self.size)
        
    def lost_health(self):
        if player.health == (self.player_health - 1):
            self.player_health = player.health
            self.pos[0] -= 42
        else:
            self.player_health = player.health
            self.pos[0] -= 84
            
class Laser:
    
    def __init__(self, image, position, size, velocity, center):
        self.img = image
        self.pos = position
        self.size = size
        self.vel = velocity
        self.cen = center
    
    def draw(self, canvas):
        width, height = IMG_SIZES[LASER_IMG]
        canvas.draw_image(self.img, 
                          (width/2, height/2), 
                          (width, height), 
                          self.pos, 
                          self.size)
    def update(self):
        for i in range(2):
            self.pos[i] += self.vel[i]
    
    # Performs a rectangular collision check with obstacles       
    def has_collided(self, other_obs):
        collision = False
        left_boundary =  self.pos[0] - self.size[0]/2 - other_obs.size[0]/2
        right_boundary = self.pos[0] + self.size[0]/2  + other_obs.size[0]/2
        upper_boundary = self.pos[1] - self.size[1]/2 - other_obs.size[1]/2
        lower_boundary = self.pos[1] + self.size[1]/2 + other_obs.size[1]/2
        
        if left_boundary < other_obs.pos[0] < right_boundary and  upper_boundary < other_obs.pos[1] < lower_boundary:
            collision = True
        return collision

class Items:
    
    def __init__(self, image, size, position):
        self.img = image
        self.size = size
        self.pos = position
        self.vel = (0, 2)
        
    def draw(self, canvas):
        width, height = IMG_SIZES[self.img]
        canvas.draw_image(self.img, 
                          (width/2, height/2), 
                          (width, height), 
                          self.pos, 
                          self.size)
    def update(self):
        for i in range(2):
            self.pos[i] += self.vel[i]     
        if screen_scroll:
            self.pos[1] += player.scroll_speed

class Obstacles:
    
    def __init__(self, image, size, position, velocity):
        self.img = image
        self.size = size
        self.pos = position
        self.vel = velocity
        self.animated = False
        self.time = 0
        
    def draw(self, canvas):
        if self.animated:
            center1 = IMG_SIZES[EXP_IMG][0]
            width, height = IMG_SIZES[EXP_IMG][1]
            col = self.time % EXP_COLS
            row = self.time // EXP_COLS
            tile_center = tile_center = [center1[0] + col*width, 
                           center1[1] + row*height]
            canvas.draw_image(EXP_IMG,
                              tile_center, 
                              IMG_SIZES[EXP_IMG][1],
                              self.pos,
                              [self.size[0]*2,self.size[1]*2])                      
                       
        else:
            width, height = IMG_SIZES[self.img]
            canvas.draw_image(self.img, 
                          (width/2, height/2), 
                          (width, height), 
                          self.pos, 
                          self.size)
 
    def update(self):
        for i in range(2):
            self.pos[i] += self.vel[i]     
        if screen_scroll:
            self.pos[1] += player.scroll_speed
        if self.animated:
            self.time += 1

class Planet:
    
    def __init__(self, image, size, position):
        self.img = image
        self.size = size
        self.pos = position
        self.vel = [0, 4.01]
        self.time = 0 # For rotating animation
        
    def draw(self, canvas):
            
        width, height = IMG_SIZES[self.img]
        column = self.time % EARTH_COLS 
        row = self.time // EARTH_COLS 
        tile_center = [width/2 + column*width,    
                       height/2 + row*height]
        canvas.draw_image(self.img,
                          tile_center,   
                          IMG_SIZES[self.img],
                          self.pos,
                          self.size)
        
    def update(self):
        for i in range(2):
            self.pos[i] += self.vel[i] 
        self.time += 1
        self.time %= EARTH_COLS * EARTH_ROWS # Reset after last tile

class Button:
    
    def __init__(self, image, position, width, height):
        self.img = image
        self.pos = position
        self.width = width
        self.height = height
  
        
    def draw(self, canvas):
        width, height = IMG_SIZES[self.img]
        canvas.draw_image(self.img, 
                          (width/2, height/2), 
                          (width, height), 
                          self.pos, 
                          (self.width, self.height))
        
    def is_selected(self, mouse_pos):
        left = self.pos[0] - self.width
        right = self.pos[0] + self.width
        top = self.pos[1] -  self.height/2
        bottom = self.pos[1] + self.height/2
        in_x = mouse_pos[0] >= left and mouse_pos[0] <= right
        in_y = mouse_pos[1] >= top and mouse_pos[1] <= bottom
        return in_x and in_y
    
# Handler to draw on canvas
def draw(canvas):
    
    global GAME_OVER_TIMER, screen, has_collided, health, screen_scroll 
    global lightning_list, asteroid_spawn_rate, blackhole_spawn_rate 
    global song_timer, game_over_sound, victory_sound
    
    # Menu screen   
    
    if screen == MENU:
        GAME_OVER_SOUND.pause()
        MENU_SOUND.play()
        screen_scroll = False
        canvas.draw_image(MENU_IMG,
                          [FRAME_WIDTH/2, FRAME_HEIGHT/2], 
                          [FRAME_WIDTH, FRAME_HEIGHT],
                          [FRAME_WIDTH/2, FRAME_HEIGHT/2], 
                          [FRAME_WIDTH, FRAME_HEIGHT]) 
        # Button draw
        start_button.draw(canvas)
        controls_button.draw(canvas)
        tips_button.draw(canvas)
        
        # Spawns asteroid for aesthetic purposes
        for asteroid in asteroid_list:
            asteroid.draw(canvas)
            asteroid.update()
            if offscreen(asteroid.pos):
                asteroid_list.remove(asteroid) # Removing when offscreen
        if random.randrange(100) == 0: # Spawn rate
            position,velocity = randomstats()
            new_asteroid = Obstacles(ASTEROID_IMG,
                                   ASTEROID_SIZE,
                                    position, velocity)
            asteroid_list.append(new_asteroid)
            
    # New game screen
    
    if screen == GAME:
        
        # To calculate current time which is used for duration for boost item
        current_time = time.time()
        MENU_SOUND.pause()
        
        # Background image
        width, height = IMG_SIZES[BKGD]
        canvas.draw_image(BKGD,
                      (width/2, height/2),
                      (width, height),
                      background_pos,
                      (width, height))
        # Laser
        for laser in laser_list:
            laser.draw(canvas)
            laser.update()
            if offscreen(laser.pos):
                laser_list.remove(laser) # Removing when offscreen 

        # Player
        player.draw(canvas)
        player.update()
        if player.health <= 0:
            screen = GAME_OVER
            
        if player.pos[1] > FRAME_HEIGHT:
            screen = GAME_OVER
            

        if screen_scroll:
            background_pos[1] += player.scroll_speed
            background_pos[1] %= height/2
            
        # Items
        # Boost
        # Doesn't spawn a bit before the finale
        
        if player.disp <= FINAL_MARK - 400:
            if random.randrange(600) == 0:
                position = randompos()
                new_lightning = Items(LIGHTNING_IMG,
                                          LIGHTNING_SIZE,
                                          position)
                lightning_list.append(new_lightning)
        for lightning in lightning_list:
            lightning.draw(canvas)
            lightning.update()
            if offscreen(lightning.pos):
                lightning_list.remove(lightning)
            if collided(player, lightning, 2):
                global time1
                time1 = time.time()
                player.boost(BOOST_SPEED)
                has_collided = True
        if has_collided and (current_time - time1) > 2:
            player.boost(NORMAL_SPEED)
            has_collided = False
            
        # Bullet Cases
        for bullet_case in bullet_case_list:
            bullet_case.draw(canvas)
            bullet_case.update()
            if offscreen(bullet_case.pos):
                bullet_case_list.remove(bullet_case)
            if collided(player, bullet_case, 2):
                bullet_case_list.remove(bullet_case)
                player.bullets += 1
        if random.randrange(500) == 0:
            position = randompos()
            new_bullet_case = Items(BULLET_CASE_IMG,
                                      BULLET_CASE_SIZE,
                                      position)
            bullet_case_list.append(new_bullet_case)
            
        # Obstacles
        # Asteroid 
        for asteroid in asteroid_list:
            asteroid.draw(canvas)
            asteroid.update()
            if offscreen(asteroid.pos):
                asteroid_list.remove(asteroid) # Removing when offscreen
            elif collided(player, asteroid, 2): # When collided with a player queue explosion 
                if not asteroid.animated:
                    asteroid.animated = True  
                    player.health -= 1
                    health.lost_health()
                    EXP_SOUND.play()
                
            # So that it only removes the asteroid if after the explosion    
            elif asteroid.time == EXP_ROWS*EXP_COLS:
                asteroid_list.remove(asteroid)        
        if random.randrange(asteroid_spaw_rate) == 0: # Spawn rate
            position,velocity = randomstats()
            new_asteroid = Obstacles(ASTEROID_IMG,
                                   ASTEROID_SIZE,
                                    position, velocity)
            asteroid_list.append(new_asteroid)

        # Checks to see if laser and asteroid have collided and removes
        # them if they are and queues explosion animation
        for asteroid in asteroid_list:    
            for laser in laser_list:
                if laser.has_collided(asteroid):
                    asteroid.animated = True  
                    laser_list.remove(laser)
                    EXP_SOUND.rewind()
                    EXP_SOUND.play()
            if asteroid.time == EXP_ROWS*EXP_COLS:
                asteroid_list.remove(asteroid)    

        # Blackhole
        for blackhole in blackhole_list:
            blackhole.draw(canvas)
            blackhole.update()
            if offscreen(blackhole.pos):
                blackhole_list.remove(blackhole) 
            if collided(player, blackhole, 2):   # Removes black hole when
                blackhole_list.remove(blackhole) # when collided    
                player.health -= 2
                health.lost_health()
        if random.randrange(blackhole_spawn_rate) == 0:
            position = randompos()
            new_blackhole = Obstacles(BLACKHOLE_IMG,
                                      BLACKHOLE_SIZE,
                                      position, BLACKHOLE_VEL)
            blackhole_list.append(new_blackhole)
            
        # Things that only happen at the final part of game
        # Planet
        
        if player.disp >= FINAL_MARK:
            GAME_MUSIC.rewind()
            FINAL_SOUND.play() # Queues final/boss music
            player.scroll_speed = FINAL_SPEED
            # Spawn rates for asteroid and blackhole increase
            asteroid_spawn_rate = 80
            blackhole_spawn_rate = 200

        else:
            GAME_MUSIC.play()
            FINAL_SOUND.rewind()
       
        if player.disp >= FINAL_MARK + 1657:
            # Spawns rock at the same time the bass drops for song
            # Rock doesn't actually do any damage just there to
            # scare the player
            moon.draw(canvas)
            moon.update()
            
        if player.disp >= FINAL_MARK + 5000:
            # Slows down player as Earth is coming near
            player.scroll_speed = 3
        if player.disp >= FINAL_MARK + 5500:
            earth.draw(canvas)
            earth.update()
            if collided(player, earth, 2.2):  
                    screen = 4
                    EXP_SOUND.play() 	     
       
        # Drawing the hearts on the screen
        health.draw(canvas)
        
        # Adds to the displacement when scrolling the screen
        if screen_scroll:
            # When moving at the normal speed
            if player.scroll_speed == NORMAL_SPEED:
                player.disp += 1
            # During the finale
            elif player.scroll_speed == FINAL_SPEED:
                player.disp += 2
            # When boosting
            else:
                player.disp += 3
        
        # Showing displacement count
        canvas.draw_text(str(player.disp), (15, 34), 40, "Red")

        # Print bullet count
        width, height = IMG_SIZES[BULLET_POUCH]
        canvas.draw_image(BULLET_POUCH, 
                              (width/2, height/2), 
                              (width, height), 
                              BULLET_POUCH_POS, 
                              BULLET_POUCH_SIZE)
        canvas.draw_text("x" + str(player.bullets), (935, 40), 40, "Gold")
        
    # End screen
    if screen == GAME_OVER:
        if game_over_sound:
            GAME_OVER_SOUND.play()
            game_over_sound = False
        GAME_MUSIC.pause()
        width, height = IMG_SIZES[GAME_OVER_IMG]
        canvas.draw_image(GAME_OVER_IMG, 
                          (width/2, height/2), 
                          (width, height), 
                          (FRAME_WIDTH/2, FRAME_HEIGHT/2), 
                          (FRAME_WIDTH, FRAME_HEIGHT))
        play_again_button.draw(canvas)
        home_button.draw(canvas)
        canvas.draw_text("Score: " + str(player.disp), (361, 300), 45, 
                         "#C0F8FF")
        if player.disp >= FINAL_MARK: 
            FINAL_SOUND.pause()  
            
    # Win screen        
    if screen == WIN:
        if victory_sound:
            VICTORY_SOUND.play()
            victory_sound = False
       
        canvas.draw_image(WIN_SCREEN_IMG, 
                          (FRAME_WIDTH/2, FRAME_HEIGHT/2), 
                          (FRAME_WIDTH, FRAME_HEIGHT), 
                          (FRAME_WIDTH/2, FRAME_HEIGHT/2), 
                          (FRAME_WIDTH, FRAME_HEIGHT))
        home_button.draw(canvas)
    
    # Controls screen
    if screen == CONTROLS : 
        canvas.draw_image(CONTROLS_SCREEN_IMG, 
                          (FRAME_WIDTH/2, FRAME_HEIGHT/2), 
                          (FRAME_WIDTH, FRAME_HEIGHT), 
                          (FRAME_WIDTH/2, FRAME_HEIGHT/2), 
                          (FRAME_WIDTH, FRAME_HEIGHT))
        home_button.draw(canvas)
    
     # Tips screen
    if screen == TIPS : 
        canvas.draw_image(TIPS_IMG, 
                          (FRAME_WIDTH/2, FRAME_HEIGHT/2), 
                          (FRAME_WIDTH, FRAME_HEIGHT), 
                          (FRAME_WIDTH/2, FRAME_HEIGHT/2), 
                          (FRAME_WIDTH, FRAME_HEIGHT))
        home_button.draw(canvas)

        # Handler for when mouse is clicked    
        
def mouse_click(mouse_position):
    global screen, playing
    if screen == MENU:
        if start_button.is_selected(mouse_position):
            screen = GAME
            new_game()
        if controls_button.is_selected(mouse_position):
            screen = CONTROLS
        if tips_button.is_selected(mouse_position):
            screen = TIPS
    if screen == MENU or screen == WIN or screen == CONTROLS or screen == TIPS:
        if home_button.is_selected(mouse_position):
            screen = MENU
    
  
    if screen == GAME_OVER:
        if play_again_button.is_selected(mouse_position):
            GAME_OVER_SOUND.rewind()
            MENU_SOUND.rewind()
            new_game()
            screen = GAME
        if home_button.is_selected(mouse_position):
            screen = MENU
            GAME_OVER_SOUND.rewind()
            MENU_SOUND.rewind()
            MENU_SOUND.play()

# Handler for when keyboard key is pressed   
def key_down(key):
    global bullets
    # To make sure player can only press the buttons when in game mode
    if screen == GAME:
        if key == simplegui.KEY_MAP['w']:
            player.vel[1] = -PLAYER_SPEED
            player.animated2 = True

        if key == simplegui.KEY_MAP['s']:
            if player.disp <= FINAL_MARK:

                player.vel[1] = PLAYER_SPEED
            else:
                # Doesn't let player go backwards in the finale
                player.vel[1] = -PLAYER_SPEED
        if key == simplegui.KEY_MAP['a']:
            player.vel[0] = -PLAYER_SIDE_SPEED
            player.animated1 = True
        if key == simplegui.KEY_MAP['d']:
            player.animated1 = True
            player.vel[0] = PLAYER_SIDE_SPEED
        if key == simplegui.KEY_MAP['up']:
            if player.bullets > 0:
                player.bullets -= 1
                if player.bullets >= 0:
                    player.shoot()
                    SHOOT_SOUND.rewind()
                    SHOOT_SOUND.play()

# Handler for when keyboard key is released        
def key_up(key):
    if screen == GAME:
        if key == simplegui.KEY_MAP['w']:
            if player.disp <= FINAL_MARK:
                # Forces player to go forward during finale
                player.vel[1] = 0
                player.animated2 = False

        if key == simplegui.KEY_MAP['s']:
            if player.disp <= FINAL_MARK:
                player.vel[1] = PLAYER_SPEED
            else:
                # Doesn't let player go backwards during finale
                player.vel[1] = -PLAYER_SPEED
        if key == simplegui.KEY_MAP['a']:
            player.vel[0] = 0
            player.animated1 = False
        if key == simplegui.KEY_MAP['d']:
            player.vel[0] = 0
            player.animated1 = False

# Buttons
spawn_button()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Spaceion", FRAME_WIDTH, FRAME_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_mouseclick_handler(mouse_click)
frame.set_canvas_background("white")
frame.add_label("Hello user, we have found that the journey is a bit over 10, 000 light years. ")
frame.add_label("Press expand and zoom in and out by using control +/- for optimal screen size")

# Start the frame animation
new_game()
frame.start()
