#평균 구하기
#https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    answer = 0
    for i in arr:
        answer+=i
    answer=answer/len(arr)
    return answer

# 20210811 다시 풀어봤음
def solution2(arr):
    return sum(arr)/len(arr)

print(solution2([1,2,3,4]))