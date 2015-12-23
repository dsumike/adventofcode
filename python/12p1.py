#!/usr/bin/env python
import re

# Part 1
# ignore that this is JSON, look for all ints and add them together

with open('../input/12.txt') as fileobj:
	json = fileobj.readline()

total = sum([int(x) for x in re.findall(r'-?[0-9]+', json)])

print total
