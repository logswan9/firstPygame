import sys
import pygame
import random
from pygame.locals import (
	RLEACCEL,
	K_UP,
	K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)


# Constants/load images
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
PLAYER_SHIP = pygame.image.load("images/nightraiderfixed.png")
PLAYER_SHIP = pygame.transform.scale(PLAYER_SHIP, (100, 80))
ASTEROID = pygame.image.load("images/Asteroid2.png")
ASTEROID = pygame.transform.scale(ASTEROID, (50, 50))
ASTEROIDROLL1 = pygame.image.load("images/Asteroid2.png")
ASTEROIDROLL2 = pygame.image.load("images/Asteroid2.png")
ASTEROIDROLL3 = pygame.image.load("images/Asteroid2.png")
ASTEROIDROLL4 = pygame.image.load("images/Asteroid2.png")
ASTEROIDROLL5 = pygame.image.load("images/Asteroid2.png")
ASTEROIDROLL6 = pygame.image.load("images/Asteroid2.png")
ASTEROIDROLL7 = pygame.image.load("images/Asteroid2.png")
ASTEROIDROLL1 = pygame.transform.scale(ASTEROIDROLL1, (50, 50))
ASTEROIDROLL2 = pygame.transform.scale(ASTEROIDROLL2, (50, 50))
ASTEROIDROLL3 = pygame.transform.scale(ASTEROIDROLL3, (50, 50))
ASTEROIDROLL4 = pygame.transform.scale(ASTEROIDROLL4, (50, 50))
ASTEROIDROLL5 = pygame.transform.scale(ASTEROIDROLL5, (50, 50))
ASTEROIDROLL6 = pygame.transform.scale(ASTEROIDROLL6, (50, 50))
ASTEROIDROLL7 = pygame.transform.scale(ASTEROIDROLL7, (50, 50))
ASTEROIDROLL1 = pygame.transform.rotate(ASTEROIDROLL1, 45)
ASTEROIDROLL2 = pygame.transform.rotate(ASTEROIDROLL2, 90)
ASTEROIDROLL3 = pygame.transform.rotate(ASTEROIDROLL3, 135)
ASTEROIDROLL4 = pygame.transform.rotate(ASTEROIDROLL4, 180)
ASTEROIDROLL5 = pygame.transform.rotate(ASTEROIDROLL5, 225)
ASTEROIDROLL6 = pygame.transform.rotate(ASTEROIDROLL6, 270)
ASTEROIDROLL7 = pygame.transform.rotate(ASTEROIDROLL7, 315)
STAR_PIC = pygame.image.load("images/star_red01.png ")
STAR_PIC02 = pygame.image.load("images/star_red02.png ")
STAR_PIC03 = pygame.image.load("images/star_red03.png ")
STAR_PIC04 = pygame.image.load("images/star_red04.png ")
STAR_PIC = pygame.transform.scale(STAR_PIC, (200 , 200))
STAR_PIC02 = pygame.transform.scale(STAR_PIC02, (203 , 203))
STAR_PIC03 = pygame.transform.scale(STAR_PIC03, (206 , 206))
STAR_PIC04 = pygame.transform.scale(STAR_PIC04, (209 , 209))
BULLET = pygame.image.load("images/star_blue04.png")
BULLET = pygame.transform.scale(BULLET, (25, 25))
FLAMINGO = pygame.image.load("images/flamingo.png")

# Define player object
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = PLAYER_SHIP
		self.surf.set_colorkey((0, 0, 0), RLEACCEL)
		self.rect = self.surf.get_rect()

	def update(self, pressed_keys):
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)


		# Keep player on screen
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT

		

	def shipLocation(self):
		return self.rect
		

# Define bullet object
class Shoot(pygame.sprite.Sprite):
	def __init__(self, shipPosition):
		super(Shoot, self).__init__()
		self.surf = BULLET
		self.surf.set_colorkey((255, 255, 255), RLEACCEL)
		self.rect = self.surf.get_rect()
		self.speed = 25
		self.shipPosition = shipPosition

	def spawnBullet(self):
		self.rect = self.shipPosition
		self.rect.move_ip(0, 22)

	def update(self):
		self.rect.move_ip(self.speed, 0)
		if self.rect.left > 1000:
			self.kill()
		# KILL AMMO!!!!!!!!!!!!!! 

# Define background mini stars object
class BackgroundStar(pygame.sprite.Sprite):
	def __init__(self):
		super(BackgroundStar, self).__init__()
		self.surf = pygame.Surface((2, 2))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(
			center = (
					random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
					random.randint(0, SCREEN_HEIGHT)

				)
			)
		self.speed = 25

	# Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
	def update(self):
		self.rect.move_ip(-self.speed, 0)
		if self.rect.right < 0:
			self.kill()

# Define asteroids/enemies
class Asteroid(pygame.sprite.Sprite):
	def __init__(self):
		super(Asteroid, self).__init__()
		
		self.sprites = []

		self.sprites.append(ASTEROID)
		self.sprites.append(ASTEROIDROLL1)
		self.sprites.append(ASTEROIDROLL2)
		self.sprites.append(ASTEROIDROLL3)
		self.sprites.append(ASTEROIDROLL4)
		self.sprites.append(ASTEROIDROLL5)
		self.sprites.append(ASTEROIDROLL6)
		self.sprites.append(ASTEROIDROLL7)

		self.index = 0
		self.image = self.sprites[self.index]

		self.rect = self.image.get_rect(
			center = (
					random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
					random.randint(0, SCREEN_HEIGHT)

				)
			)
		self.speed = random.randint(7, 15)

	# Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
	def update(self):
		self.rect.move_ip(-self.speed, 0)

		self.index += 0.1
		if self.index >= len(self.sprites):
			self.index = 0
			
			

		self.image = self.sprites[int(self.index)]
		
		if self.rect.right < 0:
			self.kill()

# STAR background objects
class STAR(pygame.sprite.Sprite):
	def __init__(self):
		super(STAR, self).__init__()

		self.sprites = []
		self.is_animating = False
		self.sprites.append(STAR_PIC)
		self.sprites.append(STAR_PIC02)
		self.sprites.append(STAR_PIC03)
		self.sprites.append(STAR_PIC04)
		
		self.index = 0
		self.image = self.sprites[self.index]
		


		self.rect = self.image.get_rect(
			center = (
					random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
					random.randint(0, SCREEN_HEIGHT)

				)
			)
		self.speed = 6

	def animate(self):
		self.is_animating = True

	def update(self):
		if self.is_animating == True:
			self.index += 0.25
			if self.index >= len(self.sprites):
				self.index = 0
			
			self.rect.move_ip(-self.speed, 0)

			self.image = self.sprites[int(self.index)]
			

			

			if self.rect.right < 0:
				self.kill()


	
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("My First Pygame")
pygame.display.set_icon(FLAMINGO)

#Set up font and score/health
myfont = pygame.font.SysFont('Comic Sans MS', 30, bold=True)
text_for_score = "Score: "
score = 0
text_for_health = "Shield: "
player_health = 100


# Create custom event for adding a new Asteroid and stars
ADDASTEROID = pygame.USEREVENT + 1
pygame.time.set_timer(ADDASTEROID, 250)
ADDSTAR = pygame.USEREVENT + 2
pygame.time.set_timer(ADDSTAR, 3000)
ADDBACKGROUNDSTAR = pygame.USEREVENT + 3
pygame.time.set_timer(ADDBACKGROUNDSTAR, 100)

player = Player()

#Create groups to hold Asteroid sprites and all sprites
asteroids = pygame.sprite.Group()
stars = pygame.sprite.Group()
bullets = pygame.sprite.Group()
backgroundStars = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()
pygame.mixer.music.load("sounds/tecnoFunk.wav")
pygame.mixer.music.play(loops = -1)
explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
thud_sound = pygame.mixer.Sound("sounds/thud.wav")
laser_sound = pygame.mixer.Sound("sounds/laser.wav")





running = True

while running:

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
			if event.key == K_SPACE:
				bullet = Shoot(pygame.Rect(bulletSpawnPoint))
				bullets.add(bullet)
				all_sprites.add(bullet)
				bullet.spawnBullet()
				laser_sound.play()	

		elif event.type == QUIT:
			running = False

		# Add events
		elif event.type == ADDBACKGROUNDSTAR:
			new_backStar = BackgroundStar()
			backgroundStars.add(new_backStar)
			all_sprites.add(new_backStar)

		elif event.type == ADDASTEROID:
			new_asteroid = Asteroid() 
			asteroids.add(new_asteroid)
			#all_sprites.add(new_asteroid)

		elif event.type == ADDSTAR:
			new_star = STAR()
			stars.add(new_star)
			new_star.animate()

		
			
			
			
	# Render score and health to screen
	score_text = myfont.render((text_for_score + str(score)), False, (255, 255, 255))
	health_text = myfont.render((text_for_health + str(player_health) + "%"), False, (255, 255, 255))
	screen.blit(score_text,(0,0))
	screen.blit(health_text, (SCREEN_WIDTH - 200, 0))

	pygame.display.update()
	# Get keys pressed
	pressed_keys = pygame.key.get_pressed()
	
	player.update(pressed_keys)

	backgroundStars.update()
	asteroids.update()
	stars.update()

	
	bullets.update()     
	bulletSpawnPoint = player.shipLocation()
	
	
	

	screen.fill((0, 0, 0))	

	# pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

	# surf = pygame.Surface((50, 50))
	# surf.fill((0, 0, 0))
	# rect = surf.get_rect()
	#surfCenter = (
	#	(SCREEN_WIDTH - surf.get_width()) / 2,
	#	(SCREEN_HEIGHT - surf.get_height()) / 2
	#)

	#  Draw surf/player onto screen with blit
	#     screen.blit(player.surf, player.rect)
	for entity in all_sprites:
		screen.blit(entity.surf, entity.rect)

	# For drawing and animating stars
	for sprite in stars:
		screen.blit(sprite.image, sprite.rect)

	for asteroid in asteroids:
		screen.blit(asteroid.image, asteroid.rect)
	
	# Collision for each bullet and asteroids
	for bullet in bullets:
		gets_hit = pygame.sprite.spritecollide(bullet, asteroids, True)
		if gets_hit:
			bullet.kill()
			thud_sound.play()
			score += 100


	# Check if any asteroids collide with player and if they do, remove the asteroid
	# and play explosion sound while subtracting 1 from the player's health
	for asteroid in asteroids:
		ship_gets_hit = pygame.sprite.spritecollide(player, asteroids, True)
		if ship_gets_hit:
			explosion_sound.play()
			player_health -= 25
			# If player's health reaches 0 and gets hit one more time, kill player and end game
			if player_health < 0:
				player.kill()
				running = False
		
			
		
	
		
		
	

	# Flip everything to display
	#pygame.display.flip()
	#pygame.display.update()


	# Locked at 60 fps
	clock.tick(60)


pygame.quit()	