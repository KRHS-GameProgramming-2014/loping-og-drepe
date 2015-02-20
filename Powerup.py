import pygame

class Powerup():
    def __init__(self, kind, pos = [0,0]):
        self.kind = kind
        if self.kind == "SPU":
            self.image = pygame.image.load("Art/SPDPower.png")
        self.rect = self.image.get_rect()
        self.place(pos)
        self.living = True
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.timeMax = 5*60
        self.time = 0


    def place(self, pos):
        self.rect.center = pos

    def collidePlayer(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.living = False
                        return True
        return False
        
    def update(self):
        if self.time < self.timeMax:
            self.time += 1
        else:
            self.living = False
    
    def distance (self, other):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        


