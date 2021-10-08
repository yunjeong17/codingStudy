# 문제 : 없는 숫자 더하기
# 링크 :  https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    return sum(list(set([1,2,3,4,5,6,7,8,9])-set(numbers)))