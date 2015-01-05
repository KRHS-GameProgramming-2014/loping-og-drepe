import pygame, sys
from Player import Player
from Button import Button


pygame.init()

clock = pygame.time.Clock

width = 1000
height = 715
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("BL1.png").convert()
bgRect = bgImage.get_rect()

players = []
player1 = [Player(1, "ball.png",[0,0], [100,100])]
player1 + [Player(1, "ball.png",[0,0], [100,100])]

run = False

startButton = Button([width/2, height-300], 
				     "Start_Base.png", 
				     "Start_Clicked.png")

while True:
	while not run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					run = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				startButton.click(event.pos)
			if event.type == pygame.MOUSEBUTTONUP:
				if startButton.release(event.pos):
					run = True
					
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(startButton.image, startButton.rect)
		pygame.display.flip()
		
		
	bgImage = pygame.image.load("BL1.png").convert()
	bgRect = bgImage.get_rect()
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					player1.go("up")
				if event.key == pygame.K_d:
					player1.go("right")
				if event.key == pygame.K_s:
					player1.go("down")
				if event.key == pygame.K_a:
					player1.go("left")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					player1.go("stop up")
				if event.key == pygame.K_d:
					player1.go("stop right")
				if event.key == pygame.K_s:
					player1.go("stop down")
				if event.key == pygame.K_a:
					player1.go("stop left")
					
while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player.go("up")
				if event.key == pygame.K_RIGHT:
					player.go("right")
				if event.key == pygame.K_DOWN:
					player.go("down")
				if event.key == pygame.K_LEFT:
					player.go("left")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					player.go("stop up")
				if event.key == pygame.K_RIGHT:
					player.go("stop right")
				if event.key == pygame.K_DOWN:
					player.go("stop down")
				if event.key == pygame.K_LEFT:
					player.go("stop left")
	
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(player.image, player.rect)
		pygame.display.flip()
		clock.tick(60)
