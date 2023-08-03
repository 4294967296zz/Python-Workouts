# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:03:22 2023
@fileName: chapter11-03.py
@author: Jiho
@description:
    [ 문자열 뒤집기 ]
    0과 1로만 이루어진 문자열 S가 있다.
    문자열 S에 있는 모든 숫자를 전부 같은 값으로 만들려고 한다.
    이 때, 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
    뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
    예를 들어 S = 0001100 일때
        1. 전체를 뒤집으면 1110011 이 된다.
        2. 4번째부터 5번째까지 뒤집으면 1111111이 되어 2번의 행동에 모두 같은 숫자가 되었다.
    하지만 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 0000000이 된다.
    즉, 1번의 행동만에 모두 같은 숫자로 만들 수 있다.
    문자열 S가 주어졌을 때, 모든 숫자를 같은 값으로 만드는 행동의 최소 횟수를 출력하시오.
    
    "00011100000011111111110011000"
    "00", "01", "10", "11"
     
    
"""
def CLS() :
    print( "\014" ) 
            

# 숫자의 갯수를 세어서 반환
def counter01( S ) :
    counter = [ 0, 0 ]
    for k in range( len( S ) ) :
        counter[ int( S[ k ] ) ] += 1
    return counter
    

def flip01( S = "00011100" ) :
    count = 0
    counter = counter01( S )
    trigger = counter.index( min( counter ) )
    
    
# 연속된 숫자의 갯수를 세어서 행렬을 만들기
def counter02( S ) :
    L = len( S ) - 1
    counter = [ [], [] ]
    count = 1
    
    for k in range( L ) :
        if k != L -1 :
            if S[ k ] == S[ k + 1 ] :
                count += 1
            else :
                counter[ int( S[ k ] ) ] += [ count ]
                count = 1
        else :
            counter[ int( S[ k ] ) ] += [ count + 1 ]
            
    return counter


def flip02( S = "00011100000011111111110011000" ) :
    mat = counter02( S )
    ML = [ len( mat[ 0 ] ), len( mat[ 1 ] ) ]
    f = min( ML )
    
    print( flip02.__name__ + "() :" , f )
    
    
# improving countet02 - 연속된 숫자의 갯수만 세기
def counter02A01( S ) :
    L = len( S ) - 1
    counter = [ 0, 0 ]
    
    for k in range( L ) :
        if k != ( L - 1 ) :
            if S[ k ] != S[ k + 1 ] :
                counter[ int( S[ k ] ) ] += 1
        else :
            counter[ int( S[ k ] ) ] += 1
            
    return counter


def flip03( S = "00011100000011111111110011000" ) :
    counts = counter02A01( S )
    f = min( counts )
    print( flip03.__name__ + "() :" , f )
    

    
def main() :
    CLS()
    flip01()
    flip02()
    flip03()

if( __name__ == "__main__" ) :
    main()

