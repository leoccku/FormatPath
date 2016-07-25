#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def formatPath(arg):
	arg = arg[1:].split('/')
	print arg
        if len(arg) == 1 and len(arg[0]) != 1 : return arg[0]
        path = arg[0].upper() + ':/' + '/'.join(arg[1:])
	return path

arg = '/C/C1/C2/C3'

arg = formatPath(arg)

print arg

print "End TEST !"
