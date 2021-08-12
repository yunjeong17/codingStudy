#https://programmers.co.kr/learn/courses/30/lessons/68935
#3진법 뒤집기

def solution(n):
    lst=[]
    answer=0
    while 1:
        mok=int(n%3)
        n=int(n/3)
        lst.append(mok)
        if ( (n<3) & (n!=0) ):
            lst.append(n)
            break
        if(n==0):
            break
    for i in range(0,len(lst)):
        answer+=lst[i]*3**(len(lst)-i-1)
    return answer

def solution2(n):
    answer=0
    lst=[]
    while n>0:
        n,d=divmod(n,3)
        lst.append(d)
    lst.reverse()
    for i in range(len(lst)):
        answer+=(lst[i]*(3**i))
    return answer

def solution3(n):
    answer=0
    lst=[]
    while n>0:
        n,d=divmod(n,3)
        lst.append(d)
    a=''.join(map(str,lst))
    answer=int(a,3)
    return answer

print(solution3(45))
print(solution3(1))