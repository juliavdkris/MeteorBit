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

	def move_relative(self, x, y):
		microbit.display.set_pixel(self.x, self.y, 0)
		if valid_coords(self.x + x, self.y + y):
			self.x += x
			self.y += y
			microbit.display.set_pixel(self.x, self.y, 9)

	def render(self):
		microbit.display.set_pixel(self.x, self.y, 9)


class Meteor(Movable):
	def __init__(self):
		self.x = randint(0, 4)
		self.y = 0

	def __del__(self):
		meteors.remove(self)


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
		if meteor.y == 4:
			del meteor
		meteor.y += 1  # Some kind of error happens here, Bram pls halp
	for i in range(0, level):
		meteors.append(Meteor())
	for meteor in meteors:
		meteor.move_relative(0, 1)


# Main loop
while True:
	meteor_loop()
	sleep(1)