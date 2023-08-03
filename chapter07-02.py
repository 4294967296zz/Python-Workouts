# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 00:49:44 2023
@fileName: chapter07-02.py
@author: Jiho
@description:
    [ 부품 찾기 ] **
    동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
    어느날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 견적서를 요청했다.
    동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
    이 때 가게안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
    예를 들어 가게의 부품이 총 5개 일때 부품 번호가 다음과 같다고 하자.
        N = 5
        [8, 3, 7, 9, 2]
    손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.
        N = 3
        [5, 7, 9]
    이 때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes,
    부품이 없으면 no 를 출력한다. 구분은 공백으로 한다.
    입력 예시 :
            5
            8 3 7 9 2
            3
            5 7 9
    출력 예시 : no yes yes
    입력 조건 : 첫째 줄에는 정수 N, 둘째 줄에는 공백으로 구분하여 N 개의 정수, 
                셋째 줄에는 정수 M, 넷째 줄에는 공백으로 구분하여 M 개의 정수
"""
def CLS() :
    print( "\014" )


# used "in" statement
def checkParts01() :
    global N, parts
    N = 5
    parts = [ 8, 3, 7, 9, 2 ]
    
    R = 3
    rParts = [ 5, 7, 9 ]
    # rInputs = input( "부품 번호를 공백으로 구분하여 입력해주세요 : " )
    # rParts = list( map ( int, rInputs.split(" ") ) )
    # R = len( rParts )
    prints = [ "no", "yes" ]
    
    print( checkParts01.__name__ + "() :" )
    for k in range( R ) :
        print( prints[ rParts[ k ] in parts ], end = " " )
    print()
    
    
# binary search
def findParts01( r ) :
    start = 0
    end = N - 1
    
    while( start <= end ) :
        mid = ( start + end ) >> 1
        if r == parts[ mid ] :
            return 1
        elif r > parts[ mid ] :
            start = mid + 1
        else :
            end = mid - 1
    return 0

            
# used binary search
def checkParts02() :
    global N, parts
    N = 5
    parts = [ 8, 3, 7, 9, 2 ]
    
    R = 3
    rParts = [ 5, 7, 9 ]
    # rInputs = input( "부품 번호를 공백으로 구분하여 입력해주세요 : " )
    # rParts = list( map ( int, rInputs.split(" ") ) )
    # R = len( rParts )
    
    parts.sort()
    prints = [ "no", "yes" ]
    
    print( checkParts02.__name__ + "() :" )
    for k in range( R ) :
        print( prints[ findParts01( rParts[ k ] ) ], end = " " )
    print()


# 이진 탐색의 대상이 되는 부품 리스트의 범위를 좁혀서 준비하기
def checkParts03A01() :
    global N, parts
    N = 5
    parts = [ 8, 3, 7, 9, 2 ]
    
    R = 3
    rParts = [ 5, 7, 9 ]
    # rInputs = input( "부품 번호를 공백으로 구분하여 입력해주세요 : " )
    # rParts = list( map ( int, rInputs.split(" ") ) )
    # R = len( rParts )
    
    parts.sort()
    rParts.sort()
    searchStart = rParts[ 0 ]
    searchEnd = rParts[ R - 1 ]
    parts = [ parts[ k ] for k in range( N ) if parts[ k ] >= searchStart ]
            
    prints = [ "no", "yes" ]
    
    print( checkParts03A01.__name__ + "() :" )
    for k in range( R ) :
        print( prints[ findParts01( rParts[ k ] ) ], end = " " )
    print()


# binary search
def findParts02( N, part, r ) :
    start = 0
    end = N - 1
    
    while( start <= end ) :
        mid = ( start + end ) >> 1
        if r == part[ mid ] :
            return 1
        elif r > part[ mid ] :
            start = mid + 1
        else :
            end = mid - 1
    return 0


# 이진 탐색의 대상이 되는 부품 리스트의 범위를 좁혀서 준비하기
def checkParts03A02() :
    N = 5
    parts = [ 8, 3, 7, 9, 2 ]
    
    R = 3
    rParts = [ 5, 7, 9 ]
    # rInputs = input( "부품 번호를 공백으로 구분하여 입력해주세요 : " )
    # rParts = list( map ( int, rInputs.split(" ") ) )
    # R = len( rParts )
    
    parts.sort()
    rParts.sort()
    searchStart = rParts[ 0 ]
    searchEnd = rParts[ R - 1 ]
    part = [ parts[ k ] for k in range( N ) if searchEnd >= parts[ k ] >= searchStart ]
            
    prints = [ "no", "yes" ]
    
    print( checkParts03A02.__name__ + "() :" )
    for k in range( R ) :
        print( prints[ findParts02( N, part, rParts[ k ] ) ], end = " " )
    print()


def main() :
    CLS()
    checkParts01()
    checkParts02()
    checkParts03A01()
    checkParts03A02()
    
if( __name__ == "__main__" ) :
    main()