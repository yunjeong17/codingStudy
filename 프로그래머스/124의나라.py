# 문제 : 124의 나라
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/12899

# 3진법하듯이
# 사용할수 있는 수 : 012 -> 123 - > 124
# 질문하기에서 본거 참고해서 함
def solution(n):
    answer = ''
    while True:
        k=n%3
        if k==0: #나머지가 없을 때 3으로
            n=n//3 # 1 안빼주면 안됨 다른 진법과 다르게 0이 없어서 
            print("n:",n)
            answer+=str(3) 
        else:
            answer+= str(n%3)
            n=n//3
            print("n:",n)
        print(n)
        if n<3:
            break
    answer+=str(n)
    answer=''.join(reversed(answer)).lstrip('0').replace('3','4')
    return answer

# print(solution(1),"result: 1")
# print("====================")
# print(solution(2),"result: 2")
# print("====================")
# print(solution(3),"result: 4")
# print("====================")
# print(solution(4),"result: 11")
# print("====================")
# print(solution(10),"result: 41")
# print("====================")
# print(solution(18),"result: 124")

def getNum(num,lst):
    a=num//3
    b=num%3

    print(a,"  ",b)
    if a==0:
        return lst
    else:
        return getNum(num,lst)

def solution2(n):
    answer=''
    num=['1','2','4']
    lst=[]
    l=getNum(n,lst)
    print(l)
    return answer

# print(getNum(18,[]))

# print(solution2(3),"result: 4")
# print("====================")
# print(solution2(18),"result: 124")

def solution3(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        if mod!=0:
            answer += str(mod)
        else :
            n-=1
            answer += str('4')
            

    return answer[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 answer가 출력
    # https://blog.wonkyunglee.io/3
    
print(solution3(18))