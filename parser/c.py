#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re

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

	if command['a']:
		file.seek(0)
		blankLine, codeLine, commentLine = 0, 0, 0
		line = file.readline()
		while line != '':
			matchResult = re.search(r'//\S+', line)
			if matchResult:
				# 包含注释
				matchResult = re.compile(r'\S').findall(line.replace(matchResult.group(), ''))
				if (len(matchResult) > 1):
					codeLine = codeLine + 1
				else:
					commentLine = commentLine + 1
			else:
				matchResult = re.compile(r'\S').findall(line)
				if (len(matchResult) > 1):
					codeLine = codeLine + 1
				else:
					blankLine = blankLine + 1
			line = file.readline()
			

	# 输出文件统计信息
	print('[', file.name.replace(os.path.abspath(os.path.curdir), ''), ']')
	print('------')
	if command['c']:
		print('字符数:', chars)
	if command['w']:
		print('单词数:', words)
	if command['l']:
		print('行数:', lines)
	if command['a']:
		if command['c'] or command['w'] or command['l']:
			print('------')
		print('代码行数:', codeLine)
		print('注释行数:', commentLine)
		print('空行数:', blankLine)
	print('')

	file.close()