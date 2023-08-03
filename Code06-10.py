# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 23:10:25 2022
@FileName: Code06-10.py
@author: Jiho
"""
def CLS() :
    print( "\014" )
        
def isStackFull() :
    global SIZE, stack, top
    
    if( top >= SIZE - 1 ) :
        return True
    else:
        return False

def isStackEmpty() :
    global SIZE, stack, top
    
    if( top == -1 ) :
        return True
    else:
        return False
    
def push( data ) :
    global SIZE, stack, top
    
    if( isStackFull() ) :
        print( "스택이 꽈악 찼습니다!" )
        return
    
    top += 1
    stack[ top ] = data
    
def pop() :
    global SIZE, stack, top
    
    if( isStackEmpty() ) :
        print( "스택이 비어있습니다." )
        return
    
    data = stack[ top ]
    stack[ top ] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    
    if( isStackEmpty() ) :
        print( "스택이 비어있습니다." )
        return
    return stack[ top ]

def checkBracket( expr ) :
    for ch in expr :
        if ch in "([{<" :
            push( ch )
        elif ch in ")]}>" :
            out = pop()
            if ch == ")" and out == "(" :
                pass
            elif ch == "]" and out == "[" :
                pass
            elif ch == "}" and out == "{" :
                pass
            elif ch == ">" and out == "<" :
                pass
            else :
                return False
        else :
            pass
        
    if isStackEmpty() :
        return True
    else :
        return False
    
# used ascii code by ord(), failed
def checkBracket01( expr ) :
    opened, closed = 0, 0
    for ch in expr :
        if ch in "([{<" :
            push(ch)
            opened = ord(ch)
        elif ch in ")]}>" :
            out = pop()
            if out != None :
                closed = ord(ch)
                opened = ord(out)
                calcs = closed - opened
                if closed > opened and calcs < 3:
                    return True
                else : 
                    pass
            else : 
                return False
            
    if isStackEmpty() :
        return True
    else :
        return False

# improving checkBracket01, success!
def checkBracket02( expr ) :
    for ch in expr :
        if ch in "([{<" :
            push( ch )
        elif ch in ")]}>" :
            out = pop()
            if out != None :
                if( ord(ch) - ord(out) ) < 3 :
                    return True
                else :
                    return False
        else :
            pass
        
    if isStackEmpty() :
        return True
    else :
        return False

# used array
def checkBracket03( expr ) :
    bracketAry1 = [ "(", "[", "{", "<" ]
    bracketAry2 = [ ")", "]", "}", ">" ]
    
    for ch in expr :
        if ch in bracketAry1 :
            push( ch )
        elif ch in bracketAry2 :
            out = pop()
            if out != None :
                if bracketAry1.index(out) == bracketAry2.index(ch) :
                    return True
                else :
                    return False
        else :
            pass
        
    if isStackEmpty() :
        return True
    else :
        return False
    
def checkBracket04( expr ) :
    bracketAry1 = "([{<"
    bracketAry2 = ")]}>"
    
    for ch in expr :
        if ch in bracketAry1 :
            push( ch )
        elif ch in bracketAry2 :
            out = pop()
            if out != None :
                if bracketAry1.index(out) == bracketAry2.index(ch) :
                    return True
                else :
                    return False
        else :
            pass
        
    if isStackEmpty() :
        return True
    else :
        return False

def checkBracket05( expr ) :
    bracketAry1 = "([{<"
    bracketAry2 = ")]}>"
    
    for ch in expr :
        if ch in bracketAry1 :
            push( ch )
        elif ch in bracketAry2 :
            out = pop()
            if out != None :
                return ( bracketAry1.index(out) == bracketAry2.index(ch) )
        
    return isStackEmpty()
    
def checkBracket_Test() :
    global SIZE, stack, top
    
    SIZE = 100
    stack = [ None for _ in range( SIZE ) ]
    top = -1
    
    exprAry = [ "(A+B)", ")A+B(", "((A+B)-C", "(A+B]", "(<A+{B-C}/[C*D]>)" ]
    
    for expr in exprAry :
        top = -1
        print( expr, "-->", checkBracket05( expr ) )
 
def main() :
    CLS()
    checkBracket_Test()
    
if( __name__ == "__main__" ) :
    main()

