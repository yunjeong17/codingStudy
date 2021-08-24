#두 정수 사이의 합
#https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    if(a<b):
        for i in range(a,b+1):
            answer+=i
    elif(a>b):
        for i in range(b,a+1):
            answer+=i        
    else:
        answer=a


    return answer

# 부호를 선언해서 코드를 간결하게 해봤는데 복잡도 면에서는....
def solution2(a, b):
    sign = -1 if a>b else 1
    answer= [x for x in range(a,b+sign,sign) ]
    return sum(answer)


# 절댓값 이용 수학공식사용
# 등차수열일떄  사용 가능
# 합공식 : 1부터 n까지의 합은 n*(n+1)//2
# a부터 b까지의 합은 (숫자의 개수 : abs(a-b)+1)*(끝수+첫수)//2

# 엄청 오랜만에 보는 공식인듯.. 수학공부도 해야할거같다..
def solution3(a, b):    
    return (abs(a-b)+1) * (a+b) // 2

print("1:",solution3(3,5)) #12
print("2:",solution3(3,3)) #3
print("3:",solution3(5,3)) #12