#!/usr/bin/env python
import itertools as itertools

distances = dict()
places = set()
paths = set()

with open("../input/09.txt") as fileobj:
	for line in fileobj:
		lhs, rhs = line.strip().split(' = ')
		distance = int(rhs)
		start, end = lhs.split(' to ')
		places.add(start)
		places.add(end)
		distances[(start, end)] = distances[(end, start)] = distance

for cities in itertools.permutations(places):
	distance = 0
	for i in range(len(cities)-1):
		distance += distances[cities[i],cities[i+1]]
	paths.add(distance)

print min(paths)
