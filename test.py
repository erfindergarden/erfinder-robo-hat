from Erfinderbot import Erfinderbot
from time import sleep

my_robot = Erfinderbot()


while True:
	my_robot.forward()
	sleep(5)
	my_robot.stop()
