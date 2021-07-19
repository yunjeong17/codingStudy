# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982
import time
def solution1(d, budget):
    start=time.time()
    answer = 0
    d.sort()
    for i in range(len(d)):
        budget-=d[i]
        if(budget<0):
            answer=i
            break
        if(len(d)==i+1):
            answer=i+1
    end=time.time()
    print("WorkingTime: {} sec".format(end-start))
    return answer

print(solution1([1,3,2,5,4],9),"result: 3")
print(solution1([2,2,3,3],10),"result: 4")

#다른사람 풀이
def solution2(d, budget):
    start=time.time()
    d.sort() #sort해서 작은 순서로
    while budget < sum(d): #d의 합이 예산보다 크면
        d.pop() #d의 제일 큰 숫자를 pop으로 꺼냄
    end=time.time()
    print("WorkingTime: {} sec".format(end-start))
    return len(d) #길이를 출력
#근데 이게 더 오래걸리지 않나 매번 리스트에 있는 모든 수를 sum 해줘야하는데??
#짧은건 이게 덜 걸림.

print(solution2([1,3,2,5,4],9),"result: 3")
print(solution2([2,2,3,3],10),"result: 4")