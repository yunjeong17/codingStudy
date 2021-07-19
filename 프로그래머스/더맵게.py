# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626
# heapq 모듈 사용
# 최초 힙은 빈 리스트 []
# heapq.heappop(힙) : 힙에서 가장 작은 수 팝
# heapq.heappush(힙, 넣을 요소) : 오름차순 위치에 맞는 곳에 요소를 push


import heapq

#오래걸림 안좋음
def solution(scoville, K):
    count=0
    while scoville[0] < K :
        newScoville=scoville[0]+(scoville[1]*2)
        scoville[0]=newScoville
        scoville.pop(1)
        scoville.sort()
        count+=1
        if len(scoville)<2 and scoville[0]<K:
            count=-1
            break
    return count


def solution(scoville,K):
    count=0
    newScoville=0
    scoville.sort()
    if K==0:
        return 0
    while scoville[0]<K:
        n1=heapq.heappop(scoville)
        n2=heapq.heappop(scoville)
        newScoville = n1+(n2 * 2)
        heapq.heappush(scoville,newScoville)
        count+=1
        if len(scoville) < 2 and scoville[0]<K:
            count=-1
            break
    return count


print("1:",solution([1,2,3,9,10,12],7), 2)
print("2:",solution([1, 1, 1], 4), 2)
print("3:",solution([10, 10, 10, 10, 10], 100), 4)
print("4:",solution([1, 2, 3, 9, 10, 12], 7), 2)
print("5:",solution([0, 2, 3, 9, 10, 12], 7), 2)
print("6:",solution([0, 0, 3, 9, 10, 12], 7), 3)
print("7:",solution([0, 0, 0, 0], 7), -1)
print("8:",solution([0, 0, 3, 9, 10, 12], 7000), -1)
print("9:",solution([0, 0, 3, 9, 10, 12], 0), 0)
print("10:",solution([0, 0, 3, 9, 10, 12], 1), 2)
print("11:",solution([0, 0], 0), 0)
print("12:",solution([0, 0], 1), -1)
print("13:",solution([1, 0], 1), 1)
print("14:",solution([1,2], 3), 1)