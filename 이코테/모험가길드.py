# 이코테 13강 그리디
# 모험가 길드

# 공포도 x인 모험가는 반드시 x명 이상 구성한 모험가 그룹에 참여
# 여행을 떠날 수 있는 "그룹 수의 최댓값"
# 몇명의 모험가는 마을에 남아있어도 됨
def solution():
    n=input()
    lst=list(map(int, input().split(' ')))
    lst.sort()
    print(lst)
    group=0
    count=0
    for i in lst:
        count+=1
        if count>=i:
            group+=1
            count=0
    return group

# 5
# 2 3 1 2 2
print(solution())