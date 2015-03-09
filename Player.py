import pygame, math
from Bullet import Bullet

class Player():
    def __init__(self, playernum, image, speed = [0,0], pos = [0,0]):
        self.playernumber = playernum
        if playernum == 1:
            self.images = []
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [25,25])
        self.frame = 0
        self.rect = self.image.get_rect()
        self.place(pos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.maxSpeed = 4.5
        self.changed = False
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        #self.maxSpeed = 20
        #self.normalMaxSpeed = 20
        #self.fasterMaxSpeed = 30
        self.maxSPUtime = 10*60
        self.spuTime = 0
        self.didBounceX = False
        self.didBounceY = False
        self.facing = "up"
        self.coolDown = 0
        self.coolDownMax = 5
        self.amount = 3
        self.health = self.amount
        self.living = True
        self.hurt = False
        

    def place(self, pos):
        self.rect.center = pos
        
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
        
    def go(self, direction):
      #  print "[DEBUG] direction in go() is : " + direction
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0

    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        if self.spuTime != 0:
            if self.spuTime < self.maxSPUtime:
                self.spuTimer += 1
                self.spuTime = 0
                self.maxSpeed = self.normalMaxSpeed
        if self.coolDown > 0:
            if self.coolDown < self.coolDownMax:
                self.coolDown += 1
            else:
                self.coolDown = 0
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        #self.animate()
        self.changed = False
        self.hurt
        
    def hurt(self, amount=1):
        self.changed = True
        self.hurting = True
        if not self.invincible:
            self.health -= amount
            self.invincible = True
            self.hurtDelay = self.maxHurtDelay
        
        if self.health <=0:
            self.living = False
    

    def move(self):
        #print self.speed
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
        
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        

    def collidePlayer(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.living = False
						return True
		return False
      
    def shoot(self):
        if self.coolDown == 0:
            self.coolDown += 1
            return [Bullet(self.rect.center, 8, self.facing)]
        else:
            return []                  


