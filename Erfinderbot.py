#!/usr/bin/python
# -*- coding: utf-8 -*-


__all__ = ['Erfinderbot']

class Erfinderbot(Robot):
	"""A `gpiozero.Robot` preconfigured for use with the erfindergarden
	pi-robo-board (https://github.com/erfindergarden/pi-robo-board)

	Usage: ```
		from Erfinderbot import Erfinderbot
		my_robot = Erfinderbot()
		my_robot.forward()
	```

	Official documentation for gpiozero:
	https://gpiozero.readthedocs.io/en/v1.3.1/api_boards.html#robot
	"""
	def __init__(self):
		Robot.__init__(self, left=(15, 14), right=(7, 8))

