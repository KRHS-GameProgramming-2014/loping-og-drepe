import pygame, sys, random
from Player import Player
from Button import Button
from Powerup import Powerup
from health import HealthBar

#Test 3

pygame.init()

# constant variables for static values
BULLET_DAMAGE = 13
POWERUP_BOOST = .25


clock = pygame.time.Clock()

width = 1000
height = 715
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)
bgImage = pygame.image.load("TitleAS.png").convert()
bgImage = pygame.transform.scale(bgImage, [1000,715])
bgRect = bgImage.get_rect()
player1win = pygame.image.load("Art/Background/WinP1.png")
player2win = pygame.image.load("Art/Background/WinP2.png")

player1 = Player(1, "Art/Player/P1.png", 3, [0,0], [50,357])
player2 = Player(1, "Art/Player/P2.png", 3, [0,0], [950,357])
powerups = []


p1Bullets = []
p2Bullets = []

healthbar1 = HealthBar([width - 955, 700])
healthbar2 = HealthBar([width - 4.05, 700])

run = False

startButton = Button([width/2, height-100], 
                     "Art/Button/Start_Base.png", 
                     "Art/Button/Start_Clicked.png")
                     
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
         
         
        bgImage = pygame.image.load("TitleAS.png").convert()
        bgImage = pygame.transform.scale(bgImage, [1000,715])
        bgRect = bgImage.get_rect()
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        #screen.blit(healthbar1.surface, healthbar1.rect)
        
    bgImage = pygame.image.load("Art/Background/BL1.png").convert()
    bgRect = bgImage.get_rect()
    player1 = Player(1, "Art/Player/P1.png", 3, [0,0], [950,357])
    player2 = Player(1, "Art/Player/P2.png", 3, [0,0], [50,357])
    
    

    p1Bullets = []
    p2Bullets = []

    healthbar1 = HealthBar([width - 45, 700])

    healthbar2 = HealthBar([width - 955, 700])

    while run and player1.lives > 0 and player2.lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    #print "[DEBUG] w button pressed"
                    player2.go("up")
                if event.key == pygame.K_d:
                    #print "[DEBUG] d button pressed"
                    player2.go("right")
                if event.key == pygame.K_s:
                    #print "[DEBUG] s button pressed"
                    player2.go("down")
                if event.key == pygame.K_a:
                    #print "[DEBUG] a button pressed"
                    player2.go("left")
                if event.key == pygame.K_SPACE:
                    #print "[DEBUG] a button pressed"
                    p2Bullets += player2.shoot()
                if event.key == pygame.K_UP:
                    #print "[DEBUG] up arrow pressed"
                    player1.go("up")
                if event.key == pygame.K_RIGHT:
                    #print "[DEBUG] right arrow pressed"
                    player1.go("right")
                if event.key == pygame.K_DOWN:
                    #print "[DEBUG] down arrow pressed"
                    player1.go("down")
                if event.key == pygame.K_LEFT:
                    #print "[DEBUG] left arrow pressed"
                    player1.go("left")         
                if event.key == pygame.K_KP0: # <---- DOESN'T WORK ON A KEYBOARD WITH NO KEYPAD (LIKE MOST LAPTOPS!!!)
                    #print "[DEBUG] a button pressed"
                    p1Bullets += player1.shoot()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player2.go("stop up")
                if event.key == pygame.K_d:
                    player2.go("stop right")
                if event.key == pygame.K_s:
                    player2.go("stop down")
                if event.key == pygame.K_a:
                    player2.go("stop left")
                if event.key == pygame.K_UP:
                    player1.go("stop up")
                if event.key == pygame.K_RIGHT:
                    player1.go("stop right")
                if event.key == pygame.K_DOWN:
                    player1.go("stop down")
                if event.key == pygame.K_LEFT:
                    player1.go("stop left")
        
        if len(powerups) < 2:
            if random.randint(0, 100) == 0:
                powerups += [Powerup("SPU",
                                [random.randint(50, width-50),random.randint(50,height-50)])]
        
        for powerup in powerups:
            powerup.update()
        for bullet in p2Bullets:
            bullet.update(width, height)
        for bullet in p1Bullets:
            bullet.update(width, height)
            
        player1.update(width, height)
        player2.update(width, height)
        healthbar1.update(player1.health, player1.maxHealth)
        healthbar2.update(player2.health, player2.maxHealth)
        
                    
        for bullet in p1Bullets:
            if bullet.collidePlayer(player2):
                player2.modifyHealth(BULLET_DAMAGE)

        for bullet in p2Bullets:
            if bullet.collidePlayer(player1):
                player1.modifyHealth(BULLET_DAMAGE)
                
        for powerup in powerups:
            powerup.collidePlayer(player1)
            powerup.collidePlayer(player2)
            player1.collidePowerup(powerup)
            player2.collidePowerup(powerup)
    
        for bullet in p2Bullets:
            if not bullet.living:
                p2Bullets.remove(bullet)
        for bullet in p1Bullets:
            if not bullet.living:
                p1Bullets.remove(bullet)
        for powerup in powerups:
            if not powerup.living:
                powerups.remove(powerup)
        
        if not player1.living:
            player1 = Player(1, "Art/Player/P1.png",player1.lives - 1, [0,0], [950,357])
        if not player2.living:
            player2 = Player(1, "Art/Player/P2.png",player2.lives - 1, [0,0], [50,357])
        print len(p1Bullets), len(p2Bullets)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        if player1.living == True and player2.living == True:
            screen.blit(bgImage, bgRect)

        if player1.living == True:
            screen.blit(player1.image, player1.rect)
            screen.blit(healthbar1.surface, healthbar1.rect)
        if player2.living == True:
            screen.blit(player2.image, player2.rect)
            screen.blit(healthbar2.surface, healthbar2.rect)
        
        for powerup in powerups:
            screen.blit(powerup.image, powerup.rect)
        for bullet in p1Bullets:
            screen.blit(bullet.image, bullet.rect)
        for bullet in p2Bullets:
            screen.blit(bullet.image, bullet.rect)
 
        player1win = pygame.image.load("Art/Background/WinP1.png")
        player2win = pygame.image.load("Art/Background/WinP2.png")       
        
        pygame.display.flip()
        clock.tick(60)

    while run and player1.lives == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = False
         
         
        bgImage = pygame.image.load("Art/Background/WinP1.png").convert()
        bgImage = pygame.transform.scale(bgImage, [1000,715])
        bgRect = bgImage.get_rect()
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        #screen.blit(healthbar1.surface, healthbar1.rect)
        
    while run and player2.lives == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = False
         
         
        bgImage = pygame.image.load("Art/Background/WinP2.png").convert()
        bgImage = pygame.transform.scale(bgImage, [1000,715])
        bgRect = bgImage.get_rect()
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        #screen.blit(healthbar1.surface, healthbar1.rect)
