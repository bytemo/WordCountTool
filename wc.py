#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys, getopt, importlib, glob, tkinter, tkinter.filedialog

window, button, titleLabel = None, None, None
command = {'c': False, 'w': False, 'l': False, 'a': False, 's': False, 'x': False}

# 解析命令行参数
def parseParameter(argv):
	global command
	
	try:
		opts, args = getopt.gnu_getopt(argv,"cwlhsax",["help"])
	except getopt.GetoptError:
		printError('参数错误！', True)
	# print(opts, args)
	# 控制参数是否提供
	if len(opts) == 0:
		printError('未提供控制参数！', True)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			printUsage(0)
		else:
			command[opt.replace('-', '')] = True

	if command['x']:
		startGUI()

	# 文件名是否提供
	if len(args) == 0:
		printError('未提供目标文件名！', True)

	fileList = args

	# 处理目标文件
	if command['s']:
		# 处理通配符
		fileList = []
		parserDir(fileList, os.path.abspath(os.path.curdir), args)
				

	# 调用对应的解析模块
	for file in fileList:
		fileType = file.split('.')
		if (len(fileType) == 1):
			# 可能是目录或者文件
			if (os.path.isfile(os.path.abspath(file))):
				# 处理文件
				if os.path.exists(file):
					tempFile = open(file)
					# 热加载文件格式对应的解析器
					parser = importlib.import_module('parser.common')
					parser.parse(tempFile, command)
				else:
					printError('文件不存在！')
		else:
			# 只能是文件
			if os.path.exists(file):
				if not os.path.exists(os.path.join(os.path.abspath(os.path.curdir), './parser/' + fileType[len(fileType) - 1] + '.py')):
					printError('暂不支持此文件格式的解析.')
				tempFile = open(file)
				# 热加载文件格式对应的解析器
				parser = importlib.import_module(fileType[len(fileType) - 1], 'parser')
				print(parser.parse(tempFile, command))
			else:
				printError('文件不存在！')

# 遍历目录内的文件
def parserDir(fileList, sourceDir, fileFormat):
	# 先将当前目录符合条件的加入文件
	for file in fileFormat:
		fileList.extend(glob.glob(os.path.join(sourceDir, file)))
	# 递归深入子目录
	for subDir in os.listdir(sourceDir):
		if os.path.isdir(os.path.join(sourceDir, subDir)):
			parserDir(fileList, os.path.join(sourceDir, subDir), fileFormat)


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

# 按钮的点击事件
def onButtonTap():
	global window, titleLabel, button
	file = tkinter.filedialog.askopenfilename()
	if file != '':
		window.geometry('300x200')
		button.destroy()
		titleLabel.destroy()
		fileType = file.split('.')
		if os.path.exists(file):
			if not os.path.exists(os.path.join(os.path.abspath(os.path.curdir), './parser/' + fileType[len(fileType) - 1] + '.py')):
				printError('暂不支持此文件格式的解析.')
			tempFile = open(file)
			# 热加载文件格式对应的解析器
			parser = importlib.import_module(fileType[len(fileType) - 1], 'parser')
			command = {'c': True, 'w': True, 'l': True, 'a': True}
			textLabel = tkinter.Label(window, text=parser.parse(tempFile, command), font=('', 14))
			textLabel.pack()
		else:
			printError('文件不存在！')

# 创建界面
def startGUI():
	global window, titleLabel, button
	window = tkinter.Tk()
	window.title('WordCount GUI Window')
	window.geometry('250x110')
	titleLabel = tkinter.Label(window, text='点击下方按钮选择文件：', font=('',14), height=2)
	titleLabel.pack()
	button = tkinter.Button(window, text="选择文件", font=('', 14), width=10, height=2, command=onButtonTap)
	button.pack()
	window.mainloop()
	sys.exit(0)

# 测试
def test(param):
	parseParameter(param.split(' '))

if __name__ == "__main__":
	parseParameter(sys.argv[1:])