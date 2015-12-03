#!/usr/bin/env python

x=0
y=0

total = 1

houses = set()
houses.add( (x,y) )

with open("../input/03.txt") as fileobj:
	for word in fileobj:  
		for ch in word: 
			total+=1
			if ch == '^':
				x+=1
			if ch == 'v':
				x-=1
			if ch == '<':
				y-=1
			if ch == '>':
				y+=1
			houses.add( (x,y) )

	#print total
	#print houses
	print len(houses)
