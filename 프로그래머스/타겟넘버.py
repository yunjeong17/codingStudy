# 문제 : 타겟넘버
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/43165
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.

# 다른사람 풀이 1 : dfs >재귀함수 이용
def solution1(numbers, target):
    global answer
    answer = 0
    N = len(numbers)

    def dfs(idx, numbers, total):
        global answer
        if (idx == N) and (total == target):
            answer += 1
            return
        if idx == N:
            return
        dfs(idx + 1, numbers, total + numbers[idx])
        dfs(idx + 1, numbers, total - numbers[idx])

    dfs(0, numbers, 0)
    return answer

# 다른 사람 풀이 2 :bfs > 큐 이용
from collections import deque

def solution2(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, level
    while queue:
        s, l = queue.popleft()
        print(s,l,len(numbers))
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))
        print(queue)
    return answer

# 내 풀이!
# 다른사람 풀이 참고해서 dfs > stack이용해서 풀어보기
def solution3(numbers,target):
    answer=0
    stacks=[(0,0)]
    while stacks:
        total,level=stacks.pop()
        # print('뀨',(total,level),stacks)
        temp1=total
        temp2=total
        if len(numbers)==level and target==total:
            answer+=1
            # print("answer+++",(total,level),stacks)
            continue
        if level>=len(numbers):
            continue
        stacks.append((total+numbers[level],level+1))
        stacks.append((total-numbers[level],level+1))
    return answer

print(solution3([1, 1, 1, 1, 1], 3), 5)
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# --> 5가지 방법


print(solution3([1, 2, 1, 2], 2), 3)
# 1 2 1 -2
# 1 -2 1 2
# -1 2 -1 2
# --> 3가지 방법


print(solution3([1, 2, 1, 2], 6), 1)
# 1 2 1 2
# --> 한 가지 방법
