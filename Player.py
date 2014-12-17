import pygame
class Player():
	def __init__(self, playernum):
		self.playernumber = playernum
		if playernum == 1:
			self.images = []
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
		self.changed = False
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 20
		self.normalMaxSpeed = 20
		self.fasterMaxSpeed = 30
		self.maxSPUtime = 10*60
		self.spuTime = 0

	def go(self, direction):
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
		#timers
		if self.spuTime != 0:
			if self.spuTime < self.maxSPUtime:
				self.spuTimer += 1
			else:
				self.spuTime = 0
				self.maxSpeed = self.normalMaxSpeed
		
		
		self.didBounceX = False
		self.didBounceY = False
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)

	def move(self):
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
	
	def collidePlayer(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.health = self.health-1
		
	def collidePowerUp(self, pu):
		if self.rect.right > pu.rect.left and self.rect.left < pu.rect.right:
			if self.rect.bottom > pu.rect.top and self.rect.top < pu.rect.bottom:
				if (self.radius + pu.radius) > self.distance(pu.rect.center):
					if pu.kind == "SPU":
						self.maxSpeed = self.fasterMaxSpeed
						self.spuTimer = 1
						
