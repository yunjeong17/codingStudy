#https://programmers.co.kr/learn/courses/30/lessons/12906
#같은 숫자는 싫어


def solution(arr):
    answer = []
    k=0
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if(arr[i]!=answer[k]):
            answer.append(arr[i])
            k+=1
        print("arr:",arr[i],"answer: ",answer[k])
    return answer

arr=[1,1,3,3,0,1,1]
print(solution(arr))


def solution2(arr):
    answer = []
    answer.append(arr.pop(0))
    while arr:
        a=arr.pop(0)
        if(a!=answer[-1]):
            answer.append(a)
    return answer

arr=[1,1,3,3,0,1,1]
print(solution2(arr))