# 문제 : 단어변환
# 링크 : https://programmers.co.kr/learn/courses/30/lessons/43163
# dfs(깊이우선탐색) 이용
# - 깊은 부분을 우선적으로 탐색하는 알고리즘
# - 스택 자료구조(혹은 재귀함수)를 이용
# - 동작과정
#     1. 탐색 시작 노드를 스택에 삽입하고 방문처리
#     2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
#     3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복

def dfs(begin,target,words,visited,answer):
    stacks = [begin]
 
    while stacks:
        # 스택을 활용한 dfs 구현
        stack = stacks.pop()
        
        if stack == target:
            return answer
        
        for w in range(0,len(words)):
            if sum([s != w for s, w in zip(stack, words[w])]) == 1 and visited[w] == False:
                visited[w] = True
                stacks.append(words[w])
        

        answer +=1

def solution(begin, target, words):
    answer=0
 
    if target not in words:
        return 0
    
    visited = [False]*len(words)
    answer=dfs(begin,target,words,visited,answer)
 
    return answer


# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"]), 3)
# print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)
# print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]),'result:4')
# print(solution("hit","cog",	["hot", "dot", "dog", "lot", "log"]),'result:0')