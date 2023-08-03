# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:33:34 2023
@fileName: divider.py
@author: Jiho
@description:
    [ 1이 될 때까지 ]
    어떠한 수 N 이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행.
    단 두 번째 연산은 N 이 K 로 나누어 떨어질때만 선택가능.
    1. N 에서 1을 뺀다.
    2. N 을 K 로 나눈다.
    N 과 K 가 주어질 때 N이 1이 될 때까지 1번 or 2번의 과정을 수행해야 하는 최소 횟수는?
"""
def CLS() :
    print( "\014" ) 
    
def divider01( N = 17, K = 4 ) :
    f = N
    count = 0
    
    while( f > 1 ) :
        if N % K == 0 :
            f = N % K
            count += 1
        else :
            f -= 1
    print( count )
            
def main() :
    CLS()
    divider01()


if( __name__ == "__main__" ) :
    main()