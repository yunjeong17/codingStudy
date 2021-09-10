# 문제 : H-index
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42747#fn1

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(1,len(citations)+1):
        print(i,citations[:i],citations[i:])
        if min(citations[:i]) >= i and max(citations[i:]+[0])<=i:
            answer=i

    return answer

print(solution([3, 0, 6, 1, 5]),'result:3')
print("--------------------------")
print(solution( [1, 3, 5, 7, 9, 11] ),'result:4')
print("--------------------------")
print(solution( [6,5,4,1,0] ),'result:3')
print("--------------------------")
print(solution( [4,4,4] ),'result: 3')