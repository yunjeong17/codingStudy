#이것이 취업을 위한 코딩테스트다 with python 
# 93페이지
# 큰 수의 법칙

import time

def solution():
    sum=0
    n,m,k=map(int, input().split())
    data=list(map(int, input().split())) 
    start_time = time.time()  # 시작 시간 저장
    data.sort()
    
    for i in range(m):
        if i%k==1 and i!=1:
            max=data[-2]
        else :
            max=data[-1]
        sum+=max
    end_time=time.time() 

    print("WorkingTime: {} sec".format(end_time-start_time))
    return sum



print('sum:',solution())


# 나는 이렇게 풀었는데 for문 돌아가는게 매우 비효율적.
# 그냥 한번에 곱셈으로 돌려버리는게 나은듯