#!/usr/bin/env python

literal = 0
inmemory = 0

with open("../input/08.txt") as fileobj:
	for line in fileobj:
		line = line.rstrip()
		literal += len(line)
		# remove the outer " "'s, and decode the rest
		inmemory += len(line[1:-1].decode('string_escape'))

print "literal: %d" % literal
print "in mem : %d" % inmemory
print "l-m    : %d" % (literal-inmemory)

