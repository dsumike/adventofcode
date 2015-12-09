#!/usr/bin/env python

import md5

nice = 0

with open("../input/05.txt") as fileobj:
	for line in fileobj:
		for x in range(0, len(line)-2):
			if line[x] == line[x+2]:
				break
		else:
			continue

		for x in range(0, len(line)-1):
			if line.count(line[x] + line[x+1]) > 1:
				nice += 1
				break
		else:
			continue
print nice
