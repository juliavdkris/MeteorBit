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