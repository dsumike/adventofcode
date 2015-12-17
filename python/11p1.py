#!/usr/bin/env python
import re

letters = 'abcdefghijklmnopqrstuvwxyz'

with open("../input/11.txt") as fileobj:
	password = fileobj.readline().strip()

#password = 'abcaabaa'
print password

def rules(password):
	rules = [ rule1, rule2, rule3 ]
	if all(rule(password) for rule in rules):
		print "passed"
		return True
	else:
		return False

def rule1(password):
	# Rule 1: in the range of A-Z, must have 3 consecutive letters
	# Check A-X for [abc, bcd, ..., wzy, xyz]
	for i in range(24):
		if letters[i:i+3] in password:
			return True
	# else rule 1 failed
	return False

def rule2(password):
	# Rule 2: No i, o, l
	if 'i' in password or 'o' in password or 'l' in password:
		return False
	return True

def rule3(password):
	# Rule 3: Password must contain at least 2 different, non-overlapping pairs of letters
	# (aa, bb) or even (aa, aa) "aaaa"
	pair = 0
	skipnext = False
	for i in range(len(password) - 1):
		if skipnext:
			skipnext = False
			continue
		if password[i] == password[i + 1]:
			pair += 1
			skipnext = True
	return pair >1

def increment(password):
	if password[-1] == 'z':
		return increment(password[0:-1]) + 'a'
	return password[0:-1] + letters[letters.index(password[-1]) + 1]

#print rules(password)
#password = increment(password)
#print password
#print rules(password)

while True:
	if rules(password):
		print "Success!"
		break
	else:
		password = increment(password)

print password
