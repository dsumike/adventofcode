#!/usr/bin/env python
import re

iterations = 40

with open("../input/10.txt") as fileobj:
	puzzle = fileobj.readline().strip()

print puzzle

for x in range(40):
	newpuzzle = ''
	for y in re.finditer(r"([0-9])\1*", puzzle):
		newpuzzle += str(len(y.group(0)))+y.group(0)[0]
	puzzle = newpuzzle

print len(puzzle)
