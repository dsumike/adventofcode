#!/usr/bin/env python

sx=0
sy=0
rx=0
ry=0

total = 2

houses = set()
houses.add( (0,0) ) # starting point

with open("../input/03.txt") as fileobj:
	for word in fileobj:  
		for ch in word:
			total+=1
			if total % 2 == 0:	# santa
				if ch == '^':
					sx+=1
				if ch == 'v':
					sx-=1
				if ch == '<':
					sy-=1
				if ch == '>':
					sy+=1
				houses.add( (sx,sy) )
			else:				# robo-santa
				if ch == '^':
					rx+=1
				if ch == 'v':
					rx-=1
				if ch == '<':
					ry-=1
				if ch == '>':
					ry+=1
				houses.add( (rx,ry) )

	print "total presents: %s" % total
	print "total houses visited: %s" % len(houses)

