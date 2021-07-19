# 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution1(a, b):
    answer=0
    for i in range(len(a)):
        answer+=a[i]*b[i]
    return answer

def solution2(a, b):
    answer=0
    answer=sum(n*m for n, m in zip(a, b) )
    return answer
print(solution([1,2,3,4],[-3,-1,0,2]),"result:3")

#zip 함수 사용법
#여러 개의 iterable자료형이 개수가 동일할 때 사용
# 자료형 묶을떄 사용
# ex : 리스트 두개를 딕셔너리로 만들때
#      dic = {name:value for name,value in zip(list1,list2)}