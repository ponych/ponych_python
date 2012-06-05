#!/usr/bin/env python
#-*- coding: utf-8 -*-

def print_params(*params):
    print params

print_params(2 ,3,"Hello")

def print_params2(age = 0,*params):
    print age
    print params

print_params2(21,3,"hello")

#print_params2(age=21, cls = 3,"hello")
" 语法错误了 "


def print_params3(**params):
    print params
    return 

print_params3(age=21, cls= 3,word="hello")

content = {"a": 1, "b": 4, "c": 2}

#print_params3(content)
print_params3(**content)