#! /usr/bin/env python
import urllib.request

wp = urllib.request.urlopen("https://www.baidu.com/")
pw = wp.read()
print(pw)
