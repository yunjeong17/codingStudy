# 문제 : 가장 큰 수
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(num):
     num = list(map(str, num)) 
     num.sort(key = lambda x : x*3, reverse = True) 
     return str(int(''.join(num)))


print(solution([3, 30, 34, 5, 9]))