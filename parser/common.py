#!/usr/bin/python
# -*- coding: UTF-8 -*-

def parse(file, command):
	chars, words, lines = 0, 0, 0
	if command['l'] and not command['c'] and not command['w']:
		line = file.next()
		while line != '':
			lines = lines + 1
			line = file.next()
	else:
		char = file.read(1)
		lastChar = ''
		while char != '':
			if (char == ' '):
				if lastChar != ' ' and lastChar != '':
					words = words + 1
			elif (char == '\n'):
				if lastChar != ' ':
					words = words + 1
				lines = lines + 1
			chars = chars + 1
			lastChar = char
			char = file.read(1)
		if lastChar != ' ':
			words = words + 1
			lines = lines + 1

	if command['c']:
		print('字符数：\t', chars)
	if command['w']:
		print('单词数：\t', words)
	if command['l']:
		print('行数：\t', lines)
	
	file.close()