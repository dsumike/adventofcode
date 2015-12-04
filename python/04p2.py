#!/usr/bin/env python

import md5

with open("../input/04.txt") as fileobj:
	for word in fileobj:
		i = 1
		base = md5.new(word.rstrip())
		while True:
			m = base.copy()	# according to the interwebs, this is more efficient than .new()
			m.update(str(i))
			if m.hexdigest()[:6] == '000000':
				print word,i
				break
			i+=1

