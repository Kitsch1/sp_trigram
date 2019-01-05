#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin,stdout

library = {}

while True:
	line = stdin.readline().strip()
	if line == '':
		break
	
	if line in library:
		library[line] += 1
	else:
		library[line] = 1

ngram_list = list(library.keys())
ngram_list = sorted(ngram_list)

for word in ngram_list:
	stdout.write(word+'\t'+str(library[word])+'\n')
