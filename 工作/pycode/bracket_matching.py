#!/usr/bin/python3
#coding=utf-8

text = "({[({{abc}})][{1}]})2([]){({[]})}[]"

def bracket_matching(param):
    stack = []
    bracket = {')':'(', '}':'{', ']':'['}
    for char in param:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket.keys():
            if bracket[char] != stack.pop():
                return  False
    return  True

print(bracket_matching(text))