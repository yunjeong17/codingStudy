#주식시장 (스택/큐)
# https://programmers.co.kr/learn/courses/30/lessons/42584


def solution(prices):
    answer=[]
    count=0


    return answer

print(solution([1, 2, 3, 2, 3]),"return: [4, 3, 1, 1, 0]")

# 1 > 2 > > 3 > 2>  3 처음숫자보다 줄어든적 없음 4
# 2 > 3 > 2 > 3 처음숫자보다 줄어든적 없음 3
# 3 > 2 1초만에 줄어듦
# 2 > 3  줄어든적없음 1
# 3 뒤에 없음 0

r=[1,2,3,4,5,6]
print(r)
print(len(r))
print(r[-1])
print(r[-6])