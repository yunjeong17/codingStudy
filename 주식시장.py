#주식시장 (스택/큐)
# https://programmers.co.kr/learn/courses/30/lessons/42584


# 1 > 2 > > 3 > 2>  3 처음숫자보다 줄어든적 없음 4
# 2 > 3 > 2 > 3 처음숫자보다 줄어든적 없음 3
# 3 > 2 1초만에 줄어듦
# 2 > 3  줄어든적없음 1
# 3 뒤에 없음 0

#정확성은 만점인데 효율성 0점 ㅠㅠ 다시 풀것... 어떻게 하면 for문을 줄일 수 있지? for문 안쓰고싶은데...
def solution1(prices):
    lst=prices
    answer=[]
    count=0
    while prices:
        m=prices.pop(0)
        for j in prices:
            count+=1
            if m>j:
                break
        answer.append(count)
        count=0
    return answer

print(solution1([1, 2, 3, 2, 3]),"return: [4, 3, 1, 1, 0]")
print(solution1([5, 8, 6, 2, 4, 1]),"return:  [3, 1, 1, 2, 1, 0]")


# 5 > 8 > 6 > 2 :: 4
# 8 > 6 :: 1
# 6 > 2 :: 1
# 2 > 4 > 1 :: 2
# 4 > 1 :: 1
# 1 :: 0
