#!/usr/bin/env python

total = 0

for line in open('../input/02.txt'):
	l, w, h = line.split('x')
	l, w, h = int(l), int(w), int(h)
	ribbon = 2 * min(l+w, w+h, h+l)
	bow = l*w*h
	total += ribbon + bow
print total
