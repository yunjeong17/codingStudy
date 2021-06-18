#수박수박수
#https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    a="수"
    b="박"
    for i in range(n):
        if( int(i%2)==1 ): #홀수번째일 때
            answer+=b
        else: #짝수번째일 때
            answer+=a
    return answer

print(solution(3))