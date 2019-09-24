#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys, getopt, importlib, glob

# 解析命令行参数
def parseParameter(argv):
	command = {'c': False, 'w': False, 'l': False, 'a': False, 's': False, 'x': False}
	
	try:
		opts, args = getopt.gnu_getopt(argv,"cwlh",["help"])
	except getopt.GetoptError:
		printError('参数错误！', True)
	# print(opts, args)
	# 控制参数是否提供
	if len(opts) == 0:
		printError('未提供控制参数！', True)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			printUsage(0)
		elif opt in ('-c', '-w', '-l'):
			command[opt.replace('-', '')] = True
	# 文件名是否提供
	if len(args) == 0:
		printError('未提供目标文件名！', True)

	# print(command)

	# 处理通配符
	fileList = []
	for filePath in args:
		fileList.extend(glob.glob(filePath))

	# 调用对应的解析模块
	for file in fileList:
		fileType = file.split('.')
		if (len(fileType) == 1):
			# 可能是目录或者文件
			if (os.path.isfile(file)):
				# 处理文件
				if os.path.exists(file):
					tempFile = open(file)
					# 热加载文件格式对应的解析器
					parser = importlib.import_module('parser.common')
					parser.parse(tempFile, command)
				else:
					printError('文件不存在！')
			else:
				if command['s']:
					# 处理目录
					print()
		else:
			# 只能是文件
			if os.path.exists(file):
				tempFile = open(file)
				parser = importlib.import_module('parser.' + fileType[len(fileType) - 1])
				parser.parse(tempFile, command)
			else:
				printError('文件不存在！')

# 输出错误信息
def printError(msg, isPrintUsage = False):
	print(msg)
	if isPrintUsage:
		printUsage(1)
	else:
		sys.exit(1)

# 打印程序的用法
def printUsage(signal):
	print('usage: python3 wc.py [parameter] [file_name] ...\n')
	print('Options and arguments:')
	print('-c:\t返回文件 file_name 的字符数')
	print('-w:\t返回文件 file_name 的词的数目')
	print('-l:\t返回文件 file_name 的行数')
	sys.exit(signal)

# 测试
def test(param):
	parseParameter(param.split(' '))

if __name__ == "__main__":
	parseParameter(sys.argv[1:])