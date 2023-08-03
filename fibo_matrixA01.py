# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:10:39 2023
@fileName: fibo_matrix.py
@author: Jiho
"""
def CLS() :
    print( "\014" ) 
    
def divider( N ) :
    f = N
    arr = [ N ]
    
    while( f > 2 ) :
        left = f % 2
        f = f // 2
        arr += [ f + left ]
    
    return arr


def calc01( count, N ) :
    L = len( count ) - 1
    U0 = [ [ 0, 0 ], [ 0, 0 ] ]
    U1 = [ [ 1, 1 ], [ 1, 0 ] ]
    FM = [ U0, U1 ] + [ U0 ] * ( N - 1 )
    
    k = 1
    while( k < N ) :
        k = count.pop()
        a = FM[ k // 2 ][ 0 ][ 0 ] * FM[ k // 2 ][ 0 ][ 0 ] + FM[ k // 2 ][ 0 ][ 1 ] * FM[ k // 2 ][ 1 ][ 0 ]
        b = FM[ k // 2 ][ 0 ][ 0 ] * FM[ k // 2 ][ 0 ][ 1 ] + FM[ k // 2 ][ 0 ][ 1 ] * FM[ k // 2 ][ 1 ][ 1 ]
        c = FM[ k // 2 ][ 1 ][ 0 ] * FM[ k // 2 ][ 0 ][ 0 ] + FM[ k // 2 ][ 1 ][ 1 ] * FM[ k // 2 ][ 1 ][ 0 ]
        d = FM[ k // 2 ][ 1 ][ 0 ] * FM[ k // 2 ][ 0 ][ 1 ] + FM[ k // 2 ][ 1 ][ 1 ] * FM[ k // 2 ][ 1 ][ 1 ]
        FM[ k ] = [ [ a, b ], [ c, d ] ]
        print( FM )
        
        if k % 2 == 1 :
            print( k )
            a = FM[ k ][ 0 ][ 0 ] * FM[ 1 ][ 0 ][ 0 ] + FM[ k ][ 0 ][ 1 ] * FM[ 1 ][ 1 ][ 0 ]
            b = FM[ k ][ 0 ][ 0 ] * FM[ 1 ][ 0 ][ 1 ] + FM[ k ][ 0 ][ 1 ] * FM[ 1 ][ 1 ][ 1 ]
            c = FM[ k ][ 1 ][ 0 ] * FM[ 1 ][ 0 ][ 0 ] + FM[ k ][ 1 ][ 1 ] * FM[ 1 ][ 1 ][ 0 ]
            d = FM[ k ][ 1 ][ 0 ] * FM[ 1 ][ 0 ][ 1 ] + FM[ k ][ 1 ][ 1 ] * FM[ 1 ][ 1 ][ 1 ]
            FM[ k ] = [ [ a, b ], [ c, d ] ]
        
    print( FM )
        
    return FM


def fiboMatrix01A02( N ) :
    count = divider( N )
    X = calc01( count, N )
    return X


def fiboMatrix_Test02( N = 8 ) :
    print( fiboMatrix01A02.__name__ + "() :" )
    
    f = fiboMatrix01A02( N )
    for k in range( len( f[ N ] ) ) :
        print( f[ N ][ k ] )


def main() :
    CLS()
    fiboMatrix_Test02()
    
if( __name__ == "__main__" ) :
    main()

