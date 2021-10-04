# 번호 : 1260
# 문제 : dfs와 bfs
# 링크 : https://www.acmicpc.net/problem/1260
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
#  단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
#  더 이상 방문할 수 있는 점이 없는 경우 종료한다.
#  정점 번호는 1번부터 N번까지이다.


# 입력
# 첫째 줄에 
#  정점의 개수 N(1 ≤ N ≤ 1,000), 
#  간선의 개수 M(1 ≤ M ≤ 10,000),
#  탐색을 시작할 정점의 번호 V가 주어진다. 

# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력 
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

# def dfs(graph,v,visitedDFS): #깊이우선탐색
#     stacks=[v]
#     while stacks:
#         stack=stacks.pop()
#         visitedDFS[stack]=True
#         print(stack,end=' ')

#         for i in graph[stack]:
#             if visitedDFS[i]==False and i not in stacks:
#                 stacks.append(i)
#                 break
#     print()


# def bfs(graph,v,visitedBFS): #너비우선탐색
#     queues=[v]

#     while queues:
#         queue= queues.pop(0)
#         visitedBFS[queue]=True
#         print(queue,end=' ')

#         for i in graph[queue]:
#             if visitedBFS[i]==False and i not in queues:
#                 queues.append(i)


# n, m, v = map(int,input().split(' '))
# graph=[[] for i in range(n+1)]

# for i in range(m):
#     n1,n2=map(int,input().split(' '))
#     graph[n1].append(n2)
#     graph[n2].append(n1)
# print("==-=====")

# for i in graph:
#     i.sort()

# visitedDFS=[False]*(n+1)
# visitedBFS=[False]*(n+1)

# dfs(graph,v,visitedDFS)
# bfs(graph,v,visitedBFS)

#데이터 받기
n, m, v = map(int,input().split(' '))

graph=[[] for i in range(n+1)] # 노드 간선정보를 넣을 그래프
for i in range(m):
    n1,n2=map(int,input().split(' '))
    graph[n1].append(n2)
    graph[n2].append(n1)

#dfs는 스택구조 쓸거라 뒤에서부터 pop한다. 그러므로 내림차순으로 정렬해야한다.
for i in graph:
    i.sort(reverse=True)

visitedDFS=[False]*(n+1) # DFS로 방문한 노드 저장, false는 방문하지 않음을 뜻하고 true는 방문함을 뜻함.

#============================dfs============================
stacks=[v]
resultDFS=[] # DFS로 방문한 노드 순서를 저장
while stacks:
    stack=stacks.pop()
    visitedDFS[stack]=True
    if stack not in resultDFS: #stacks에 이미 방문한 곳을 가지고있을 수 있으므로 한번 더 걸러준다 
        resultDFS.append(stack)
    for i in graph[stack]:
        if visitedDFS[i]==False : # 아직 방문하진 않았지만 스택에 있을 수 있는 상태
            stacks.append(i)

#dfs 출력
for i in resultDFS:
    print(i,end=' ')

print() #줄바꿈

#=====================bfs============================
visitedBFS=[False]*(n+1)

#bfs는 
for i in graph: 
    i.sort()

queues=[v]
resultBFS=[] #BFS 노드 방문 순서를 저장
while queues:
    queue= queues.pop(0)
    visitedBFS[queue]=True
    if queue not in resultBFS:
        resultBFS.append(queue)
    for i in graph[queue]:
        if visitedBFS[i]==False :
            queues.append(i)

#bfs출력
for i in resultBFS:
    print(i,end=' ')
