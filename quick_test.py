# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:56:00 2023
@fileName: quick_test.py
@author: Jiho
"""
def CLS() :
    print( "\014" ) 
    

def jiho01( N = 100 ) :
    f = 0
    
    for k in range( 1, N + 1 ) :
        if( k % 3 != 0 ) :
            f += k
            
    print( jiho01.__name__ + "() :", f )
    
    
def jiho02( N = 100 ) :
    f = 0
    a = N // 2
    
    for k in range( a ) :
        if( k % 3 == 0 ) :
            b = N - k - 1
            f = f + k + b
            
    f = f * 2 + 1
    print( jiho02.__name__ + "() :", f )
    

def jiho03( N = 100 ) :
    f = 0
    
    for k in range( 1, N, 3 ) :
        print(k)
        f += k + ( k + 1 )
    
    f += N
    print( jiho03.__name__ + "() :", f )


def main() :
    CLS()
    jiho01()
    jiho02()
    jiho03()
    

if( __name__ == "__main__" ) :
    main()


