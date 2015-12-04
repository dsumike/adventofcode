#!/usr/bin/env python

import md5

i = 1

with open("../input/04.txt") as fileobj:
	for word in fileobj:  
		while True:
			if md5.new("{}{}".format(word.rstrip(),i)).hexdigest()[:6] == '000000':
				print word,i
				break
			i+=1

