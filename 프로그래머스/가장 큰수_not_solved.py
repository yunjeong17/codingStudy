# 문제 : 가장 큰 수
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    answer = ''
    n=map(str,numbers)
    num=sorted(n, key=lambda x:x[0])
    num.reverse()
    print(num)
    return answer

# print(solution([6, 10, 2]),'result:"6210"')
print(solution([3, 30, 34, 5, 9]),'result:	"9534330"')
# print(solution(),'result:')