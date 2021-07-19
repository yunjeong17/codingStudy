#하샤드 수
#https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    sumX=0
    k=x
    while(k/10!=0):
        n=int(k%10)
        k=int(k/10)
        sumX+=n
        print(sumX)
    if int(x%sumX)!=0:
        answer=False
    return answer

print(solution(11))