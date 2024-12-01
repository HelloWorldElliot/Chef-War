#Phuong Nguyen Ngoc, Elliot Zhou, Zixuan Wang, Eduardo Sosa, Katie Andre, Izzy Hurley
#CS269
from .common_setting import *
import pygame as pg
import random



class Block(pg.sprite.Sprite):
	def __init__(self, x, y, health, indestructable = False, bonus = 0 ):
		pg.sprite.Sprite.__init__(self)
		self.image = self.image = pg.image.load(blocks[random.randint(0,6)]).convert()
		self.indestructable = indestructable
		if self.indestructable == True:
			self.image = self.image = pg.image.load(f"{IMAGE_PATH}permanent_block.png").convert()
		self.rect = self.image.get_rect()
		self.image.set_colorkey(BLACK)
		self.rect.center = (120+40*x,220+40*y)
		
		self.x = x
		self.y = y

		if self.indestructable:
			self.health = 100
		else:
			self.health = health
		self.bonus=	bonus
		
		
	def get_rect(self):
		return self.rect
		
	def get_rect_center(self):
		return self.rect.center
	def set_rect_center(self, x,y):
		self.rect.center = (x,y)

	def get_x(self):
		return self.x
        
	def get_y(self):
		return self.y

	def getHealth(self):
		return self.health
	def setHealth(self, v):
		self.health = v
	
	def getBonus(self):
		return self.bonus
	
	def decrementHealth(self, hit =1):
		self.health -= hit
		self.sound = pg.mixer.Sound(f"{SOUND_PATH}blockcrack.wav")
		if self.bonus != 0:
			self.sound = pg.mixer.Sound(f"{SOUND_PATH}powerupblock.wav")
		#dont play sound for indestructable blocks
		if self.health < 50:
			self.sound.play()
		else:
			self.sound = pg.mixer.Sound(f"{SOUND_PATH}perm.wav")
			self.sound.play()
        
	def update(self):
		self.sound = None
		if self.health == 0:
			if self.bonus==0:
				self.kill()
			if self.bonus==1:
				self.image = pg.image.load(f"{IMAGE_PATH}life.png").convert()#life
				self.image.set_colorkey(BLACK)
			if self.bonus==2:
				self.image = pg.image.load(f"{IMAGE_PATH}bullet-bonus.png").convert() #cabbage
				self.image.set_colorkey(BLACK)
			if self.bonus==3:
				self.image = pg.image.load(f"{IMAGE_PATH}recipe.png").convert()#ingredient
				self.image.set_colorkey(BLACK)
			if self.bonus ==4:   
				self.image = pg.image.load(f"{IMAGE_PATH}boot-collect.png").convert()#speed boost
				self.image.set_colorkey(BLACK)
			if self.bonus == 5:
				self.image = pg.image.load(f"{IMAGE_PATH}superbullet.png").convert()#super bullet
				self.image.set_colorkey(BLACK)
			if self.bonus == 6:
				self.image = pg.image.load(f"{IMAGE_PATH}light.png").convert()#light up
				self.image.set_colorkey(BLACK)
	
	def change_to_bonus_graphics(self):
		if self.bonus==1:
			self.image = pg.image.load(f"{IMAGE_PATH}life.png").convert()#life
			self.image.set_colorkey(BLACK)
		if self.bonus==2:
			self.image = pg.image.load(f"{IMAGE_PATH}bullet-bonus.png").convert() #cabbage
			self.image.set_colorkey(BLACK)
		if self.bonus==3:
			self.image = pg.image.load(f"{IMAGE_PATH}recipe.png").convert()#ingredient
			self.image.set_colorkey(BLACK)
		if self.bonus ==4:   
			self.image = pg.image.load(f"{IMAGE_PATH}boot-collect.png").convert()#speed boost
			self.image.set_colorkey(BLACK)
		if self.bonus == 5:
			self.image = pg.image.load(f"{IMAGE_PATH}superbullet.png").convert()#super bullet
			self.image.set_colorkey(BLACK)
		if self.bonus == 6:
			self.image = pg.image.load(f"{IMAGE_PATH}light.png").convert()#light up
			self.image.set_colorkey(BLACK)
		
