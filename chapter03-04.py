# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:33:34 2023
@fileName: chapter03-04.py
@author: Jiho
@description:
    [ 1이 될 때까지 ]
    어떠한 수 N 이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행.
    단 두 번째 연산은 N 이 K 로 나누어 떨어질때만 선택가능.
        1. N 에서 1을 뺀다.
        2. N 을 K 로 나눈다.
    N 과 K 가 주어질 때 N이 1이 될 때까지 1번 or 2번의 과정을 수행해야 하는 최소 횟수를 출력하시오.
    * 조건 : 2 ≤ N, K ≥ 100,000 이고 N 은 항상 K 보다 크다.
"""
def CLS() :
    print( "\014" ) 


# 연산 수행 func
def calc01( f, K ) :
    global count
    count += 1
    
    if f % K == 0 :
        return f // K
    else :
        return f - 1


def calc01A01( f, K ) :
    global count
    count += 1
    fk = [ f // K ] + [ f - 1 ] * ( K - 1 )
    
    return fk[ f % K ]


def calc01A02( f, K ) :
    fk = [ f // K ] + [ f - 1 ] * ( K - 1 )
    return fk[ f % K ]


def divider03( N = 58, K = 5 ) :
    f = N
    count = 0
    
    while( f > 1 ) :
        count += 1
        f = calc01A02( f, K )
    print( divider03.__name__ + "() :" , count )


# improving calc01
def calc02( f, K ) :
    global count
    count += 1
    
    arr = [ ( f // K ), ( f - 1 ) ]
    idx = int( ( f % K ) > 0 )
    return arr[ idx ]


# other way of calc02, reducing exec num
def calc03( f, K ) :
    global count
    
    D = f % K
    idx = int( D != 0 )
    C = [ 1, D ]
    r = [ ( f // K ), ( f - D ) ]
    
    f = r[ idx ]
    count += C[ idx ]
    return f


# other way of calc02, reducing exec num
def calc03A01( f, K ) :
    global count
    
    D = ( f % K )
    idx = int( D != 0 )
    C = [ 1, D ]
    r = [ ( f // K ), ( f - D ) ]
    
    f = r[ idx ]
    count += C[ idx ]
    return f


def divider01( N = 58, K = 5 ) :
    global count
    f = N
    count = 0
    
    while( f > 1 ) :
        f = calc02( f, K )
    print( divider01.__name__ + "() :" , count )


def divider02( N = 58, K = 5 ) :
    global count
    f = N
    count = 0
    
    while( f > 1 ) :
        f = calc03A01( f, K )
    print( divider02.__name__ + "() :" , count )


def main() :
    CLS()
    divider01()
    divider02()
    divider03()


if( __name__ == "__main__" ) :
    main()
    