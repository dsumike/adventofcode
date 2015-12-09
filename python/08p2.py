#!/usr/bin/env python

literal = 0
inmemory = 0

with open("../input/08.txt") as fileobj:
	for line in fileobj:
		line = line.rstrip()
		# build my own string encoding
		# this is a pretty terrible hack job
		newline = "\""
		for ch in line:
			if ch == '"':
				newline+="\\\""
			elif ch == '\\':
				newline+="\\\\"
			else:
				newline+=ch
		newline += "\""
		literal += len(line)
		inmemory += len(newline)

print "old : %d" % literal
print "new : %d" % inmemory
print "new-old  : %d" % (inmemory-literal)

