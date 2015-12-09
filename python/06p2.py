#!/usr/bin/env python

grid = [[0 for _ in xrange(1000)] for _ in xrange(1000)]
total = 0

with open("../input/06.txt") as fileobj:
	for line in fileobj:
		# split from the right, max of 3 splits
		instruction, from_coords, _, dest_coords = line.strip().rsplit(' ', 3)
		from_coords = [int(coord) for coord in from_coords.split(',')]
		dest_coords = [int(coord) for coord in dest_coords.split(',')]

		# set all the lights:  on, off or toggle
		for x in xrange(from_coords[0], dest_coords[0] + 1):
			for y in xrange(from_coords[1], dest_coords[1] + 1):
				if instruction == 'turn on':
					grid[x][y] += 1
				elif instruction == 'turn off':
					# don't go below 0
					if grid[x][y] > 0:
						grid[x][y] -= 1
				elif instruction == 'toggle':
						grid[x][y] += 2

	# count up the lights
	for x in range(0,999):
		for y in range (0,999):
			total+= grid[x][y]

	print total
