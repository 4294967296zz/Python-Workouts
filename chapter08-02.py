# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:58:40 2023
@fileName: chapter08-02.py
@author: Jiho
@description:
    [ 1로 만들기 ]
    정수 X가 주어질 때 정수 X 에 사용할 수 있는 연산은 다음과 같이 4가지다.
        a) X가 5로 나누어 떨어지면 5로 나눈다.
        b) X가 3으로 나누어 떨어지면 3으로 나눈다.
        c) X가 2로 나누어 떨어지면 2로 나눈다.
        d) X에서 1을 뺀다.
    정수 X가 주어졌을 때, 위의 a, b, c, d 연산 4개를 적절히 사용해서 1을 만들려고 한다.
    연산을 사용하는 횟수의 최솟값을 출력하시오.
"""
def CLS() :
    print( "\014" ) 
    
    
#  연산 수행 func
def calc01( f ) :
    global count
    
    divider = [ 5, 3, 2 ]
    L = len( divider )
    
    for k in range( L ) :
        if ( f % divider[ k ] ) == 0 :
            f = ( f // divider[ k ] )
            count += 1
            return f
        
    f -= 1
    count += 1
    return f


def calc01A01( f ) :
    global count
    
    divider = [ 5, 3, 2 ]
    L = len( divider )
    
    for k in range( L ) :
        if ( f % divider[ k ] ) == 0 :
            f = ( f // divider[ k ] )
            return f
        
    f -= 1
    return f


# other way of calc01
def calc02( f ) :
    global count
    
    r = [ 2, 3, 5 ]
    k = 0
    
    while( len( r ) ) :
        k = r.pop()
        if ( f % k ) == 0 :
            f = ( f // k )
            count += 1
            return f
            break
        
    f -= 1
    count += 1
    return f


# other way of calc01
def calc02A01( f ) :
    r = [ 2, 3, 5 ]
    k = 0
    
    while( len( r ) ) :
        k = r.pop()
        if ( f % k ) == 0 :
            f = ( f // k )
            return f
            break
        
    f -= 1
    return f


def divider01( X = 84 ) :
    global count
    count = 0
    f = X
    
    while( f > 1 ) :
        f = calc02( f )
    print( divider01.__name__ + "() :" , count )


def divider02( X = 84 ) :
    count = 0
    f = X
    
    while( f > 1 ) :
        count += 1
        f = calc02A01( f )
    print( divider02.__name__ + "() :" , count )


def main() :
    CLS()
    divider01()
    

if( __name__ == "__main__" ) :
    main()