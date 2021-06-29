# 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer=0
    answer=sum(n*m for n, m in zip(a, b) )
    return answer
print(solution([1,2,3,4],[-3,-1,0,2]),"result:3")