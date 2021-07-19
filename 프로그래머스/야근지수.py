# 야근지수
# https://programmers.co.kr/learn/courses/30/lessons/12927
import heapq
#효율성 0점 ㅎㅎㅎㅎㅎㅎㅎㅎㅎ
def solution1(n, works):
    answer = 0
    for i in range( 1, n + 1 ):
        works[ works.index( max(works) ) ]-= 1
        if max(works) <= 0 :
            return answer
        elif i == n :
            for j in works:
                answer +=(j**2)
    print(works)
    return answer


# 최소힙을 이용해 최대힙을 만듦. (파이썬에는 최대 힙이 없음!)
# 원소를 마이너스 값을 줘서 최대 숫자를 최소숫자로 바꿈 
# (어차피 제곱할거기때문에 -여도 상관없기도하고 제곱을 안할거여도 나중에 다시 - 해줘서 +로 바꿔주면됨.)
# 위에껀 매번 works의 max값을 찾아서 그것에 -1을 해주는거였는데 이러면 매번 max를 계산하니 sort를 매번하는거랑 마찬가지로 오래걸리는듯.
def solution2(n, works):
    answer = 0
    max_heap = []
    for item in works:
        heapq.heappush(max_heap, -item)

    for i in range(n):
        pop=heapq.heappop(max_heap)
        heapq.heappush(max_heap,pop+1)
        if len(max_heap)==0: #힙에 남은게 없으면 for문을 멈춤
            break
        if i+1==n:
            for j in max_heap:
                answer+=j**2

    
    return answer

def solution3(n, works):
    answer = 0
    max_heap = []
    if n>=sum(works): #힙에 남은게 없으면 for문을 멈추는것보다 애초에 n이 모든 works의 합보다 크거나 같으면 아예 for문에 안들어가고 return 하는게 빠름
        return answer
    for item in works:
        heapq.heappush(max_heap, -item)

    for i in range(n):
        pop=heapq.heappop(max_heap)
        heapq.heappush(max_heap,pop+1)

        if i+1==n:
            for j in max_heap:
                answer+=j**2
    return answer
    
# print(solution1(4,[3, 3, 4]),"result: 12")
# print(solution1(1,[2, 1, 2]),"result: 6")
# print(solution1(3,[1,1]),"result: 0")
# print(solution1(99, [2, 15, 22, 55, 55]),"result: 580")

# print(solution2(4,[3, 3, 4]),"result: 12")
# print(solution2(1,[2, 1, 2]),"result: 6")
# print(solution2(3,[1,1]),"result: 0")
# print(solution2(99, [2, 15, 22, 55, 55]),"result: 580")

print(solution3(4,[3, 3, 4]),"result: 12")
print(solution3(1,[2, 1, 2]),"result: 6")
print(solution3(3,[1,1]),"result: 0")
print(solution3(99, [2, 15, 22, 55, 55]),"result: 580")