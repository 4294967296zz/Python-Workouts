# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:22:45 2023
@fileName: unFinisher.py
@author: Jiho
@description: 
    수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
    
    마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
    
    제한사항
    마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
    completion의 길이는 participant의 길이보다 1 작습니다.
    참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
    참가자 중에는 동명이인이 있을 수 있습니다.
"""
def CLS() :
    print( "\014" )
    
    # used loop
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i, k in enumerate( completion ) :
        if k != participant[ i ] :
            return participant[ i ]
    
    return participant[ -1 ]

def solution_test( participant = ["mislav", "stanko", "mislav", "ana"], completion = ["stanko", "ana", "mislav"] ) :
    print( solution.__name__+"() : \n", solution( participant, completion ) )
          
    # used hash
def solution01( participant, completion ):
    hashD = {}
    sumH = 0
    
    for k in participant :
        hashD[ hash( k ) ] = k
        sumH += hash( k )
    
    for k in completion :
        sumH -= hash( k )
        
    return hashD[ sumH ]

def solution01_test( participant = ["mislav", "stanko", "mislav", "ana"], completion = ["stanko", "ana", "mislav"] ) :
    print( solution01.__name__+"() : \n", solution01( participant, completion ) )

    # used collections.Counter
def solution02( participant, completion ):
    import collections
    answer = collections.Counter( participant ) - collections.Counter( completion )
    
    return list( answer.keys() ) [ 0 ]
    

def solution02_test( participant = ["mislav", "stanko", "mislav", "ana"], completion = ["stanko", "ana", "mislav"] ) :
    print( solution02.__name__+"() : \n", solution02( participant, completion ) )


def main() :
    
    CLS()
    solution_test()
    solution01_test()
    solution02_test()

if __name__ == "__main__" :
    main()
