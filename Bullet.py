
import pygame

class Bullet():
    def __init__(self, pos, speed, heading):
        self.image = pygame.image.load("Art/Lazor.png")
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedy = 0
        self.place(pos)
        self.didBounceX = False
        self.didBounceY = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.living = True
        if heading == "up":
            self.speedy = -speed
        if heading == "down":
            self.speedy = speed
        if heading == "right":
            self.speedx = speed
        if heading == "left":
            self.speedx = -speed
        self.speed = [self.speedx, self.speedy]

    def place(self, pos):
        self.rect.center = pos
        
    def update(self, width, height):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideWall(width, height)
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        

    def collideZombie(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False
    
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.living = False
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.living = False
                
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))