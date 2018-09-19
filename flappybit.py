import os
from time import sleep

screen = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
]

def tick(time):
	sleep(time)
	os.system('cls')


def render(screen):  # TODO: Update this when we actually get a MicroBit
	for y in screen:
		for x in y:
			print(x, end=' ', flush=True)
		print()


os.system('cls')
while True:  # Main game loop
	render(screen)

	tick(1)