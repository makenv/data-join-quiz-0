#!/usr/bin/python

import random

random.seed()

for i in range(1, 6):
	for j in range(1, 5):
		print "%d,%d,%d" % (i, j, random.randint(40,100))
