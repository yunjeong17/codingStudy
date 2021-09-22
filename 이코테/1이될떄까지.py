#이코테 13강 그리디 
# 1이 될 때까지

# 문제 
# n:17 ,k:4
# 두 과정중 하나를 반복적으로 선택 해 수행 
# 단, 2번째 연산은 n이 k로 나누어 떨어질때만 선택 가능
# 1. n에서 1을 뺍니다
# 2. n을 k로 나눕니다.

# 내풀이
def solution():
    n,k=map(int,input().split())
    cnt=0
    while n!=1:
        if n%k==0:
            n=n//k
        else:
            n-=1
        cnt+=1
    print(cnt)

#책 풀이
def solution2():
    n,k=map(int,input().split())
    result=0

    while True:
        # n이 k로 나누어 떨어지는 수가 될 때 까지 빼기
        target = (n//k)*k 
        result+=(n-target) 
        n=target

        #n이 k보다 작을 때 (더이상 나눌 수 없을때) 반복문 탈출
        if n<k:
            break
        result+=1

        #k로 나누기
        n//=k
    #마지막으로 남은 수에 대하여 1 씩 빼기
    result+=(n-1)
    print(result)


solution()
solution2()