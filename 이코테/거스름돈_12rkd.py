# 이코테 12강 그리디
# 거스름돈 

# 내 풀이
def solution(money):
    coin=[500,100,50,10]
    result=[]
    for c in coin:
        if money!=0:
            result.append(money//c)
            money-=c*result[-1]
    
    return sum(result)


print(solution(1260),'result:6')

# 영상 풀이
def solution2():
    n=1260
    count=0
    array=[500,100,50,10]

    for coin in array:
        count+=n//coin
        n%=coin

    return count

print(solution2(),'result:6')