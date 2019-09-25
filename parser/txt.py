#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

output = ''

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
	printMsg('[', file.name.replace(os.path.abspath(os.path.curdir), ''), ']')
	printMsg('------')
	if command['c']:
		printMsg('字符数:', chars)
	if command['w']:
		printMsg('单词数:', words)
	if command['l']:
		printMsg('行数:', lines)

	file.close()

	return output

# 重写输出方法
def printMsg(*tupleArg):
	global output
	for msg in tupleArg:
		output = output + str(msg)
	output = output  + '\n'