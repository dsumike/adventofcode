#!/usr/bin/env python

command = dict()
results = dict()

with open("../input/07.txt") as fileobj:
	for line in fileobj:
		# split the command into operations and result
		ops, res = line.split('->')
		command[res.strip()] = ops.strip().split(' ')

def get_value(key):

	# check if we have an integer result
	try:
		return int(key)
	except ValueError:
		pass

	# guess we're not done yet

	if key not in results:
		value = command[key]
		# if we just have the one thing, do that
		if len(value) == 1:
			result = get_value(value[0])
		# else calculate the operation
		else:
			op = value[-2]	# get the operation to be done
			if op == 'AND':
				result = get_value(value[0]) & get_value(value[2])
			if op == 'OR':
				result = get_value(value[0]) | get_value(value[2])
			if op == 'NOT':
				result = ~get_value(value[1])
			if op == 'RSHIFT':
				result = get_value(value[0]) >> get_value(value[2])
			if op == 'LSHIFT':
				result = get_value(value[0]) << get_value(value[2])

		results[key] = result
	return results[key]

print "a: %d" % get_value('a')

