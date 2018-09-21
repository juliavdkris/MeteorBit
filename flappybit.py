#---------------------------------------------> Setup

import microbit
from time import sleep
from random import randint
level = 1
meteors = []

#---------------------------------------------> Class definition

class Meteor():
	def __init__(self):
		self.x = randint(0, 4)
		self.y = 0
	def __del__(self):
		meteors.remove(self)

class Player():
	def __init__(self):
		self.x = 2
		self.y = 3
		self.alive = True
		
#---------------------------------------------> Function definition
		
def meteor_loop():
	for meteor in meteors:
		if meteor.y == 4:
			del meteor
		meteor.y = y + 1
	for i in range(0, level):
		meteors.append(meteor())
	microbit.display.clear()
	for meteor in meteors:
		microbit.display.set_pixel(meteor.x, meteor.y, 100)

#---------------------------------------------> Execution of code

while True:
	meteor_loop()
	sleep(1)