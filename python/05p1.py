#!/usr/bin/env python

import md5

nice = 0

with open("../input/05.txt") as fileobj:
	for line in fileobj:
		if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
			continue
		if (line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')) < 3:
			continue
		for x in range(0, len(line)-1):
			if line[x] == line[x+1]:
				nice += 1
				break
print nice
