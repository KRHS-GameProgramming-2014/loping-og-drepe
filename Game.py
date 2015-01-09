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
bgImage = pygame.transform.scale(bgImage, [1850,1445])
bgRect = bgImage.get_rect()

player1 = Player(1, "P1.png",[0,0], [400,200])
player2 = Player(1, "P2.png",[0,0], [750,600])

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
					#print "[DEBUG] w button pressed"
					player1.go("up")
					player1.update(width, height)
				if event.key == pygame.K_d:
					#print "[DEBUG] d button pressed"
					player1.go("right")
					player1.update(width, height)
				if event.key == pygame.K_s:
					#print "[DEBUG] s button pressed"
					player1.go("down")
					player1.update(width, height)
				if event.key == pygame.K_a:
					#print "[DEBUG] a button pressed"
					player1.go("left")
					player1.update(width, height)
				if event.key == pygame.K_UP:
					#print "[DEBUG] up arrow pressed"
					player2.go("up")
					player2.update(width, height)
				if event.key == pygame.K_RIGHT:
					#print "[DEBUG] right arrow pressed"
					player2.go("right")
					player2.update(width, height)
				if event.key == pygame.K_DOWN:
					#print "[DEBUG] down arrow pressed"
					player2.go("down")
					player2.update(width, height)
				if event.key == pygame.K_LEFT:
					#print "[DEBUG] left arrow pressed"
					player2.go("left")
					player2.update(width, height)				
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					player1.go("stop up")
				if event.key == pygame.K_d:
					player1.go("stop right")
				if event.key == pygame.K_s:
					player1.go("stop down")
				if event.key == pygame.K_a:
					player1.go("stop left")
				if event.key == pygame.K_UP:
					player2.go("stop up")
				if event.key == pygame.K_RIGHT:
					player2.go("stop right")
				if event.key == pygame.K_DOWN:
					player2.go("stop down")
				if event.key == pygame.K_LEFT:
					player2.go("stop left")
										
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(player1.image, player1.rect)
		screen.blit(player2.image, player2.rect)
		pygame.display.flip()
		
