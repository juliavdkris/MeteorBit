import microbit
from time import sleep
from random import randint
# from . import classes  # Relative imports don't work (TODO: workaround?)


# Global variables
level = 1
meteors = []


class Movable:
	x = None
	y = None
	outside = False
	brightness = 9

	def move(self, oldx, oldy, x, y):
		self.x = x
		self.y = y
		microbit.display.set_pixel(oldx, oldy, 0)
		microbit.display.set_pixel(x, y, self.brightness)

	def move_relative(self, x, y):
		microbit.display.set_pixel(self.x, self.y, 0)
		if valid_coords(self.x + x, self.y + y):
			self.move(self.x, self.y, self.x + x, self.y + y)
		else:
			self.outside = True

	def render(self):
		microbit.display.set_pixel(self.x, self.y, self.brightness)


class Meteor(Movable):
	def __init__(self):
		self.x = randint(0, 4)
		self.y = 0
		self.brightness = 4
		self.render()


class Player(Movable):
	def __init__(self):
		self.x = 2
		self.y = 3
		self.alive = True


def valid_coords(x, y):  # Check if coords are on screen
	return 0 <= x <= 4 and 0 <= y <= 4  # Chained comparison fuckery


# Object loops (TODO: clean up and move to object or main loop)
def meteor_loop():
	for meteor in meteors:
		if not meteor.outside:
			meteor.move_relative(0, 1)
		else:
			meteor.move(meteor.x, meteor.y, randint(0, 4), 0)
			meteor.outside = False
	if len(meteors) < level:
		meteors.append(Meteor())


# Main loop
while True:
	meteor_loop()
	sleep(1)