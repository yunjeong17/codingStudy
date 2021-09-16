# 이코테 13강
# 곱하기 혹은 더하기

#내 풀이
def solution():
    str=input()
    result=0
    for i in str:
        intI=int(i)
        if intI<=1 or result==0:
            result+=intI
        else:
            result*=intI
    return result

print(solution())

def solution2():
    result=0
    return result


