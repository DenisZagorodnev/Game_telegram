#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:05:39 2020

@author: deniszagorodnev
"""






def solver(arg):
    
    stack = []
    
    for elem in arg:
        
        if elem in ['(', '{', '[']:
            stack.append(elem)
            
        elif elem in [')', '}', ']'] and len(stack) != 0:
            
            if ''.join({')':'(', '}':'{', ']':'['}[elem]) == stack[-1]:
                
                stack = stack[:-1]
                
            else: return False

    return True

    
    
example = list(input())
    
#true_example = list("({}[]([]))")
#false_example = list("([)]")

print(solver(example))