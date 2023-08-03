# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:30:28 2022
@FileName : fibo01.py
@author: Jiho
@Description : fibonacci Seriese

f(0) = 0, f(1) = 1,
f(n) = f(n-1) + f(n-2)

"""

def CLS() :
    print( '\014' )

# Recursion
def fiboR( N = 5 ) :
    if( N <= 2 ) :
        return 1
    else :
        return fiboR( N - 1 ) + fiboR( N - 2 )

def fiboR_Test( N ) :
    print( "\n" + fiboR.__name__ + "() :")
    for k in range( 1, N + 1 ) :
        print( fiboR( k ), end=', ' )

def fiboR01( N = 5 ) :
    if ( N < 2 ) :
        return N
    
    return fiboR01( N - 1 ) + fiboR01( N - 2 )
        
def fiboR02( N = 5 ) :
    f = N
    if ( N < 2 ) :
        return N
    
    f = fiboR02( N - 1 ) + fiboR02( N - 2 )
    return f

def fiboR03( N = 5 ) :
    f = [ 0, 1 ]
    
    if ( N < 2 ) :
        return N
    
    f = fiboR03( N - 1 ) + fiboR03( N - 2 )
    
    return f

def fiboR03_Test( N ) :
    print( "\n" + fiboR03.__name__ + "() :")
    for k in range( 1, N + 1 ) :
        print( fiboR03( k ), end=', ' )

def fiboR04( N = 5 ) :
    if ( N < 2 ) :
        return N
    
    f = fiboR04( N - 1 ) + fiboR04( N - 2 )
    return f


def fiboR04_Test( N ) :
    print( "\n" + fiboR04.__name__ + "() :")
    for k in range( 1, N + 1 ) :
        print( fiboR04( k ), end=', ' )
        
# omitting codes..
def fiboR05( N ) :
    global resAry
    if ( N < 2 ) :
        return N
        
    f = fiboR05( N - 1 ) + fiboR05( N - 2 )
    if ( resAry[ N ] == 0 ) :
        resAry[ N ] = f
    
    return f

def fiboR05_Test( N = 5 ) :
    global resAry
    resAry = [0, 1] + [ 0 ] * ( N - 1 )
    
    print( "\n" + fiboR05.__name__ + "() :")
    for k in range( 1, N + 1 ) :
        fiboR05( k )
        print(resAry[ k ], end = ", " )

# reverse test func
def fiboR06( N ) :
    global resAry, count
    count += 1

    if ( N < 2 ) :
        resAry[ N ] = N
        return N
    else :
        f = fiboR06( N - 1 ) + fiboR06( N - 2 )
        resAry[ N ] = f
    return f

def fiboR06_Test( N = 5 ) :
    global resAry, count
    count = 0
    resAry = [0, 1] + [ 0 ] * ( N - 1 )
    
    print( "\n" + fiboR06.__name__ + "() :")
    for k in range( N , 1, -1 ) :
        # fiboR06( k )
        print( fiboR06( k ), end = ", " )
                
    # for k in range( 1, N + 1 ) :
    #     print( resAry[ k ], end = ", " )
    
# reverse test func
def fiboR06A01( N ) :
    global resAry, count
    count += 1

    if ( N < 2 ) :
        resAry[ N ] = N
        return N, [ resAry[ N ] ]
    else :
        f = fiboR06A01( N - 1 ) + fiboR06A01( N - 2 )
        resAry[ N ] = f
    return f, [ resAry[ N ] ]

def fiboR06A01_Test( N = 5 ) :
    global resAry, count
    count = 0
    resAry = [0, 1] + [ 0 ] * ( N - 1 )
    
    print( "\n" + fiboR06A01.__name__ + "() :")
    
    print( fiboR06A01( 3 ), end = ", " )
    print()
    print( resAry[ 3 ], end = ", " )
    
    # for k in range( N , 1, -1 ) :
    #     # fiboR06( k )
    #     print( fiboR06A01( k ), end = ", " )
                
    # for k in range( 1, N + 1 ) :
    #     print( resAry[ k ], end = ", " )

def fiboR06A02( N ) :
    global resAry, count
    count += 1

    if ( N < 2 ) :
        resAry[ N ] = N
        return N
    else :
        f = fiboR06A02( N - 1 ) + fiboR06A02( N - 2 )
        resAry[ N ] = f
    return f

def fiboR06A02_Test( N = 5 ) :
    global resAry, count
    count = 0
    resAry = [0, 1] + [ 0 ] * ( N - 1 )
    
    print( "\n" + fiboR06A02.__name__ + "() :")
    
    print( fiboR06A02( 3 ), end = ", " )
    print()
    print( resAry[ 3 ], end = ", " )
    
    # for k in range( N , 1, -1 ) :
    #     # fiboR06( k )
    #     print( fiboR06A01( k ), end = ", " )
                
    # for k in range( 1, N + 1 ) :
    #     print( resAry[ k ], end = ", " )
    
def fiboR06A03( N ) :
    global resAry, count

    if ( N < 2 ) :
        resAry[ N ] = N
        # count += 1
        return N
    else :
        if ( resAry[ N ] > 0 ) :
            count += 1
            print( "N : ", N, count, resAry[ N ] )
            return resAry[ N ]
        f = fiboR06A03( N - 1 ) + fiboR06A03( N - 2 )
        resAry[ N ] = f
    return f

def fiboR06A03_Test( N = 4 ) :
    global resAry, count
    N = 4
    resAry = [0, 1] + [ 0 ] * ( N - 1 )
    
    print( "\n" + fiboR06A03.__name__ + "() :" )
    print( N )
    for k in range( 4, N + 1 ) :
        count = 0
        print( N, fiboR06A03( k ), count, end = ", " )
        print()

def fiboR06A04( N ) :
    global resAry, count

    if ( N < 2 ) :
        resAry[ N ] = N
        count += 1  
        return N
    else :
        if ( resAry[ N ] > 0 ) :
            count += 1
            return resAry[ N ]
        f = fiboR06A04( N - 1 ) + fiboR06A04( N - 2 )
        resAry[ N ] = f
    return f

def fiboR06A04_Test( N = 4 ) :
    global resAry, count
    N = 4
    resAry = [0, 1] + [ 0 ] * ( N - 1 )
    
    print( "\n" + fiboR06A04.__name__ + "() :" )
    for k in range( 1, N + 1 ) :
        count = 0
        fiboR06A04( k )
        print( N, fiboR06A04( k ), count, end = ", " )
        print()
    print(resAry)
    
def fiboR06A05( N ) :
    global resAry, count

    if ( N < 2 ) :
        resAry[ N ] = N
        count += 1  
        return N
    else :
        if ( resAry[ N ] > 0 ) :
            count += 1
            return resAry[ N ]
        f = fiboR06A05( N - 1 ) + fiboR06A05( N - 2 )
        resAry[ N ] = f
    return f

def fiboR06A05_Test( N = 4 ) :
    global resAry, count
    N = 5
    resAry = [0,1] + [ 0 ] * ( N - 1 )
    
    print( "\n" + fiboR06A05.__name__ + "() :" )
    for k in range( 1, N + 1 ) :
        count = 0
        fiboR06A05( k )
        print(resAry[k], "count : ", count )

def fiboR06A06( N ) :
    global resAry, count, calc

    if ( N < 2 ) :
        resAry[ N ] = N
        count += 1  
        return N
    else :
        if ( resAry[ N ] > 0 ) :
            count += 1
            return resAry[ N ]
        f = fiboR06A06( N - 1 ) + fiboR06A06( N - 2 )
        calc += 1
        resAry[ N ] = f
    return f

def fiboR06A06_Test( N = 4 ) :
    global resAry, count, calc
    N = 5
    resAry = [0,1] + [ 0 ] * ( N - 1 )
    print( "\n" + fiboR06A06.__name__ + "() :" )
    count = 0
    calc = 0
    
    for k in range( 1, N + 1 ) :
        fiboR06A06( k )
        print(k, resAry[k], "count : ", count, calc )


# Loop
def fiboL( N = 5 ) :
    f = [ 0, 1, 1 ]
    
    for k in range( 3, N + 1 ) : 
        f.append( f[ k - 1 ] + f[ k - 2 ] )
        
    return f[ N ]

def fiboL_Test( N ) :
    print( "\n" + fiboL.__name__ + "() :")    
    for k in range( 1, N + 1 ) :
        print( fiboL( k ), end=', ' )

# new way
def fiboL01( N = 5 ) :
    a = 0
    b = 1
    c = a + b
    
    if( N == 1 ) : 
        return c
    else : 
        for k in range( N - 1 ) :
            c = a + b
            a = b
            b = c
        
        return c

def fiboL01_Test( N ) :
    print( "\n" + fiboL01.__name__ + "() :")    
    for k in range( 1, N + 1 ) :
        print( fiboL01( k ), end=', ' )

# improving fiboL01
def fiboL02( N ) :
    f = [ 0, 1 ]
    for k in range( 2, N + 1 ) :
        f.append( f[ k - 1 ] + f[ k - 2 ] )
    
    return f[N]

def fiboL02_Test( N ) :
    print( "\n" + fiboL02.__name__ + "() :")    
    for k in range( 1, N + 1 ) :
        print( fiboL02( k ), end=', ' )

def fiboL03( N ) :
    f = [ 0, 1 ] + [ 0 ] * ( N + 1 )
    
    for k in range( 2, N + 1 ) :
        f[ k ] = f[ k - 1 ] + f[ k - 2 ] 
    
    return f[ N ]

def fiboL03_Test( N ) :
    print( "\n" + fiboL03.__name__ + "() :")    
    for k in range( 1, N + 1 ) :
        print( fiboL03( k ), end=', ' )
        


def fibo_all( N = 5 ) :
    # fiboR_Test( N )
    # fiboR03_Test( N )
    # fiboR04_Test( N )
    # fiboR05_Test( N )
    # fiboR06_Test( N )
    # fiboR06A01_Test( N )
    # fiboR06A02_Test( N )
    # fiboR06A03_Test( N )
    # fiboR06A04_Test( N )
    # fiboR06A05_Test( N )
    fiboR06A06_Test( N )
    # fiboR07_Test( N )
    # fiboL_Test( N )
    # fiboL01_Test( N )
    # fiboL02_Test( N )
    # fiboL03_Test( N )
    
def main() :
    CLS()
    fibo_all()

if ( __name__ == "__main__" ) :
    main()
