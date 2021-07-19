# 이것이 취업을 위한 코딩테스트다 with python 
# p.98
# 숫자 카드 게임

def solution():
    n,m=map(int, input().split())
    lst=[]
    num=0
    for i in range(n):
        lst.append(list(map(int, input().split())) )
        if num <min(lst[i]):
            num=min(lst[i])
    return num
    
print(solution())