# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:01:29 2023
@fileName: chapter08-03.py
@author: Jiho
@description :
    [ 개미 전사 ] **
    개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량 창고를 몰래 공격하려고 한다.
    메뚜기 마을에는 여러개의 식량 창고가 있는데 식량 창고는 일직선으로 이어져 있다.
    각 식량 창고에는 정해진 수의 식량을 저장하고 있으며, 개미 전사는 식량 창고를 선택적으로 약탈하여
    식량을 빼앗을 예정이다. 이 때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서
    서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다. 따라서 개미전사가 정찰병에게 들키지 않고
    식량 창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
    예를 들어 식량창고 4개가 다음과 같이 존재한다고 가정하자
        {1, 3, 1, 5}
    이때 개미 전사는 두번째 식량창고와 네번째 식량창고를 선택했을때 최댓값인 총 8개의 식량을 빼앗을 수 있다.
    개미 전사는 식량창고가 이렇게 일직선상일때 최대한 많은 식량을 얻기를 원한다.
    개미 전사를 위해 식량 창고 N개에 대한 정보가 주어졌을 때 
    얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.
    입력 조건 : 첫째 줄에 식량창고의 개수 N 이 주어진다
                둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다
                예시 )  4
                        1 3 1 5
    출력 조건 : 첫째 줄에 개미전사가 얻을 수 있는 식량의 최댓값을 출력하시오.
                예시 ) 8
    
"""
def CLS() :
    print( "\014" )
    
    
def getFood01() :
    N = 4
    K = "1 3 1 5"
    kList = list( map ( int, K.split(" ") ) )
    maxRob = ( N // 2 ) + ( N % 2 )
    
    maxIndex = [ ]
    
    for k in range( N ) :
        idx = kList.index( max( kList ) )
        maxIndex += [ [ idx, kList[ idx ] ] ]
        kList[ idx ] = 0
        
    vals = 0
    for k in range( maxRob ) :
        vals += maxIndex[ k ][ 1 ]
        
    print( getFood01.__name__ + "() :", vals )


def getFood02() :
    K = input( "수열을 띄어쓰기로 구분하여 입력하세요 : " )
    kList = list( map ( int, K.split() ) )
    N = len( kList )
    
    offset = -2
    res = 0
    
    while( offset <= N - 3 ) :
        vals = [ kList[ offset + 2 ], kList[ offset + 3 ] ]
        val = max( vals )
        res += val
        offset = offset + vals.index( val ) + 2
    
    print( getFood02.__name__ + "() :", res )
    
    
def getFood02A01() :
    K = "1 3 7 5 8 2 3 4 9"
    kList = list( map ( int, K.split(" ") ) )
    N = len( kList )
    offset = -2
    res = 0
    
    while( offset <= N - 3 ) :
        vals = [ kList[ offset + 2 ], kList[ offset + 3 ] ]
        val = max( vals )
        res += val
        offset = offset + vals.index( val ) + 2
    
    print( getFood02A01.__name__ + "() :", res )
    
    
def getFood03() :
    K = "1 3 7 5 8 2 3 4 9"
    kList = list( map ( int, K.split(" ") ) )
    N = len( kList )
    res = 0
    curr = 0
    offset = 0
    
    while( offset <= N - 1 ) :
        maxVal = max( curr, res + kList[ offset ] )
        res = curr
        curr = maxVal
        offset += 1
    
    print( getFood03.__name__ + "() :", curr )
    
    
def getFood03A01() :
    K = "1 3 7 5 8 2 3 4 9"
    kList = list( map ( int, K.split() ) )
    N = len( kList )
    res = curr = 0

    for k in range( N ):
        maxVal = max( res + kList[ k ], curr )
        res = curr
        curr = maxVal
        
    print( getFood03A01.__name__ + "() :", curr )
    

def main() :
    CLS()
    getFood01()
    # getFood02()
    getFood02A01()
    getFood03()
    getFood03A01()
    
if( __name__ == "__main__" ) :
    main()
