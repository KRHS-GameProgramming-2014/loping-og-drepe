import pygame, sys
from Player import *


pygame.init()

clock = pygame.time.Clock

width = 100
height = 800
size = width, height



screen = pygame.display.set_mode(size)

player1 = [Player(1, "ball.png")]


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player1.go("up")
			if event.key == pygame.K_RIGHT:
				player1.go("right")
			if event.key == pygame.K_DOWN:
				player1.go("down")
			if event.key == pygame.K_LEFT:
				player1.go("left")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player1.go("stop up")
			if event.key == pygame.K_RIGHT:
				player1.go("stop right")
			if event.key == pygame.K_DOWN:
				player1.go("stop down")
			if event.key == pygame.K_LEFT:
				player1.go("stop left")



	if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player2.go("up")
			if event.key == pygame.K_d:
				player2.go("right")
			if event.key == pygame.K_s:
				player2.go("down")
			if event.key == pygame.K_a:
				player2.go("left")
	if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player2.go("stop up")
			if event.key == pygame.K_d:
				player2.go("stop right")
			if event.key == pygame.K_s:
				player2.go("stop down")
			if event.key == pygame.K_a:
				player2.go("stop left")
		
	


	
	bgColor = pygame.image.load("BL1.png")

pygame.init()

clock = pygame.time.Clock

width = 100
height = 800
size = width, height



screen = pygame.display.set_mode(size)

player1 = [Player(1, "ball.png")]


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player1.go("up")
			if event.key == pygame.K_RIGHT:
				player1.go("right")
			if event.key == pygame.K_DOWN:
				player1.go("down")
			if event.key == pygame.K_LEFT:
				player1.go("left")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player1.go("stop up")
			if event.key == pygame.K_RIGHT:
				player1.go("stop right")
			if event.key == pygame.K_DOWN:
				player1.go("stop down")
			if event.key == pygame.K_LEFT:
				player1.go("stop left")



	if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player2.go("up")
			if event.key == pygame.K_d:
				player2.go("right")
			if event.key == pygame.K_s:
				player2.go("down")
			if event.key == pygame.K_a:
				player2.go("left")
	if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player2.go("stop up")
			if event.key == pygame.K_d:
				player2.go("stop right")
			if event.key == pygame.K_s:
				player2.go("stop down")
			if event.key == pygame.K_a:
				player2.go("stop left")
		
	


	
	bgColor = pygame.image.load("BL1.png")
	screen.fill(bgColor)
	pygame.display.flip()
	clock.tick(60)
