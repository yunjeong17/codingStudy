# 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

# n 마리 중 n/2 마리 가져가도됨
# 가져갈 수 있는 폰켓몬의 최대 종류수 구하기 

def solution(nums):
    answer = 0
    mine = len(nums)//2
    distinctNums=set(nums)
    if len(distinctNums)<mine:
        answer=len(distinctNums)
    else :
        answer=mine
    return answer


# 다른사람 풀이
#min() >> 여러 인자들 중 가장 작은 값을 반환
# 이번 문제에서는 값들 중 작은 값을 반환해야하니까 min 쓰면 적절.
# 내 문제점 : 무조건 for, if, else문 먼저 나온다. 람다식 풀이법, 각종 모듈 및 함수 사용 등을 생각할 것.

def solution2(ls):
    return min(len(ls)/2, len(set(ls)))


print(solution([3,1,2,3]),"   resutl:2")
print(solution([3,3,3,2,2,4]),"   result:3")
print(solution([3,3,3,2,2,2]),"   resutl:2")