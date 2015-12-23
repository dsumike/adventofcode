#!/usr/bin/env python
import re
import json

# Part 2
# Aww man, have to actually read the JSON :/

def get_sum(j):
	if isinstance(j, (str, unicode)):
		return 0
	if isinstance(j, int):
		return j
	elif isinstance(j, list):
		return sum([get_sum(b) for b in j])
	else:
		if 'red' in j.values():
			return 0
		else:
			return get_sum(list(j.values()))

with open('../input/12.txt') as fileobj:
	j = fileobj.readline()

total = get_sum(json.loads(j))

print total
