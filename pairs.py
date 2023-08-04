# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:28:33 2023
@fileName: pairs.py
@author: Jiho
@description :
    괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

    "()()" 또는 "(())()" 는 올바른 괄호입니다.
    ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
    '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
    
    제한사항
    문자열 s의 길이 : 100,000 이하의 자연수
    문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
    
"""
def CLS() :
    print( "\014" )

def solution(s):
    stack = []
    for k in s : 
        if k == "(" :
            stack.append( k )
        elif len( stack ) == 0 or stack.pop() != "(" :
            return False
    if stack :
        return False
    else :
        return True
    
def solution_test( s = "(()())" ) :
    print( solution.__name__ + "() : \n", solution( s ) ) 
    
def solution02(s):
    count = 0

    for k in s : 
        if k == "(" :
            count += 1
        elif k == ")" :
            count -= 1
        if count < 0 :
            return False

    return count == 0
    
def solution02_test( s = "(()())" ) :
    print( solution02.__name__ + "() : \n", solution02( s ) ) 

def main() :
    CLS()
    solution_test()
    solution02_test()
    
if (__name__ == "__main__") :
    main()
