# -*- coding: utf-8 -*-
# @Author: Zeyuan Shang
# @Date:   2016-05-04 13:32:40
# @Last Modified by:   Zeyuan Shang
# @Last Modified time: 2016-05-04 13:37:56
import re

T = int(input(""))
in_css = False
for _ in range(T):
	s = input()
	if '{' in s:
		in_css = True
	elif '}' in s:
		in_css = False
	elif in_css:
		for color in re.findall('#[0-9a-fA-F]{3,6}', s):
			print color
