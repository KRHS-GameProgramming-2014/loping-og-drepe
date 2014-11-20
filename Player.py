import pygame

class Player:
	def __init__(image, speed=[0,0], pos=[0,0])
		player1.__init__(self, "Art/Player1Art.png", [0,0], pos)
		player2.__init__(self, "Art/Player2Art.png", [0,0], pos)
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
		

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


