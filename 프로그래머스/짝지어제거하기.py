# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973


#스택이용해서 풀어봄!! o(N)
def solution1(s):
    answer=-1
    stack=[]
    for i in s:
        stack.append(i)
        if len(stack) > 1 :
            if(stack[len(stack)-1]==stack[len(stack)-2]):
                stack.pop()
                stack.pop()
    if(len(stack)==0):
        answer=1
    else:
        answer=0
    return answer


print(solution1("baabaa"),"result:1")
print(solution1("cdcd"),"result:0")




#너무 오래걸림 O(N^2)
def solution2(s):
    answer = -1
    lst=list(s)
    count=0
    while True:
        for i in range(len(lst)-1):
            if lst[i]==lst[i+1]:
                lst.pop(i)
                lst.pop(i)
                break
            if(i==len(lst)-2):
                return 0
        if len(lst)==0:
            return 1
    return answer

print(solution2("baabaa"),"result:1")
print(solution2("cdcd"),"result:0")

