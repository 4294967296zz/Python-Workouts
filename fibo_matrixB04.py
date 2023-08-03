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
    arr = [ f ]
    
    while( f > 3 ) :
        f = f // 2
        arr += [ f ]
    
    return arr


def matMUL( X, Y ) :
    a = X[ 0 ][ 0 ] * Y[ 0 ][ 0 ] + X[ 0 ][ 1 ] * Y[ 1 ][ 0 ]
    b = X[ 0 ][ 0 ] * Y[ 0 ][ 1 ] + X[ 0 ][ 1 ] * Y[ 1 ][ 1 ]
    c = X[ 1 ][ 0 ] * Y[ 0 ][ 0 ] + X[ 1 ][ 1 ] * Y[ 1 ][ 0 ]
    d = X[ 1 ][ 0 ] * Y[ 0 ][ 1 ] + X[ 1 ][ 1 ] * Y[ 1 ][ 1 ]
    f = [ [ a, b ], [ c, d ] ]
        
    return f    


def fiboMatrix( N ) :
    UN = [ [ 1, 0 ], [ 0, 1 ] ]
    U0 = [ [ 0, 0 ], [ 0, 0 ] ]
    U1 = [ [ 1, 1 ], [ 1, 0 ] ]
    U2 = [ [ 2, 1 ], [ 1, 1 ] ]
    
    UA = [ UN, U1 ]
    FM = [ U0, U1, U2 ] + [ U0 ] * ( N - 2 )

    count = divider( N )
    k = 2
    
    while( k < N ) :
        k = count.pop()
        FM[ k ] = matMUL( FM[ k // 2 ], FM[ k // 2 ] )
        FM[ k ] = matMUL( FM[ k ], UA[ k & 1 ] )
        
    return FM


def fiboMatrix_Test( N = 7 ) :
    print( fiboMatrix.__name__ + "() :" )
    
    f = fiboMatrix( N )
    
    for k in range( len( f[ N ] ) ) :
        print( f[ N ][ k ] )


def main() :
    CLS()
    fiboMatrix_Test()
    
if( __name__ == "__main__" ) :
    main()

