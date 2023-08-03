# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:38:02 2023
@fileName: coin01.py
@author: Jiho
"""
def CLS() :
    print( "\014" )
    
import random 
    
def coin( N ) : 
    result = [ ]
    for i in range( N ) :
        r = random.randint( 0, 1 )
        if( r == 1 ) :
            result.append( 1 )
        else :
            result.append( 0 )
    return result
    
def montaCoin( N ) :
    cnt = 0
    for i in range( N ) : 
        cnt += coin( 1 ) [ 0 ]
        
    result = cnt / N
    return result

def coin_Test( N = 100 ) :
    print( "\n" + montaCoin.__name__ + "() :" )
    print( montaCoin( N ) )

def coin01( N ) : 
    global result
    result = [ ]
    # for _ in range( N ) :
    r = random.randint( 0, 1 )
    if( r == 1 ) :
        result.append( 1 )
    else :
        result.append( 0 )
    return result
    
def montaCoin01( N ) :
    global result
    cnt = 0
    for _ in range( N ) : 
        cnt += coin01( 1 ) [ 0 ]
        
    result = cnt / N
    return result

def coin01_Test( N = 100 ) :
    print( "\n" + montaCoin01.__name__ + "() :" )
    print( montaCoin01( N ) )

def coin02( N ) : 
    # global result
    # result = [ ]
    # for _ in range( N ) :
    r = random.randint( 0, 1 )
    # if( r == 1 ) :
    #     result.append( 1 )
    # else :
    #     result.append( 0 )
    return r
    
def montaCoin02( N ) :
    global result
    cnt = 0
    for _ in range( N ) : 
        cnt += coin02( 1 )
        
    result = cnt / N
    return result

def coin02_Test( N = 100 ) :
    print( "\n" + montaCoin02.__name__ + "() :" )
    print( montaCoin02( N ) )

def coin03( N ) : 
    r = random.randint( 0, 1 )
    return r
    
def montaCoin03( N ) :
    global result
    cnt = 0
    for _ in range( N ) : 
        cnt += coin03( 1 )
        
    result = cnt / N
    return result

def coin03_Test( N = 100 ) :
    print( "\n" + montaCoin03.__name__ + "() :" )
    print( montaCoin03( N ) )


def main() :
    CLS()
    coin_Test()
    coin01_Test()
    coin02_Test()
    coin03_Test()
    
if( __name__ == "__main__" ) :
    main()
