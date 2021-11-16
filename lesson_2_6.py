# import random
#
# class Monty:
# 	def __init__(self, choices):
# 		self.choices = choices
#
# 	def choose_door(self):
# 		judge = random.choice(self.choices)

import random

num = 50
win = 0

for i in range(1, num):
	if random.randint(1,3) == random.randint(1,3):
		win +=1
print("Я не менял выбора и выиграл:", win, "игр")
print("Я менял выбор и выиграл:", num-win, "игр")