#!/usr/bin/env python

floor=0
count=0

with open("01.txt") as fileobj:
	for word in fileobj:  
		for ch in word: 
			count+=1
			if ch == '(':
				floor+=1
			if ch == ')':
				floor-=1
			if floor<0:
				break
	print count
	print floor
