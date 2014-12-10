import pygame

class Text():
	def __init__(self, pos, text = "", textSize = 12, textColor=(255,255,255), font = None):
		self.text = text
		self.textColor = textColor
		self.font = pygame.font.Font(font, textSize)
		self.image = self.font.render(self.text, 1, textColor)
		self.rect = self.image.get_rect()
		self.place(pos)
		
	def place(self, pos):
		self.rect.center = pos
		
	def setText(self, text):
		self.text = text
		self.image = self.font.render(text, 1, textColor)
		self.rect = self.image.get_rect(center = self.rect.center)
		
	def update(self, width, height):
		pass

class Score(Text):
	def __init__(self, pos, baseText = "Score: ", textSize = 12, textColor=(255,255,255), font = None):
		self.score = 0
		self.baseText = baseText
		self.text = self.baseText + str(self.score)
		Text.__init__(self, pos, self.text, textSize, textColor, font)
		self.change = False
			
	def setText(self, text):
		self.baseText = text
		self.change = True
		
	def update(self):
		if self.change:
			self.text = self.baseText + str(self.score)
			self.image = self.font.render(self.text, 1, self.textColor)
			self.rect = self.image.get_rect(center = self.rect.center)
			self.change = False
	
	def setScore(self, score):
		self.score = score
		self.change = True
		
	def increaseScore(self, amount = 1):
		self.score += amount
		self.change = True
		
	def resetScore(self):
		self.score = 0
		self.change = True
		
class PlayerInfo(Text):
	def __init__(self, player, screenSize):
		self.player = player
		self.value = self.player.health
		self.playerNum = self.player.playernum
		self.text = "Player " + str(self.playerNum) + " " + str(self.value)
		if self.playerNum == 1:
			pos = [screenSize[0]+25, screenSize[1]-25]
			self.textColor = [0,0,0]
		if self.playerNum == 2:
			pos = [screenSize[0]-25, screenSize[1]-25]
			self.textColor = [255,255,255]
		Text.__init__(self, pos, self.text, 12, textColor, None)
		
	def update(self):
		if self.player.health != self.value:
			self.value = self.player.health
			self.text = "Player " + str(self.playerNum) + " " + str(self.value)
			self.image = self.font.render(self.text, 1, self.textColor)
			self.rect = self.image.get_rect(center = self.rect.center)
		
