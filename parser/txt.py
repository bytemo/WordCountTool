#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

def parse(file, command):
	chars, words, lines = 0, 0, 0
	if command['l'] and not command['c'] and not command['w']:
		line = file.readline()
		while line != '':
			lines = lines + 1
			line = file.readline()
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

	# 输出文件统计信息
	print('[', file.name.replace(os.path.abspath(os.path.curdir), ''), ']')
	print('------')
	if command['c']:
		print('字符数:', chars)
	if command['w']:
		print('单词数:', words)
	if command['l']:
		print('行数:', lines)
	print('')

	file.close()