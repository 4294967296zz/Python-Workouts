# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:50:47 2023

@fileName: fibonachi.py
@author: Jiho
@description :
    피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

    예를들어
    
    F(2) = F(0) + F(1) = 0 + 1 = 1
    F(3) = F(1) + F(2) = 1 + 1 = 2
    F(4) = F(2) + F(3) = 1 + 2 = 3
    F(5) = F(3) + F(4) = 2 + 3 = 5
    와 같이 이어집니다.
    
    2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
    
    제한 사항
    n은 2 이상 100,000 이하인 자연수입니다.
"""

def CLS() :
    print( "\014" )
    
def solution( n ):
    answer = 0
    f = [ 0, 1 ] + [ 0 ] * ( n + 1 )
    
    for k in range( 2, n + 1 ) :
        f[ k ] = f[ k - 1 ] + f[ k - 2 ] 
        
    answer = f[ n ] % 1234567
    
    return answer

def solution_test( n = 3 ) :
    print( solution.__name__+"() : \n", solution( n ) )
    
    
def solution01( n ):
    if n < 2 :
        return n
    
    return solution01( n - 1 ) + solution01( n - 2 )

def solution01_test( n = 3 ) :
    print( solution01.__name__+"() : \n", solution01( n ) )
    
    
    
def main() :
    CLS()
    solution_test()
    solution01_test()

if( __name__ == "__main__" ) :
    main()    

