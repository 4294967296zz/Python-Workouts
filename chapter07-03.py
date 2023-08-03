# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:55:44 2023
@fileName: chapter07-03.py
@author: Jiho
@description :
    [ 떡볶이 떡 만들기 ] **
    오늘 동빈이는 여행가신 부모님을 대신해서 떡집 일을 하기로 했다. 
    오늘은 떡볶이를 떡을 만드는 날이다.
    동빈이네 떡볶이 떡은 길이가 일정하지 않다. 
    대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 맞춰서 잘라준다.
    절단기에 높이(H)를 지정하면 줄지어진 떡을 한번에 절단할 수 있다.
    높이가 H보다 긴 떡은 H 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다.
    예를 들어 높이가 19, 14, 10, 17 cm 인 떡이 나란히 있고 절단기 높이를 15cm 로 지정하면
    자른 뒤 떡의 높이는 15, 14, 10, 15cm 가 될 것이다.
    잘린 떡의 길이는 차례대로 4, 0, 0, 2 cm 이다.
    손님은 6cm 만큼의 길이를 가져간다.
    손님이 요청한 총 길이가 M 일때 적어도 M 만큼의 떡을 얻기 위해
    절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
    
    입력 조건 : 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M 이 주어진다
                둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이므로
                손님은 필요한 양만큼 떡을 사갈 수 있다.
                예시 )  4 6
                        19 15 10 17
    출력 조건 : 적어도 M 만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값을 출력한다.
                예시 ) 15
"""
def CLS() :
    print( "\014" )
    

def main() :
    CLS()
    

if( __name__ == "__main__" ) :
    main()