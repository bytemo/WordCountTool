#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wc

# 测试基本功能
print('开始测试基本功能：')
wc.test('-c -w -l testFiles/test.java')

# 测试扩展功能
print('开始测试扩展功能：')
wc.test('-a -s *.c')

# 测试高级功能
print('开始测试高级功能：')
wc.test('-x')