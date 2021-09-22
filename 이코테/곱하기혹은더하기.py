# 이코테 13강 그리디
# 곱하기 혹은 더하기
# 각자리가 숫자로 이루어진 문자열 s
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자 확인하며 숫자 사이에 x 혹은 + 연산자를 넣음
# 만들어질 수 있는 가장 큰 수 구하는 프로그램
# 모든 연산은 왼쪽에서부터 순서대로

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

#책 풀이
def solution2():
    data=input()
    result=int(data[0])
    for i in range(1,len(data)):
        num=int(data[i])
        if num<=1 or result<=1:
            result+=num
        else:
            result*=num
    return result


