# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 22:26:21 2023
@fileName: Googoodan.py
@author: Jiho
"""
def CLS() :
    print( "\014" )
    
def googoodan( X, Y ) :
    global M 
    M = []
    mSize = 10
    
    for k in range( mSize ) :
        ary = []
        for v in range ( mSize ) :
            ary += [ k * v ]
        M += [ ary ]
    
    return M[ X ][ Y ]
    
def googoodan_Test() :
    global M
    X, Y = 3, 3
    print( "\n" + googoodan.__name__ + "() :")
    print( X, "x", Y, "=", googoodan( X, Y ) )
    
def googoodan01( X, Y ) :
    global M 
    M = []
    mSize = 10
    xStart, yStart = 1, 2
    
    for k in range( xStart, mSize ) :
        ary = []
        for v in range ( yStart, mSize ) :
            ary += [ k * v ]
        M += [ ary ]
    
    return M[ X - xStart ][ Y - yStart ]
    
def googoodan01_Test() :
    global M
    X, Y = 3, 3
    print( "\n" + googoodan01.__name__ + "() :")
    print( X, "x", Y, "=", googoodan01( X, Y ) )


def main() :
    CLS()
    googoodan_Test()
    googoodan01_Test()
    
if( __name__ == "__main__" ) :
    main()