# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:04:01 2023
@fileName: fibo_matrix01.py
@author: Jiho
"""
def CLS() :
    print( "\014" ) 
    
def divider( N ) :
    f = N
    arr = [ N ]
    
    while( f > 1 ) :
        left = f % 2
        f = f // 2
        arr += [ f + left ]
    
    return arr

def calc( count, N ) :
    L = len( count ) - 1
    U0 = [ [ 0, 0 ], [ 0, 0 ] ]
    U1 = [ [ 1, 1 ], [ 1, 0 ] ]
    FM = [ U0, U1 ] + [ U0 ] * ( N - 1 )
    
    print( count )
    
    for k in range( L , 0, -1 ) :
        idx = count[ k ]
        
        if idx > 1 and idx % 2 == 0 :
            idx -= 1
        
        a = FM[ idx ][ 0 ][ 0 ] * FM[ idx ][ 0 ][ 0 ] + FM[ idx ][ 0 ][ 1 ] * FM[ idx ][ 1 ][ 0 ]
        b = FM[ idx ][ 0 ][ 0 ] * FM[ idx ][ 0 ][ 1 ] + FM[ idx ][ 0 ][ 1 ] * FM[ idx ][ 1 ][ 1 ]
        c = FM[ idx ][ 1 ][ 0 ] * FM[ idx ][ 0 ][ 0 ] + FM[ idx ][ 1 ][ 1 ] * FM[ idx ][ 1 ][ 0 ]
        d = FM[ idx ][ 1 ][ 0 ] * FM[ idx ][ 0 ][ 1 ] + FM[ idx ][ 1 ][ 1 ] * FM[ idx ][ 1 ][ 1 ]
        
        A = [ [ a, b ], [ c, d ] ]
        
        FM[ count[ k - 1 ] ] = A
        
        a = A[ 0 ][ 0 ] * FM[ 1 ][ 0 ][ 0 ] + A[ 0 ][ 1 ] * FM[ 1 ][ 1 ][ 0 ]
        b = A[ 0 ][ 0 ] * FM[ 1 ][ 0 ][ 1 ] + A[ 0 ][ 1 ] * FM[ 1 ][ 1 ][ 1 ]
        c = A[ 1 ][ 0 ] * FM[ 1 ][ 0 ][ 0 ] + A[ 1 ][ 1 ] * FM[ 1 ][ 1 ][ 0 ]
        d = A[ 1 ][ 0 ] * FM[ 1 ][ 0 ][ 1 ] + A[ 1 ][ 1 ] * FM[ 1 ][ 1 ][ 1 ]
        
        B = [ [ a, b ], [ c, d ] ]
        print( "B : , ", B  )
        
        FM[ count[ k - 1 ] ] = B
        
    print( FM )
    
    
    return FM


def fiboMatrix01( N ) :
    count = divider( N )
    FM = calc( count, N )
    return FM


def fiboMatrix_Test( N = 8 ) :
    print( fiboMatrix01.__name__ + "() :" )
    
    f = fiboMatrix01( N )
    for k in range( len( f[ N ] ) ) :
        print( f[ N ][ k ] )
        
        
        
def main() :
    CLS()
    fiboMatrix_Test()
    
if( __name__ == "__main__" ) :
    main()
