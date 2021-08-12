#두 정수 사이의 합
#https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    if(a<b):
        for i in range(a,b+1):
            answer+=i
            print(a,b,i)
            print("sfsdf",answer)
    elif(a>b):
        for i in range(b,a+1):
            answer+=i        
    else:
        answer=a


    return answer

# 짧게 다시 풀어보기
def solution2(a, b):
    answer =0
    return answer

# print("1:",solution(3,5)) #12
# print("2:",solution(3,3)) #3
# print("3:",solution(5,3)) #12