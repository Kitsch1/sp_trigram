#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
	line = sys.stdin.readline().strip()
	
	if line == "":
		break
	words = line.split()
	length = len(words)
	for i in range(0,length+1):
		if i == 0:
			sys.stdout.write('<s>'+' '+words[i]+'\n')
		elif i == length:
			sys.stdout.write(words[i-1]+' '+'</s>'+'\n')
		else:
			sys.stdout.write(words[i-1]+' '+words[i]+'\n')
